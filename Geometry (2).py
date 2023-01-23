#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  File: Geometry.py

#  Description: The following program implements 4 different classes, including Point, Sphere, Cube and Cylinder.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/5/22

#  Date Last Modified: 2/7/22

import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = float(x)
      self.y = float(y)
      self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      tol = 1.0e-6
      return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol)

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
      self.center = Point(x, y, z)
      self.radius = float(radius)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
      return "Center: (" + str(self.center.x) + ", " + str(self.center.y) + ", " + str(self.center.z) + "), Radius: " + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
      return 4 * math.pi * (self.radius ** 2)

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
      return (4/3) * math.pi * (self.radius ** 3)

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return self.center.distance(p) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      return self.center.distance(other.center) < abs(self.radius - other.radius)

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      return self.center.distance(a_cube.center) < abs(self.radius - (a_cube.diagonal/2))

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
      distance_x_y = math.hypot(self.center.x - a_cyl.center.x, self.center.y - a_cyl.center.y)
      distance_z = abs(self.center.z - a_cyl.center.z)
      return (distance_x_y < abs(self.radius - a_cyl.radius)) and (distance_z < abs(self.radius - a_cyl.height/2))

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
      flag = True
      if self.radius + other.radius < self.center.distance(other.center):
          flag = False
         
      return (not self.is_inside_sphere(other) and flag)

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
      flag = True
      if self.radius + a_cube.diagonal/2 < self.center.distance(a_cube.center):
          flag = False
    
      return (not self.is_inside_cube(a_cube) and flag)

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
      cube_side = self.radius * 2 / math.sqrt(3)
      cube = Cube(self.center.x, self.center.y, self.center.z, cube_side)
      return cube

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      self.center = Point(x, y, z)
      self.side = float(side)
      self.diagonal = math.sqrt(3) * float(side)

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
      return "Center: (" + str(self.center.x) + ", " + str(self.center.y) + ", " + str(self.center.z) + "), Side: " + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
      return 6*(self.side ** 2)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
      return (self.side ** 3)

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
      return (abs(self.center.x - p.x) < self.side/2) and (abs(self.center.y - p.y) < self.side/2) and (abs(self.center.z - p.z) < self.side/2)

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      return self.center.distance(a_sphere.center) < (self.side/2 - a_sphere.radius)

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      return self.center.distance(other.center) < abs(self.side/2 - other.side/2)

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
      distance_x_y = math.hypot(self.center.x - a_cyl.center.x, self.center.y - a_cyl.center.y)
      distance_z = (self.center.z - a_cyl.center.z)
      return (distance_x_y < (self.side/2 - a_cyl.radius)) and (distance_z < (self.side/2 - a_cyl.height/2))

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
      flag = True
      if self.side/2 + other.side/2 < self.center.distance(other.center):
          flag = False
          
      return not self.is_inside_cube(other) and flag

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
      length_x = abs(abs(self.center.x - other.center.x) - (self.side/2) - (other.side/2))
      length_y = abs(abs(self.center.y - other.center.y) - (self.side/2) - (other.side/2))
      length_z = abs(abs(self.center.z - other.center.z) - (self.side/2) - (other.side/2))
      return length_x * length_y * length_z
      
      
      
  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
      radius = self.side / 2
      sphere = Sphere(self.center.x, self.center.y, self.center.z, radius)
      return sphere

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.center = Point(x, y, z)
      self.radius = float(radius)
      self.height = float(height)

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      return "Center: (" + str(self.center.x) + ", " + str(self.center.y) + ", " + str(self.center.z) + "), Radius: " + str(self.radius) + ", Height: " + str(self.height)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      return (2 * math.pi * self.radius) * (self.height + self.radius)

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      return math.pi * self.height * (self.radius ** 2)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return (math.hypot(self.center.x - p.x, self.center.y - p.y) < self.radius) and (abs(self.center.z - p.z) < self.height/2)
      

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      distance_x_y = math.hypot(self.center.x - a_sphere.center.x, self.center.y - a_sphere.center.y)
      distance_z = abs(self.center.z - a_sphere.center.z)
      return distance_x_y < (self.radius - a_sphere.radius) and distance_z < (self.height/2 - a_sphere.radius)

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      distance_x_y = math.hypot(self.center.x - a_cube.center.x, self.center.y - a_cube.center.y)
      distance_z = abs(self.center.z - a_cube.center.z)
      return distance_x_y < (self.radius - a_cube.side/2) and distance_z < (self.height/2 - a_cube.side/2)

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
      distance_x_y = math.hypot(self.center.x - other.center.x, self.center.y - other.center.y)
      distance_z = abs(self.center.z - other.center.z)
      return distance_x_y < abs(self.radius - other.radius) and distance_z < abs(self.height/2 - other.height/2)

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
      distance_x_y = math.hypot(self.center.x - other.center.x, self.center.y - other.center.y)
      distance_z = abs(self.center.z - other.center.z)
      flag = True
      if (self.radius + other.radius < distance_x_y) or (self.height/2 + other.height/2 < distance_z):
          flag = False
      
      return not self.is_inside_cylinder(other) and flag

