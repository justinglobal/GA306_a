import maya.cmds
def cone(**kwargs):
    try: return maya.cmds.polyCone(**kwargs)[1]
    except: raise
def cube(**kwargs):
    try: return maya.cmds.polyCube(**kwargs)[1]
    except: raise
def cylinder(**kwargs):
    try: return maya.cmds.polyCylinder(**kwargs)[1]
    except: raise
def plane(**kwargs):
    try: return maya.cmds.polyPlane(**kwargs)[1]
    except: raise
def sphere(**kwargs):
    try: return maya.cmds.polySphere(**kwargs)[1]
    except: raise
def torus(**kwargs):
    try: return maya.cmds.polyTorus(**kwargs)[1]
    except: raise