Welcome to Class!

Week 5 Opening Exercise:

Use the example code from the cube rotation/sphere location demo from page 42 in your book, also found below:

```py
import maya.cmds
sphere = maya.cmds.polySphere()[0]
cube = maya.cmds.polyCube()[0]

maya.cmds.connectAttr(cube+'.ry', sphere+'.ty')
maya.cmds.select(cube)
```

Using the code above, write a function that does the following:
1. takes 1 argument, an integer representing the length/width/height of the cube
1. sets the cubes dimensions when it is created to the unit input in the argument
1. sets the sphere's radius to *half* the cube's dimensions