def main():
  # read data from standard input
  import sys

  # read the coordinates of the first Point p
  p = (sys.stdin.readline().split())
  xcoordinate = p[0]
  ycoordinate = p[1]
  zcoordinate = p[2]

  # create a Point object 
  p = Point (xcoordinate, ycoordinate, zcoordinate)

  # read the coordinates of the second Point q
  q = (sys.stdin.readline().split())
  xcoordinate = q[0]
  ycoordinate = q[1]
  zcoordinate = q[2]

  # create a Point object
  q = Point (xcoordinate, ycoordinate, zcoordinate)

  # read the coordinates of the center and radius of sphereA
  sphereA = (sys.stdin.readline().split())
  xcoordinate = sphereA[0]
  ycoordinate = sphereA[1]
  zcoordinate = sphereA[2]
  radius = sphereA[3]

  # create a Sphere object
  sphereA = Sphere (xcoordinate, ycoordinate, zcoordinate, radius)

  # read the coordinates of the center and radius of sphereB
  sphereB = (sys.stdin.readline().split())
  xcoordinate = sphereB[0]
  ycoordinate = sphereB[1]
  zcoordinate = sphereB[2]
  radius = sphereB[3]

  # create a Sphere object
  sphereB = Sphere (xcoordinate, ycoordinate, zcoordinate, radius)

  # read the coordinates of the center and side of cubeA
  cubeA = (sys.stdin.readline().split())
  xcoordinate = cubeA[0]
  ycoordinate = cubeA[1]
  zcoordinate = cubeA[2]
  side = cubeA[3]

  # create a Cube object
  cubeA = Cube (xcoordinate, ycoordinate, zcoordinate, side)

  # read the coordinates of the center and side of cubeB
  cubeB = (sys.stdin.readline().split())
  xcoordinate = cubeB[0]
  ycoordinate = cubeB[1]
  zcoordinate = cubeB[2]
  side = cubeB[3]

  # create a Cube object
  cubeB = Cube (xcoordinate, ycoordinate, zcoordinate, side)

  # read the coordinates of the center, radius and height of cylA
  cylA = (sys.stdin.readline().split())
  xcoordinate = cylA[0]
  ycoordinate = cylA[1]
  zcoordinate = cylA[2]
  radius = cylA[3]
  height = cylA[4]

  # create a Cylinder object
  cylA = Cylinder (xcoordinate, ycoordinate, zcoordinate, radius, height)

  # read the coordinates of the center, radius and height of cylB
  cylB = (sys.stdin.readline().split())
  xcoordinate = cylB[0]
  ycoordinate = cylB[1]
  zcoordinate = cylB[2]
  radius = cylB[3]
  height = cylB[4]

  # create a Cylinder object
  cylB = Cylinder (xcoordinate, ycoordinate, zcoordinate, radius, height)

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  originpoint = Point (0, 0, 0)

  if (p.distance (originpoint) > q.distance (originpoint)):
        print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
  else:
        print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

  # print if Point p is inside sphereA
  if (sphereA.is_inside_point(p)):
        print("Point p is inside sphereA")
  else:
        print("Point p is not inside sphereA")

  # print if sphereB is inside sphereA
  if (sphereA.is_inside_sphere(sphereB)):
        print("sphereB is inside sphereA")
  else:
        print("sphereB is not inside sphereA")

  # print if cubeA is inside sphereA
  if (sphereA.is_inside_cube(cubeA)):
        print("cubeA is inside sphereA")
  else:
        print("cubeA is not inside sphereA")

  # print if cylA is inside sphereA
  if (sphereA.is_inside_cyl(cylA)):
        print("cylA is inside sphereA")
  else:
        print("cylA is not inside sphereA")

  # print if sphereA intersects with sphereB
  if (sphereA.does_intersect_sphere(sphereB)):
        print("sphereA does intersect sphereB")
  else:
        print("sphereA does not intersect sphereB")

  # print if cubeB intersects with sphereB
  if (sphereB.does_intersect_cube(cubeB)):
        print("cubeB does intersect sphereB")
  else:
        print("cubeB does not intersect sphereB")

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  largestcirumscribedcube = sphereA.circumscribe_cube()
  if (cylA.volume() < largestcirumscribedcube.volume()):
        print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
  else:
        print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

  # print if Point p is inside cubeA
  if (cubeA.is_inside_point(p)):
        print("Point p is inside cubeA")
  else:
        print("Point p is not inside cubeA")
        
  # print if sphereA is inside cubeA
  if (cubeA.is_inside_sphere(sphereA)):
        print("sphereA is inside cubeA")
  else:
        print("sphereA is not inside cubeA")

  # print if cubeB is inside cubeA
  if (cubeA.is_inside_cube(cubeB)):
        print("cubeB is inside cubeA")
  else:
        print("cubeB is not inside cubeA")

  # print if cylA is inside cubeA
  if (cubeA.is_inside_cylinder(cylA)):
        print("cylA is inside cubeA")
  else:
        print("cylA is not inside cubeA")

  # print if cubeA intersects with cubeB
  if (cubeA.does_intersect_cube(cubeB)):
        print("cubeA does intersect cubeB")
  else:
        print("cubeA does not intersect cubeB")

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if (sphereA.volume() < cubeA.intersection_volume(cubeB)):
        print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
  else:
        print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  largestsphereinscribed = cubeA.inscribe_sphere()
  if (cylA.area() < largestsphereinscribed.area()):
        print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
  else:
        print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")

  # print if Point p is inside cylA
  if (cylA.is_inside_point(p)):
        print("Point p is inside cylA")
  else:
        print("Point p is not inside cylA")

  # print if sphereA is inside cylA
  if (cylA.is_inside_sphere(sphereA)):
        print("sphereA is inside cylA")
  else:
        print("sphereA is not inside cylA")

  # print if cubeA is inside cylA
  # print if cubeA is inside cylA
  if (cylA.is_inside_cube(cubeA)):
        print("cubeA is inside cylA")
  else:
        print("cubeA is not inside cylA")

  # print if cylB is inside cylA
  if (cylA.is_inside_cylinder(cylB)):
        print("cylB is inside cylA")
  else:
        print("cylB is not inside cylA")

  # print if cylB intersects with cylA
  if (cylA.does_intersect_cylinder(cylB)):
        print("cylB does intersect cylA")
  else:
        print("cylB does not intersect cylA")

if __name__ == "__main__":
  main()
