#!/usr/bin/env python
# -*- coding: utf-8 -*-
from points import Point

class Triangle:
	"""Klasa reprezentująca trójkąty na płaszczyźnie."""
	
	def __init__(self, x1, y1, x2, y2 = 0, x3 = 0 , y3 = 0):
		
		if isinstance(x1, Point):
			self.pt1, self.pt2, self.pt3 = x1, y1, x2
		else:
			self.pt1 = Point(x1, y1)
			self.pt2 = Point(x2, y2)
			self.pt3 = Point(x3, y3)
		
	def __str__(self):
		"""       [(x1, y1), (x2, y2), (x3, y3)]  """
		return "[{0}, {1}, {2}]".format(self.pt1, self.pt2, self.pt3)

	def __repr__(self):
		"""      Triangle(x1, y1, x2, y2, x3, y3)    """
		return str("Triangle(%.2f, %.2f, %.2f, %.2f, %.2f, %.2f)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y) )

	def __eq__(self, other):
		"""        obsługa tr1 == tr2     """
		
		if not isinstance(other, str):
			tmp_other = [other.pt1, other.pt2, other.pt3]
			tmp_self = [self.pt1, self.pt2, self.pt3]
			for i in tmp_other:
				if not i in tmp_self:
					return False
			return True
		return str(self) == str(other)
	# zakladam że "są równe" oznacza takie same współrzędne, a nie np są takie same
	# ale jeden jest powyżej drugiego

	def __ne__(self, other):
		"""         obsługa tr1 != tr2        """
		return not self == other

	def center(self):
		"""          zwraca środek trójkąta     """
		return Point((self.pt1.x + self.pt2.x + self.pt3.x)/3, (self.pt1.y + self.pt2.y + self.pt3.y)/3)

	def area(self):
		"""          pole powierzchni            """
		AB = self.pt2 - self.pt1
		AC = self.pt3 - self.pt1
		return 1.0 / 2.0 * abs(AB.x * AC.y - AB.y * AC.x)

	def move(self, x, y):
		"""          przesunięcie o (x, y)        """
		self.pt1 += Point(x, y)
		self.pt2 += Point(x, y)
		self.pt3 += Point(x, y)
		

	def make4(self):
		"""     zwraca listę czterech mniejszych   """
	
		new4triangles = list()
		
		pl = [self.pt1, self.pt2, self.pt3]
		
		for i in range(3):
			new4triangles.append(Triangle(pl[i], self.side_center(pl[i], pl[i-1]), self.side_center(pl[i], pl[i-2])))
		new4triangles.append(Triangle(self.side_center(pl[0], pl[1]), self.side_center(pl[0], pl[2]),  self.side_center(pl[1], pl[2])))
		
		return new4triangles
			

	def side_center(self, pt1, pt2):
		return Point((pt1.x + pt2.x)/2, (pt1.y + pt2.y)/2)
		
	

# Kod testujący moduł.

tri1 = Triangle(0, 0, 3, 0, 1.5, 3)
tri2 = Triangle(0, 1, 5, 0, 2, 3)
tri3 = Triangle(0, 0, 3, 0, 1.5, 3)

import unittest

class TestTriangle(unittest.TestCase):
		
	def test__str__(self):
		self.assertEqual(tri1, "[(0.00, 0.00), (3.00, 0.00), (1.50, 3.00)]")
		self.assertEqual(tri2, "[(0.00, 1.00), (5.00, 0.00), (2.00, 3.00)]")
	
	def test__repr__(self):
		self.assertEqual(repr(tri1), "Triangle(0.00, 0.00, 3.00, 0.00, 1.50, 3.00)")
		self.assertEqual(repr(tri2), "Triangle(0.00, 1.00, 5.00, 0.00, 2.00, 3.00)")
	
	def test__eq__(self):
		self.assertEqual(tri1 == tri3, True)
		self.assertEqual(tri1 == tri2, False)
	
	def test__ne__(self):
		self.assertEqual(tri1 != tri3, False)
		self.assertEqual(tri1 != tri2, True)
	
	def test_center(self):
		self.assertEqual(tri1.center(), Point(1.5, 1))
		self.assertEqual(tri2.center(), Point(2.33, 1.33))
		
	def test_area(self):
		self.assertEqual(tri2.area(), 6)
		self.assertEqual(tri1.area(), 4.5)
		
	def test_move(self):
		tmp = Triangle(0, 0, 3, 0, 1.5, 3)
		tmp.move(1, 2)
		self.assertEqual(str(tmp), Triangle(1, 2, 4, 2, 2.5, 5))
		tmp.move(-1, -2)
		self.assertEqual(str(tmp), tri1)
		
	def test_make4(self):
		trlist = [Triangle( 0, 0, 0.75, 1.5, 1.5, 0)]
		trlist.append(Triangle(0.75, 1.5, 1.5, 3, 2.25, 1.5)) 
		trlist.append(Triangle(3, 0, 1.5, 0, 2.25, 1.5)) 
		trlist.append(Triangle(0.75, 1.5, 2.25, 1.5, 1.5, 0)) 
		
		result = tri1.make4()

		for i in result:
			if not i in trlist:
				print ("error in result: %s" % i)
				print ("FAILED: test_make4")
				break;



		trlist2 = [Triangle( 0, 1, 1, 2, 2.5, 0.5)]
		trlist2.append(Triangle(2.5, 0.5, 5, 0, 3.5, 1.5)) 
		trlist2.append(Triangle(1, 2, 3.5, 1.5, 2, 3)) 
		trlist2.append(Triangle(1, 2, 2.5, 0.5, 3.5, 1.5)) 
		
		result2 = tri2.make4()

		for i in result2:
			if not i in trlist2:
				print ("error in result: %s" % i)
				print "FAILED: test_make4"
				break;


			
		
if __name__ == '__main__':
    unittest.main()    


	
