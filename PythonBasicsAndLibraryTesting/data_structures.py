# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 23:26:09 2019

@author: sa6o6
"""

myList = [[1, 2, 3], ['what', 'no', 'who'], True]

print(myList)

print(myList[1])

myList.append(False)
myList.insert(1, 'Hehe')

print(myList)
if (myList.__contains__('Hehe')) :
    print('Hehe found!') #this is executed
    print('Found, but kinda useless') #this is also executed

#==================================================================
#tuple: array of constants. No more constants can be added,
# and the already added constants can't be chnaged. Is fast
myTuple = 'Aleksandar', 'Boev' 
print(myTuple[0])

myTuple[0] = 'Gosho' #Error
myTuple.append('Gosho') #Error

if (myTuple.__contains__('Tosho')):
    print('Tosho found!')
else:
    print('Tosho NOT found!') #this is the result
    
#=================================================================
#Dictionary
myDictionary = {'Sofia': 10000,
                'Varna': 8000,
                'Plovdiv': 9000,
                10: 'Big'}

print(myDictionary)

print(myDictionary['Sofia']) #access element
print(myDictionary[10])

myDictionary['Sofia'] = 12000 #change element

del myDictionary['Varna'] #remove element
myDictionary['Turnovo'] = 7500; #add new element
print(myDictionary)

# =============================================================================
#Set - unordered unique values
mySet = set([1, 2, 3, 4, 1, 2, 3])
print(mySet) #prints unique values. 

if (4 in mySet): #better than .__contains__ (i think)
    print('Yes, it contains "4"') 
    
mySubSet = set([2, 3])

if (mySubSet.issubset(mySet)): #or use mySet.issuperset(mySubSet)
    print('Yes, it is a subset')
    
mySet.add('wat')
print(mySet)

anotherSet = set([0.5, 'Hello, Set'])

mySet.update(anotherSet) #adds everything from 'anotherSet'
print(mySet)

mySet.discard(1) 
#difference between discard and remove: 
#when removing, if there is no such value, there is an error
#when discarding, there is no error if no value matches
print(mySet)

print(len(mySet)) #length of set
# =============================================================================

