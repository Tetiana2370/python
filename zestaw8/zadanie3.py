#!/usr/bin/env python
# -*- coding: utf-8 -*-

# We simply generate random (x, y) pairs and then check if x^2 + y^2<=1 .
# If yes, we increment the number of points that appears inside the circle. 
# In randomized and simulation algorithms like Monte Carlo, the more the number 
# of iterations, the more accurate the result is. Thus, the title is “Estimating 
# the value of Pi” and not “Calculating the value of Pi”. Below is the algorithm 
# for the method:

# The Algorithm
# 1. Initialize circle_points, square_points and interval to 0.
# 2. Generate random point x.
# 3. Generate random point y.
# 4. Calculate d = x*x + y*y.
# 5. If d <= 1, increment circle_points.
# 6. Increment square_points.
# 7. Increment interval.
# 8. If increment < NO_OF_ITERATIONS, repeat from 2.
# 9. Calculate pi = 4*(circle_points/square_points).
# 10. Terminate.
import random

def calc_pi(n=100):
    points_in_circle = 0
    for iterations in range(0, 1000):
        d = random.random()**2 + random.random()**2
        if d < 1: points_in_circle += 1
        iterations += 1
    print (4.0 * points_in_circle / iterations)

calc_pi()



