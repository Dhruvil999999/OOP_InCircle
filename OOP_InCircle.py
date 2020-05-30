# -*- coding: utf-8 -*-
"""
OOP_InCircle.py

Automatically generated by Colaboratory.

# **Inheritance**
"""

class Prerequistes():

  def __init__(self,radius):
    self.radius = radius

  def incircle_radius(self,a,b,c):
    s = (a + b + c) / 2
    x = s * (s - a) * (s - b) * (s - c)
    tri_area = x**0.5
    incircle_radius = tri_area / s    
    self.radius = incircle_radius
    print(f'Incricle radius :  {incircle_radius} unit')

    

class InCircle(Prerequistes):
  pi = 22/7

  def __init__(self):
    pass

  def area(self):
    Prerequistes.incircle_radius(self,int(input('side a :  ')),int(input('side b :  ')),int(input('side c :  ')))
    return (self.radius ** 2) * self.pi

  def circumference(self):
    Prerequistes.incircle_radius(self,int(input('side a :  ')),int(input('side b :  ')),int(input('side c :  ')))
    return 2 * self.pi * self.radius

  def area_sector(self,theta): #theta in degrees
    Prerequistes.incircle_radius(self,int(input('side a :  ')),int(input('side b :  ')),int(input('side c :  ')))
    return (theta * self.pi * (self.radius ** 2)) / 360

  def arc_length(self,theta): #theta in degrees
    Prerequistes.incircle_radius(self,int(input('side a :  ')),int(input('side b :  ')),int(input('side c :  ')))
    return (theta * 2 * self.pi * self.radius) / 360

  def area_sector_rad(self,theta): #theta in radians
    Prerequistes.incircle_radius(self,int(input('side a :  ')),int(input('side b :  ')),int(input('side c :  ')))
    return (theta * (self.radius ** 2)) / 2

  def arc_length_rad(self,theta): #theta in radians
    Prerequistes.incircle_radius(self,int(input('side a :  ')),int(input('side b :  ')),int(input('side c :  ')))
    return (theta * self.radius)


  
# Example  
k = InCircle()
k.incircle_radius(3,4,5)
