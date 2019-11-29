#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
def heron(a, b, c):
    #
    if(a<=0 or b<=0 or c<=0):
        raise ValueError("all the values have to be positive and non-zero")
   
    if((a+b)<c or (b+c)<a or (a+c)<b):
        raise ValueError("Sum of length of every two sides have to be"+
        " bigger than length of the third side")
      
    p = (a+b+c)/2
    result = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if result<0:
        raise ValueError("wrong value")
    print(result) 
    return result
        

heron(3,5,4)
heron(3,3,2)
# heron(3, 0, 5)
# heron(3, 2, 7)
