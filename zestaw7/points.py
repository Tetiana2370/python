#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class Point:
	"""Klasa reprezentująca punkty na płaszczyźnie."""
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)
		
	def __str__(self):               # zwraca string "(x, y)"
		return str("(%.2f, %.2f)" % (self.x, self.y))

	def __repr__(self):        # zwraca string "Point(x, y)"
		return str("Point(%.2f, %.2f)" % (self.x, self.y))
	
	def __eq__(self, other): # obsługa point1 == point2
		if str(self) == str(other):
			return True;
		elif isinstance(other, Point):
			if(self.x == other.x):
				return self.y == self.x
		return False

	def __ne__(self, other):        # obsługa point1 != point2
		return not self == other
	
	# Punkty jako wektory 2D.
	def __add__(self, other):        # v1 + v2
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):        # v1 - v2
		return Point(self.x - other.x, self.y - other.y)

	def __mul__(self, other):  # v1 * v2, iloczyn skalarny
		return self.x * self.y + other.x * other.y

	def cross(self, other):       # v1 x v2, iloczyn wektorowy 2D   ?
		return (0, 0, self.x*other.y - self.y * other.x)

	def length(self):         # długość wektora
		return math.sqrt(self.x**2 + self.y**2)


# Kod testujący moduł.

import unittest

point = Point(2, 3)

class TestPoint(unittest.TestCase): 
	
	def test__init__(self):
		self.assertEqual(point.__str__ (), "(2.00, 3.00)" )
	
	def test__repr__(self):
		self.assertEqual(point.__repr__ (), "Point(2.00, 3.00)" )
	
	def test__eq__(self):
		self.assertEqual(point == Point(2, 3), True )
		self.assertEqual(point  == Point(4, 4), False )

	def test__ne__(self):
		self.assertEqual(point.__ne__ (Point(2, 3)), False )
		self.assertEqual(point.__ne__ (Point(4, 4)), True )
	
	def test__add__(self):
		self.assertEqual(point + Point(2, 3), Point(4, 6) )
		self.assertEqual(point + Point(1, 1), Point(3, 4) )
			
	def test__sub__(self):
		self.assertEqual(point - Point(2, 3), Point(0, 0) )
		self.assertEqual(point - Point(1, 1), Point(1, 2) )
	
	def test__mul__(self):
		self.assertEqual(point * Point(1, 2), 8 )
		self.assertEqual(point * Point(4, 5), 26 )
	
	def test_length(self):
		self.assertEqual(point.length(), math.sqrt(13) )
		self.assertEqual(Point(3, 4).length(), 5)
	def test_cross(self):
		self.assertEqual(point.cross(Point(3, 4)), (0, 0, -1))
		self.assertEqual(Point(2,5).cross(Point(4, 7)), (0, 0, -6))
	
	
if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy

	
