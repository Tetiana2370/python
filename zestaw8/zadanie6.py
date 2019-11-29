#!/usr/bin/env python
# -*- coding: utf-8 -*-

# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.

P = {(0,0):0.5, (1,0):0, (0,1):1}

def p(i, j):
    if(i<0 or j<0):
        raise ValueError("negative values")
    if not (i, j) in P:
        if(i>0 and j==0): 
            P[(i, j)]=0
        elif(j>0 and i==0): 
            P[(i, j)]=1
        else:
            P[(i, j)] = 0.5 * (p(i-1, j) + p(i, j-1))
            
    return P[(i, j)]
    
print (p(2,2))
print (p(3,2))
