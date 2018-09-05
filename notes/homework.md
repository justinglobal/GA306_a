1. Week 1
    - Read Introduction and Chapter 1 of text
    - Do Chapter 1 Terms, turn in on slack

1. Week 3 (due Week 4)

    1. What version of Python is being used in your version of Maya?

    1. Convert the following MEL statements to Python:
        - polyCylinder -h 3 -r 1 -sc 2 -ch 1;
      	- polySphere -r 3 -sx 8 -sy 8 -ch 1;
        - polyTorus -r 1 -sr 0.5 -tw 5 -sx 20 -sy 20 -ch 1;
        - polyCube -w 9 -h 9 -d 9 -sx 3 -sy 3 -sz 3 -ch 1;

    1. If you run this code:

        the_answer = “42”

        - What type of variable is the_answer?

        - What Python command can you run to confirm this?

    1. Most Maya commands have these three modes: create, query, and edit.  Explain what each means.

    1. For the following list: my_list = [2, 3, 7, 8, 9]
      	- What is the value of my_list[1]?

        - What is the value of my_list[-1]?

        - What is the value of my_list[:-1]?

        - What is the value of my_list[::-1]?

        - What is the value of my_list[1:-1]?

    1. Reformat the print statement to use % string formatting:

        a = 5

    	  b = 3

        c = pow(a, b)

        print(str(a) + “ to the “ + str(b) + “ power is “ + str(c))

    1. Write a short Python script that does the following:
    	 - Create a sphere

    	 - Create a locator

       - Connect the locator Y-translate attribute to the sphere scale (Hint: use the connectAttr() command.)

1. Week 4 - Read Chapter 3 up to page 80

1. Week 5 - Answer the following questions:

      The goal of this assignment is for you to become familiar with using variables, lists, and functions to do the majority of the work in your code.

    1. Write a function called rename_obj that takes a string as an argument to rename a selected Maya object.
        - (Hint: use  my_selection = maya.cmds.ls(selection=True) This assigns any selected objects in the scene to a list called “my_selection”.)

    1. Explain what a for loop is, and write a function that uses it to print the name of each object in a list.
        - (Hint: This list of objects could be called “my_selection”)

    1. Explain what the range command does, and write a function that uses it to print the numbers 0 through 9.

    1. Write a function called print_parents that takes a list of Maya objects as an arguments and prints each node and its parent node.
          - (Hint: use listRelatives command.)
        1. Create four objects in the scene.  Cube, Sphere, Cylinder, Torus.
        1. Parent Torus under Cylinder. Then parent Cylinder under Sphere. Then parent Sphere under Cube.
        1. Use the example hierarchy below for the objects required for the print_parent function.
            - ( Torus > Cylinder > Sphere > Cube)
        1. Format a print statement using % notation that list the selected object and all of its parent nodes.
            - (eg: “Selected Geometry: <pSphere1> , Parents: <pCube1>”)


    1. ADVANCED (Optional)

        1. Write a function called get_poly_info that takes a Maya node as an argument and returns a dictionary with keys vertex, edge, and face and values are the number of each in that piece of geometry.  (Hint: the Maya command that gives you that information is called polyEvaluate.)



        1. Write a function called find_center that takes a Maya geometry node as an argument.  Since you should know how to get the number of vertices in a mesh, use this number to create a for range loop to find the average/center position of the mesh.  (Hint: xform(<geom.vertex>, q=True, ws=True, t=True))



        1. Using list comprehension, create a Python list that consists of all meshes with more than 100 faces.  (Hint: use the ls command type arg to get the meshes and the polyEvaluate to get the number of faces)

1. Week 7
    1. Finish all homework not turned in
    1. Turn in all homework before next class
    1. Due Week 8 : Define all terms in [Terms list](/notes/terms.md)
    1. Quiz over terms (15 question short answer) Week 8


1. Week 8
    - Project: Car controller
      - Go to this page: https://github.com/justinglobal/GA306_a/blob/master/practice/create_car.py
      - Download the 'creat_car.py' file by right clicking on the 'Raw' button near the top right, then select "Save Link as..." Save the file to your computer.
      - Make a basic cube, whatever dimensions you choose (default size is fine).
      - Make a "controller" that moves the car along the x/z space by rotating the cube you just made in two dimensions.
      - Hint: You'll be connecting the car's x/z translation to the cube's x/z rotation. A demo of this behavior using the connectAttr() function can be found on p.42 of your book.
      - Save your file as 'control_car.py'

1. Week 9
    - Read Chapter 4 Modules to page 128.


