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
print(type(y1))

#========================IO 1 PURVATA==========================================
v1 = m.Var()
v2 = m.Var()

m.Equation( (v1 - 2)**2 + (v2 - 1)**2 - 6 <= 0 )
m.Equation( v2 - 2*v1 + 2 == 0 )
m.Equation( v2 >= 0 )

m.Obj( (v1 + 1)**2 + (v2 - 2)**2 )
m.solve(disp=False)
print(v1.value)
print(v2.value)

#=======================IO 1 druga zadachka====================================
z1 = m.Var()
z2 = m.Var()

m.Equation( (z1 - 1)**2 + (z2 - 1)**2 - 9 <= 0 )
m.Equation( z2 - 2*z1 + 2 == 0 )
m.Equation( z2 >= 0 )

m.Obj( (z1 + 1)**2 + (z2 + 2)**2 )
m.solve(disp=False)
print(z1.value)
print(z2.value)


#===================Optimizing client with id 100004===========================
#CustomerId        100032.00000
#LoanAmount0         4000.00000
#LoanPeriod0           10.00000
#Good                   0.00000
#PredictedGood0      -322.00000
#ClientScore          168.56683

#Formulas:
#f(x) = a*((x(1) - LoanAmount0)/LoanAmount0)^2 + (1 - a)*((x(2) - LoanPeriod0)/LoanPeriod0)^2
#x(1) >= 200
#x(1) <= 260000
#x(2) >= 2
#x(2) <= 60
n.clear()
n = GEKKO()

LoanAmount0 = 4000.0
LoanPeriod0 = 10.0
a = 0.9

s1 = n.Var(0, 200.0, 260000.0) #LoanAmount0
s2 = n.Var(0, 2, 60) #LoanPeriod0

#n.Equation(s1 >= 200.0)
#n.Equation(s1 <= 260000.0)
#
#n.Equation(s2 >= 2.0)
#n.Equation(s2 <= 60.0)

n.Obj(a*(((s1 - LoanAmount0)/LoanAmount0)**2) + (1 - a)*(((s2 - LoanPeriod0)/LoanPeriod0)**2))
#n.Obj(((s1 - LoanAmount0)/LoanAmount0)**2 + ((s2 - LoanPeriod0)/LoanPeriod0)**2)

n.solve(disp=False)
print(s1.value)
print(s2.value)

print(type(s1))






