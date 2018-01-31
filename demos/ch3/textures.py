import os
import maya.cmds
import maya.mel

def process_all_textures(out_dir = os.getenv('HOME'), new_file='processed.ma'):
    """
    A function that gets a list of textures from the current scene
    and process each texture according to name
    """
    texture_nodes = [i for i in maya.cmds.ls(type='file') if is_valid_texture(i)]
    processed_textures = []
    error_textures = []
    skipped_textures = []
    if not texture_nodes:
        maya.cmds.warning('No textures found, exiting')
        return (processed_textures, error_textures, skipped_textures)
    for name in texture_nodes:
        print('Processing texture %s'%name)
        as_type = None
        status = False
        texture = None
        if '_diff' in name:
            status, texture = process_diffuse(name, out_dir)
            if status:
                processed_textures.append(texture)
                as_type = 'diffuse'
            else:
                error_textures.append(texture)
        elif '_spec' in name:
            status, texture = process_spec(name, out_dir)
            if status:
                processed_textures.append(texture)
                as_type = 'specular'
            else:
                error_textures.append(texture)
        elif '_bump' in name:
            status, texture = process_bump(name, out_dir)
            if status:
                processed_textures.append(texture)
                as_type = 'bump'
            else:
                error_textures.append(texture)
        if status:
            print('Processed %s as a %s texture'%(texture, as_type))
        else:
            print('Failed to process %s'%name)
    try:
        maya.cmds.file(
            rename=os.path.join(
                out_dir, new_file
            )
        )
        maya.cmds.file(save=True)
    except:
        print('Error saving file, %s not saved.'%new_file)
    finally:
        return (processed_textures, error_textures, skipped_textures)

def is_valid_texture(file_node):
    """
    Return whether or not the specified file node is actually connected to any models
    """
    shaders = maya.cmds.listConnections(
        '%s.outColor'%file_node,
        destination=True
    )
    if not shaders: return False
    for shader in shaders:
        groups = maya.cmds.listConnections('%s.outColor'%shader)
        if not groups: return False
        for group in groups:
            meshes = maya.cmds.listConnections(group, type='mesh')
            if meshes:
                if '_diff' in file_node: return True
                elif '_spec' in file_node: return True
                elif '_bump' in file_node: return True
    return False

def process_diffuse(file_node, out_dir):
    """
    Process a file node's texture, re-assign the new texture
    and return a status and texture name
    """
    status = False
    texture = None
    file_name = maya.cmds.getAttr('%s.ftn'%file_node)
    meshes = []
    shaders = maya.cmds.listConnections(
        '%s.outColor'%file_node,
        destination=True
    )
    if shaders:
        for s in shaders:
            groups = maya.cmds.listConnections(
                '%s.outColor'%s
            )
            if groups:
                for g in groups:
                    m = maya.cmds.listConnections(
                        g, type='mesh'
                    )
                    if m: meshes += m
    try:
        # processing code would be here
        new_file_name = file_name
        # new_file_name is the processed texture
        shader = maya.cmds.shadingNode(
            'blinn',
            asShader=True
        )
        shading_group = maya.cmds.sets(
            renderable=True,
            noSurfaceShader=True,
            empty=True
        )
        maya.cmds.connectAttr(
            '%s.outColor'%shader,
            '%s.surfaceShader'%shading_group
        )
        texture = maya.mel.eval(
            'createRenderNodeCB -as2DTexture "" file ""'
        )
        maya.cmds.setAttr(
            '%s.ftn'%texture,
            new_file_name,
            type='string'
        )
        maya.cmds.connectAttr(
            '%s.outColor'%texture, '%s.color'%shader
        )
        for mesh in meshes:
            maya.cmds.sets(
                mesh,
                edit=True,
                forceElement=shading_group
            )
        status = True
    except:
        texture = file_node
        status = False
    return (status, texture)