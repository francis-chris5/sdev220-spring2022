# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cDryytePIxUIumIKm6E__VMkBiYrebdN

<h3>import modules</h3>
"""

import abc

"""some shape classes, all shapes will have an area method..."""

class Shape(metaclass=abc.ABCMeta):
  def __init__(self):
    pass


  @abc.abstractmethod
  def getArea(self):
    return


  def __eq__(self, other):
    if self.getArea() == other.getArea():
      return True
    else:
      return False

  def __str__(self):
    return f"this shape has an area of {self.getArea()}"

from typing_extensions import SupportsIndex
class Square(Shape):
  def __init__(self, side):
    self.side = side

  def getArea(self):
    return self.side * self.side



class Rectangle():
  def __init__(self, length, width):
    self.length = length
    self.width = width


  def coverage(self):
    return self.length * self.width

cubeFace = Square(4)
longThing = Rectangle(3, 4)

if isinstance(cubeFace, Shape):
  print("I know the area of this...")
  print(cubeFace.getArea())
else:
  print("I have no idea what this is")


if isinstance(longThing, Shape):
  print("I know the area of this...")
  print(str(longThing.getArea()))
else:
  print("I have no idea what this is")

