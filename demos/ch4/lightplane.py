import maya.cmds as cmds
cmds.pointLight(name='red_light',rgb=[1,0,0],position=[0,2.5,0]) 
cmds.polyPlane(width=10,height=10)