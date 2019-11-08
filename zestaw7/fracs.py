#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import gcd as gcd

class Frac:
	
	def __init__(self, x=0, y=1):

		if(not isinstance(x, (int, float)) or not isinstance(y, int) or y == 0):

			raise ValueError ("ValueError x: %d, y: %d" %(x, y))
		
		else:
			if isinstance(x, float):
				self.x, self.y = float.as_integer_ratio(x)
			else: 
				self.x, self.y = x, y
				
				
	def __str__(self):  		   
		"""  zwraca "x/y" lub "x" dla y=1  """
		
		self = self.simplify()
		if(self.y == 1 or self.y == -1 or self.x == 0):
			return "{0}".format(int(self.x / self.y))
		else:
			return "{0}/{1}".format(self.x, self.y)

	def __repr__(self): 
		"""    zwraca "Frac(x, y)    """
		
		self = self.simplify()
		if(self.y == 1 or self.y == -1 or self.x == 0):
			return "Frac({0})".format(int(self.x / self.y))
		else:
			return "Frac({0}, {1})".format(self.x, self.y)

	def __eq__(self, other):
		return float(self)==float(other)
	
	def __ne__(self, other):
		return not self == other

	def __add__(self, other):
		"""     frac1 + frac2, frac + int   """

		if (type(other) == int):
			return Frac(self.x + self.y * other, self.y)
		if(type(other) == float):
			temp = (other + float(self)).as_integer_ratio()
			result = Frac(temp[0], temp[1])
		else:
			if(self.y != other.y):
				denom = self.y * other.y
				result = Frac( self.x*other.y + other.x*self.y, denom ).simplify()
			else:
				result = Frac(self.x + other.x, self.y)

		return result
		
	
	__radd__ = __add__  

	def __sub__(self, other):
		"""    frac1 - frac2, frac - int    """
		
		if (type(other) == int):
			return Frac(self.x - self.y * other, self.y)
		if(type(other) == float):
			temp = (other - float(self)).as_integer_ratio()
			result = Frac(temp[0], temp[1])
		else:
			if(self.y != other.y):
				denom = self.y * other.y
				result = Frac( self.x*other.y - other.x*self.y, denom ).simplify()
			else:
				result = Frac(self.x - other.x, self.y)
		return result

	def __rsub__(self, other):     
		"""       int - frac       """
		return Frac(self.y * other - self.x, self.y)

	def __mul__(self, other): 
		"""      frac1*frac2, frac*int    """
		
		if(type(other) == int):
			result = Frac(self.x * other, self.y)
		else:
			result = Frac(self.x * other.x, self.y * other.y)
		
		comdiv = gcd(result.x, result.y)
		if(comdiv > 1):
			result.x /= comdiv
			result.y /= comdiv
		return result

	__rmul__ = __mul__              # int*frac

	def __truediv__(self, other): 
		"""      frac1/frac2, frac/int     """
		
		if(type(other) == int):
			result = Frac(self.x, self.y * other)
		else:
			result = Frac(self.x * other.y, self.y * other.x)
		comdiv = gcd(result.x, result.y)
		if(comdiv > 1):
			result.x /= comdiv
			result.y /= comdiv
		return result

	def __rtruediv__(self, other):
		"""      int / frac      """
		
		return ~self * Frac(other)


	def __pos__(self):       
		return self

	def __neg__(self):  
		
		return Frac(self.x * (-1), self.y)

	def __invert__(self):     
		"""         odwrotnosc: ~frac      """
		
		result = Frac(self.y, self.x)
		comdiv = gcd(result.x, result.y)
		if(comdiv > 1):
			result.x /= comdiv
			result.y /= comdiv
		if(result.y < 0):
			result.x *= (-1)  # ??? simplify ?
			result.y *= (-1)
			
		return result;
	

	def __float__(self):
		
		return float(self.x) / self.y
	
	
	def __lt__(self, other):
		"""   x < y   """
		return  float(self) < float(other)
	
	def __gt__(self, other):
		"""   x > y """
		return float(self) > float(other)
	 
	def __le__(self, other):  
		""" x <= y """
		return float(self) <= float(other)
	 
	def __ge__(self, other):  
		""" x >= y """
		return  float(self) >=float(other)

	def simplify(self):
		"""      ex. 2/10 -> 1/5    """
		
		comdiv = gcd(self.x, self.y)
		if(self.x == 0 or comdiv == 0 or comdiv == 1):
			return self
		return Frac(int(self.x / comdiv), int(self.y / comdiv))
		
	
f1 = Frac(1, 5)
f2 = Frac(2, 3)
f3 = Frac(10, 5)
f4 = Frac(0, 5)


import unittest
import sys

class TestFrac(unittest.TestCase):
	def test__str__(self):     
		self.assertEqual(str(f1), "1/5")
		self.assertEqual(str(f2), "2/3")
		self.assertEqual(str(f3), "2")
		self.assertEqual(str(f4), "0")
	
	def test__repr__(self): 
		self.assertEqual(repr(f1), "Frac(1, 5)")
		self.assertEqual(repr(f2), "Frac(2, 3)")
		self.assertEqual(repr(f3), "Frac(2)")
		self.assertEqual(repr(f4), "Frac(0)")

	def test__eq__(self): 
		self.assertEqual(f1== f2 , False)
		self.assertEqual(f2 == (f1), False)
		self.assertEqual(f1 == (Frac(1, 5)), True)
		
	def test__ne__(self):
		self.assertEqual(f1 != f2 , True)
		self.assertEqual(f2 != (f1), True)
		self.assertEqual(f1 != (Frac(1, 5)), False)
		
	def test__add__(self):  
		self.assertEqual(f1 + f2, 13/15)
		self.assertEqual(f2 + f3, 40/15)
		self.assertEqual(f1 + 4 , 21/5)
		self.assertEqual(f1 + 3.25, 3.45)   


	def test__sub__(self):
		self.assertEqual(f1 - f2, -7/15)
		self.assertEqual(f3 - f2, 20/15)
		self.assertEqual(f2 - 3, -7/3)
		#self.assertEqual(f1 - 1.5, -1.3) # funckcja float.as_integer_ratio() nie zawsze daje dobry wynik

	def test__rsub__(self):     
		self.assertEqual(12 - f2, 34/3)

	def test__mul__(self):
		self.assertEqual(f1 * f2, 2/15)
		self.assertEqual(f2 * 3, 2)
		self.assertEqual(f2 * f4, 0)
		
	def test__rmul__(self):
		self.assertEqual(3 * f2, 2)
		self.assertEqual(5 * f2, 10/3)

	def test__truediv__(self):
		self.assertEqual(f1 / f2, 3/10)
		self.assertEqual(f2 / f1, 10/3)

	def test__rtruediv__(self): 
		self.assertEqual(17 / f1, 85)
		self.assertEqual(17 / f2, 51/2)


	def test__pos__(self):
		self.assertEqual(+f1, f1)

	def test__neg__(self):        
		self.assertEqual(-f1, -1/5)

	def test__invert__(self): 
		self.assertEqual(~f1, 5)
		self.assertEqual(~f3, 5/10)
		

	def test__float__(self):
		self.assertEqual(float(f1), 0.2)
		self.assertEqual(float(f4), 0)
		self.assertEqual(float(f2), 2/3)
		
	def test_comparation(self):
		self.assertEqual(f1 < f2, True)
		self.assertEqual(f1 <= f2, True)
		self.assertEqual(f3 <= 3, True)
		self.assertEqual(f3 > 2, False)

if __name__ == '__main__':
    unittest.main()    

	
