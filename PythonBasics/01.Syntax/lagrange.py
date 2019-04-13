# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:18:01 2019

@author: sa6o6
"""

import numpy as np

def func(X): 
    x = X[0]
    y = X[1]
    lambd = X[2] # this is the multiplier. lambda is a reserved keyword in python
    return x + y + lambd * (x**2 + y**2 - 1)


def dfunc(X):
    dLambda = np.zeros(len(X))
    h = 1e-3 # this is the step size used in the finite difference. 0.001
    for i in range(len(X)):
        dX = np.zeros(len(X))
        dX[i] = h #step
        
        func1Param = X + dX
        func1Result = func(func1Param)
        
        func2Param = X - dX
        func2Result = func(func2Param)
        
        funcDifference = func1Result - func2Result
        dLambda[i] = (funcDifference/(2*h));
    return dLambda


from scipy.optimize import fsolve

# this is the max
X1 = fsolve(dfunc, [1, 1, 0])
print (X1) 
print(func(X1))

# this is the min
X2 = fsolve(dfunc, [-1, -1, 0])
print(X2) 
print(func(X2))




