# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:29:46 2019

@author: sa6o6
"""
#https://youtu.be/onMqBj-IgR0?t=341 --> tutorial for GEKKO library

#!pip install gekko --> this is how an external library is installed
from gekko import GEKKO    
import numpy as np

#https://youtu.be/UD0ac9pKopk?t=895
m = GEKKO()
x1 = m.Var(value = 0)
x2 = m.Var(value = 0)

m.Equation(x1**2 + x2**2 <= 4)
m.Equation(x1 - x2 <= 0)
m.Obj(2*x1 + x2)
m.solve(disp=False)
print(x1.value)
print(x2.value)

x1Result = -4 / np.sqrt(5)
print(x1Result)

x2Result = -2 / np.sqrt(5)
print(x2Result)

#==============================================================================
#https://youtu.be/UD0ac9pKopk?t=1533
y1 = m.Var(value = 0)
y2 = m.Var(value = 0)

m.Equation(y1**2 + y2 - 1 <= 0)

m.Obj(y1**2 + y2**2 - 2*y1)
m.solve(disp=False)
print(y1.value)
print(y2.value)