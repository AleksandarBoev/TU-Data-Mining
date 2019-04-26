# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 09:56:56 2019

@author: sa6o6
"""
import numpy as np

integerArray = [1, 2, 3, 4, 5, 6, 7, 8]

def filter_odds(num):
    if (num % 2 == 0):
        return False #evens are filtered OUT
    else:
        return True #whatever returns true - stays
        
arrayOfOdds = filter(filter_odds, integerArray) #first way of doing it
for num in arrayOfOdds:
    print(num)
    
arrayOfEvens = filter(lambda x: x % 2 == 0, integerArray) #second way of doing it
for num in arrayOfEvens:
    print(num)
    
