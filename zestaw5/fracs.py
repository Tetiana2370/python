from fractions import gcd as gcd

def add_frac(frac1, frac2):
	if(frac1[1] != frac2[1]):
		denom = frac1[1] * frac2[1]
		result = [frac1[0]*frac2[1] + frac2[0]*frac1[1], denom]
		comdiv = gcd(result[0], result[1])
		if(comdiv > 1):
			result[0] /= comdiv
			result[1] /= gomdiv
	return result
def sub_frac(frac1, frac2):
	if(frac1[1] != frac2[1]):
		denom = frac1[1] * frac2[1]
		result = [abs(frac1[0]*frac2[1]) - abs(frac2[0]*frac1[1]), denom]
		comdiv = gcd(result[0], result[1])
		if(comdiv > 1):
			result[0] /= comdiv
			result[1] /= comdiv
	return result

def mul_frac(frac1, frac2):
	result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
	comdiv = gcd(result[0], result[1])
	if(comdiv > 1):
		result[0] /= comdiv
		result[1] /= comdiv
	return result

def div_frac(frac1, frac2):
	result = [frac1[0]*frac2[1], frac1[1] * frac2[0]]
	comdiv = gcd(result[0], result[1])
	if(comdiv > 1):
		result[0] /= comdiv
		result[1] /= comdiv
	return result

def is_positive(frac):
	if(frac[0] / frac[1] >= 0):
		return True
	return False

def is_zero(frac):
	if(frac[0] == 0):
		return True
	return False

def cmp_frac(frac1, frac2): 
	a, b = float(frac1[0]) / frac1[1], float(frac2[0]) / frac2[1]
	if(a == b):
		return 0
	if(a < b):
		return -1
	else:
		return 1

def frac2float(frac): 
	return float(frac[0])/frac[1]

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznacznosc)
f5 = [0, 2]                   # zero (niejednoznacznosc)

import unittest
import sys

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
		self.assertEqual(sub_frac([1, 2], [2, 3]), [-1, 6])

    def test_mul_frac(self): 
		self.assertEqual(mul_frac([2, 3], [1, 2]), [1, 3])

    def test_div_frac(self): 
		self.assertEqual(div_frac([2, 3], [1, 2]), [4, 3])

    def test_is_positive(self): 
		self.assertEqual(is_positive([-2, 3]), False)
		self.assertEqual(is_positive([2, -3]), False)
		self.assertEqual(is_positive([2, 3]), True)
		self.assertEqual(is_positive([-2, -3]), True)
		

    def test_is_zero(self): 
		self.assertEqual(is_zero([0, 2]), True)
		self.assertEqual(is_zero([2,2]), False)
		
    def test_cmp_frac(self):
		self.assertEqual(cmp_frac([1,2], [2, 3]), -1 )
		self.assertEqual(cmp_frac([2, 3], [1,2]), 1 )
		self.assertEqual(cmp_frac([4, 6], [2, 3]), 0 )

    def test_frac2float(self): 
		self.assertEqual(frac2float([1, 2]), 0.5)
		self.assertEqual(frac2float([1, 3]), 1.0/3)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

	
