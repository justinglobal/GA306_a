"""This script prints some information and creates a spike ball."""
import maya.cmds

def addSpikes(obj):
    """This function adds spikes to a polygon object."""
    try: polycount = mya.cmds.polyEvaluate(obj, face=True)
    except: raise
    for i in range(0, polycount):
        face = '%s.f[%s]'%(obj, i)
        maya.cmds.polyExtrudeFacet(face, ltz=1, ch=0)
        maya.cmds.polyExtrudeFacet(face, ltz=1, ch=0, ls=[.1,.1,.1])
    maya.cmds.polySoftEdge(obj, a=180, ch=0)
    maya.cmds.select(obj)
    
def create_car(name, length=2, width=1):
    # Create the car components
    body = create_body(length, width)
    tires = create_tires(length, width)
    
    # Group the car components
    final_name = assemble_car(name, body, tires)
    
    # Clear any selections in the scene
    cmds.select(clear=True)
    
    return final_name
    
def create_body(length=2, width=1):
    # Create a plane that represents the car body.
    # Return the transform node name.
    body = cmds.polyPlane(w=length, h=width, name="body")
    addSpikes(body[0])
    return body[0]
    
def create_tires(body_length, body_width):
    # Create four tires for the car.
    # Size and position are relative to the body dimensions.
    tire_width = 0.25 * body_width
    tire_radius = 0.25 * body_length
    x_pos = 0.5 * body_length
    z_pos = 0.5 * body_width + 0.5 * tire_width
    
    fl_tire = create_tire("front_left_tire", tire_width, tire_radius, x_pos, 0, -z_pos)
    fr_tire = create_tire("front_right_tire", tire_width, tire_radius, x_pos, 0, z_pos)
    rl_tire = create_tire("rear_left_tire", tire_width, tire_radius, -x_pos, 0, -z_pos)
    rr_tire = create_tire("rear_right_tire", tire_width, tire_radius, -x_pos, 0, z_pos)
    
    return [fl_tire, fr_tire, rl_tire, rr_tire]
    
def create_tire(name, width, radius, tx, ty, tz):
    # Create a cylinder that represents a tire.
    # Return the transform node name.
    tire = cmds.polyCylinder(h=width, r=radius, ax=(0,0,1), sc=True, name=name)
    cmds.setAttr("{0}.translate".format(tire[0]), tx, ty, tz)
    return tire[0]
    
def assemble_car(name, body, tires):
    # Create groups for the body and tires and parent them
    # under the main car group.
    # Return the car group name.
    body_grp = cmds.group(body, name="body_grp")
    tires_grp = cmds.group(tires, name="tires_grp")
    
    car_grp = cmds.group(body_grp, tires_grp, name=name)
    return car_grp
    
if __name__ == "__main__":
    name = create_car("test_car")
    print("Car created: {0}".format(name))
    


#print('module name: %s'%__name__)
#print('globals:')
#for k in globals().keys(): print('\t%s'%k)
#addSpikes(maya.cmds.polyPrimitive(ch=0)[0])