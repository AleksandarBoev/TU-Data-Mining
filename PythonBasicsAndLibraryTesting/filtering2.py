# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:07:12 2019

@author: sa6o6
"""

#Параметри за оптимизация
#x = [LoanAmount LoanPeriod]' - два параметъра на кредита, чиито оптимални стойности се 
#търсят за всеки отхвърлян кандидат. 
#Кандидатът се приема за отхвърлян, ако PredictedGood(x) = PredictedGood0 + x'*par >= cut-off, 
#където par = [-0.0250382262277766    59.0719735110589]'.
import numpy as np    

x = np.array([1.0, 2.0])
par = np.array([-0.0250382262277766, 59.0719735110589])
result = x * par #multiplies 1st elements of each array and then the 2nd element of each array
print(result)

result2 = 1 + result #adds 1 to each array element
print(result2)

booleanArray = result2 >= 0.5
print(booleanArray)

if (booleanArray.all()): #all elements should be true
    print('Yes!')
else:
    print('No')
    
booleanArray[0] = False

if (booleanArray.all()):
    print('Yes!')
else:
    print('No!')
	
if (booleanArray.any()): #at least one element should be true
    print('Yes!')
else:
    print('No')