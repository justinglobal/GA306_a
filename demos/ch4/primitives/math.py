import maya.cmds
pi = 3.1415926535897931
def getCircumference(obj):
    try: return maya.cmds.getAttr('%s.radius'%obj) * 2.0 * pi
    except: raise
def getHeight(obj):
    try: return maya.cmds.getAttr('%s.height'%obj)
    except: raise