<!-- 1. Week 2
    - Finish reading Chapter 1, read Chapter 2 to page 46
    - Answer the following questions and save in .txt format
        1. Name the four Maya programming interfaces.
        1. What are the three ways to run Python in Maya?
        1. What version of Python is being used in your version of Maya?
        1. If you run this code:
            - test_variable = “12345”
            1. What type of variable is the_answer?  
            1. What Python command can you run to confirm this?
        1. Most Maya commands have these three modes: create, query, and edit. Explain what each means.
    - Write a short Python script that does the following:
        1. Create a sphere
        1. Create a locator
        1. Connect the locator Y-translate attribute to the sphere scale
        1. Save script as follows: [your last name]-ga306-[assignment week]-[description (if necessary)].[extension]
        Example: epperly-ga306-week2.py
    - You will turn in 2 files, a .txt file with your answers, and a .py file with your script
    - Send homework to instructor via Slack

1. Week 3
    - Read pp. 47 - 71 (Finishes Ch.2 and first 10 pages of Ch.3)
    - Project: Car controller
      - Go to this page: https://github.com/justinglobal/GA306_a/blob/master/practice/create_car.py
      - Download the 'creat_car.py' file by right clicking on the 'Raw' button near the top right, then select "Save Link as..." Save the file to your computer.
      - Make a basic cube, whatever dimensions you choose (default size is fine).
      - Make a "controller" that moves the car along the x/z space by rotating the cube you just made in two dimensions.
      - Hint: You'll be connecting the car's x/z translation to the cube's x/z rotation. A demo of this behavior using the connectAttr() function can be found on p.42 of your book.
      - Save your file as 'control_car.py'
    - Answer the following questions:
      1. Convert the following MEL statements to Python:
          1. polyCylinder -h 3 -r 1 -sc 2 -ch 1;
          1. polySphere -r 3 -sx 8 -sy 8 -ch 1;
          1. polyTorus -r 1 -sr 0.5 -tw 5 -sx 20 -sy 20 -ch 1;
          1. polyCube -w 9 -h 9 -d 9 -sx 3 -sy 3 -sz 3 -ch 1;
      1. For the following list: my_list = [2, 3, 7, 8, 9]
          1. What is the value of my_list[1]?
          1. What is the value of my_list[-1]?
          1. What is the value of my_list[:-1]?
          1. What is the value of my_list[::-1]?
          1. What is the value of my_list[1:-1]?
      1. Reformat the print statement to use % string formatting:
          a = 5
          b = 3
          c = pow(a, b)

          print(str(a) + “ to the “ + str(b) + “ power is “ + str(c))

1. Week 4
    1. Finish reading Chapter 3

    1. Write a function called name_objects that takes a string as an argument to name Maya objects as they are being created.

    1. Write a function called rename_obj that takes a string as an argument to rename a selected Maya object.
  	-(Hint: use  m_sel = maya.cmds.ls(selection=True)   to assign the selected object to a variable.

    1. Explain what a for loop is, and write a function that uses it to print the name of each object in a list.

    1. Explain what the range command does, and write a function that uses it to print the numbers 0 through 9.

    1. Write a function called print_parents that takes a list of Maya objects as an arguments and prints each node and its parent node.
      (Hint: use listRelatives command.)
          1. Create four objects in the scene.  Cube, Sphere, Cylinder, Torus.
          1. Parent Torus under Cylinder. Then parent Cylinder under Sphere. Then parent Sphere under Cube.
          1. Use this example hierarchy for the objects required for the print_parent function.

1. Week 5
    1. Finish reading through Chapter 3
    1. Do all homework not already submitted.
    1. Mid-term in-class exercise next week. Open book, open internet, no collaboration. You will be given questions to answer and a programming task.


    1. Note: If you are having trouble, remember everything you can do in Maya you can do in Maya with Python. Think about the way you might do the task without python. Everything that exists in Maya can be listed and edited using the right Python commands. Search the internet and/or use the Maya Python documentation to find the python function that does what you want to do: http://help.autodesk.com/cloudhelp/2016/ENU/Maya-Tech-Docs/CommandsPython/index.html
    This documentation is linked on the main class github as well.

1. Week 6
    Answer the following questions
    1. What is a Module and what is it used for?
    1. When does the code in an imported Module run?
    1. What is the difference between a package and a Module?
    1. Define 'userSetup Scripts' and 'sitecustomize Module' and describe when they would be used.
    1. What is 'Pillow' and how would you import it? (consult google for help)

1. Week 8
    1. Read Ch. 4 to page 127, Read Ch. 5 to page 168
    1. Finish all assignments not turned in
    1. Work on final project

1. Week 9
    1. Run "spike.py" on your asset for the final project and screenshot the result
    1. Finish all assignments not turned in
    1. Work on final Project -->
