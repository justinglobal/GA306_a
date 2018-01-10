import maya.OpenMaya as om
import maya.cmds as cmds
import random, time

def arPolyNoise(geoObject, maxDisplacement):
    """Apply noise to the supplied geometry object using the supplied max displacement."""
    # get the dag path for the shapeNode using an API selection list
    selection = om.MSelectionList()
    dagPath = om.MDagPath()
    try:
        selection.add(geoObject)
        selection.getDagPath(0, dagPath)
    except: raise
    # apply noise to the shape's points
    try:        
        # initialize a geometry iterator
        geoIter = om.MItGeometry(dagPath)
        # get the positions of all the vertices in world space
        pArray = om.MPointArray()
        geoIter.allPositions(pArray)
        # displace each of the vertices
        for i in xrange(pArray.length()):
            displacement = om.MVector.one * random.random() * maxDisplacement
            pArray[i].x += displacement.x
            pArray[i].y += displacement.y
            pArray[i].z += displacement.z
        # update the surface of the geometry with the changes
        geoIter.setAllPositions(pArray)
        meshFn = om.MFnMesh(dagPath)
        meshFn.updateSurface()
    except: raise

# start the timer and add the noise
timeStart = time.clock()
# create a sphere and add noise
sphere = cmds.polySphere(radius=1, subdivisionsX=200, subdivisionsY=200)
arPolyNoise(sphere[0], 0.02)
# stop the timer
timeStop = time.clock()
print('Execution time: %s seconds.'%(timeStop-timeStart))