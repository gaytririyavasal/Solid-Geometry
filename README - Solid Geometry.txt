
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

This assignment is on object-oriented programming. You will be developing several classes that are fundamental in Solid Geometry - Point, Sphere, Cube, and Cylinder. In main(), you will test the various functions that you have written for the classes.

Note that in this program, you will be checking for the equality of two floating point numbers. Since there is a finite precision in the representation of floating point numbers, it is not always possible to determine exact equality. A working solution is to determine equality is to take the difference of the floating point numbers and see if the difference is less than a pre-determined tolerance. This tolerance is arbitrary and is often dictated by the problem that you are trying to solve. Here is a function that tests for the equality of two floating point numbers.

def is_equal (a, b):
  tol = 1.0e-6
  return (abs (x - y) < tol)

Input: 

You will be reading your input from standard input in the following format geometry.in:

-3.0 2.0 1.0                       # coordinates of p
2.0 -1.0 3.0                       # coordinates of q
2.0 1.0 3.0 4.0                    # center and radius of sphereA
-1.0 -2.0 -3.0 5.0                 # center and radius of sphereB
2.0 1.0 -3.0 4.0                   # center and side of cubeA
3.0 2.0 -4.0 3.0                   # center and side of cubeB
-2.0 1.0 -3.0 5.0 4.0              # center, radius, and height of cylA
1.0 5.0 3.0 4.0 2.0                # center, radius, and height of cylB

Output: 

You will print your output to standard out in the following format geometry.out:

Distance of Point p from the origin (is / is not) greater than the distance of Point q from the origin

Point p (is / is not) inside sphereA
sphereB (is / is not) inside sphereA
cubeA (is / is not) inside sphereA
cylA (is / is not) inside sphereA
sphereA (does / does not) intersect sphereB
cubeB (does / does not) intersect sphereB
Volume of the largest Cube that is circumscribed by sphereA (is / is not) greater than the volume of cylA

Point p (is / is not ) inside cubeA
sphereA (is / is not) inside cubeA
cubeB (is / is not) inside cubeA
cylA (is / is not) inside cubeA
cubeA (does / does not) intersect cubeB
Intersection volume of cubeA and cubeB (is / is not) greater than the volume of sphereA
Surface area of the largest Sphere object inscribed by cubeA (is / is not) greater than the surface area of cylA

Point p (is / is not) inside cylA
sphereA (is / is not) inside cylA
cubeA (is / is not) inside cylA
cylB (is / is not) inside cylA
cylB (does / does not) intersect cylA
