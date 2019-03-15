# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:51:33 2019

@author: sa6o6
"""

intNumber = 4
print(intNumber) #prints int

floatNumber = 5.0
print(type(floatNumber)) #prints float

floatIsBigger = floatNumber > intNumber
print(floatIsBigger) #True
print(type(floatIsBigger)) #bool

someString = 'Hello, Python'
print(someString)

print(someString.upper())

print('%s has reached %s' % ('The ship', 'the moons serfice'))
greeting = 'Hello, %s!' % ('Python')
print(greeting)

import numpy as np

vector = np.array([1, 2, 3, 'aaaa'])
print(vector)

vector = np.append(vector, 4.5) #adds it to the back of the array
print(vector)

#result is 23, because one element is a string and
# so all elements become strings
print(vector[1] + vector[2]) 

vector = np.insert(vector, 0, 99) #new first element
print(vector)

print(np.size(vector)) #size of the vector

print(len(vector)) #size of the vector again

intNum2 = 5
floatNum2 = float(intNum2) #casting
print(type(floatNum2)) #prints float

matrix = np.array([
                  [1, 2, 3], 
                  [4, 5, 6],
                  [7, 8, 'a'] #one string turns all the elemnts into strings
                  ])

print(matrix) #just a vector with elements, which are arrays
#Note: if one of the arrays was a different size than the others
#the printing looks different (infront of every array there is the word 'list')

print(matrix[0, 1] + matrix[1, 2]) #26, string concatenation

print(matrix[0]) #print the entire first row

print(matrix[0 : 2]) #prints row 0 and 1 => exclusive indexes given
print(matrix[1, :]) #prints everything from row 1

print(matrix[2][1 : 3]) #prints from row 2: '8' and 'a'

print(matrix[1][1:]) #prints from row 1 every element AFTER element 1
print(matrix[1][:1]) #prints from row 1 every element BEFORE element 1

print(matrix[:, 0]) #prints everything from column 0 ('1', '4', '7')

clear() #clear the righ side

m1 = np.array([
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
        ])

m2 = np.array([
        [10, 10, 10],
        [20, 20, 20],
        [30, 30, 30]
        ])

m3 = np.append(m1, m2, axis=0)

print(m3)
#Result:
#[[ 1  1  1]
# [ 2  2  2]
# [ 3  3  3]
# [10 10 10]
# [20 20 20]
# [30 30 30]]

m3 = np.append(m1, m2, axis=1)

print(m3)
#Result:
#[[ 1  1  1 10 10 10]
# [ 2  2  2 20 20 20]
# [ 3  3  3 30 30 30]]



