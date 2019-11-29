#!/usr/bin/env python
# -*- coding: utf-8 -*-

# zadanie 1 
# Twierdzenie: Równanie diofantyczne ax + by = c ma rozwiązanie 
# wtedy i tylko wtedy, gdy NWD(a, b) jest dzielnikiem liczby c. 

from fractions import gcd as gcd

MAXITER = 100
def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    div = gcd(a, b)
    if(div != 0):
        if(c%div == 0):
            i = 0
            while i <= MAXITER: 
                if(-c - (i * a)) % b == 0: 
                    print("x = " + str(i) + ", y = " + str(int((-c - (i * a)) / b))) 
                    return 0
                i += 1
        else:
            print("suitable values don't exist")
            
            
print("result for 1")
solve1(6,2,0)
print("result for 2")
solve1(5,3,4)


