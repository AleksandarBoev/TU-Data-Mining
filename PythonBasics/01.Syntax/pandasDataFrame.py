# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:23:44 2019

@author: sa6o6
"""
#Learning source: https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm
#Data Frame testing

#import the pandas library and aliasing as pd
import pandas as pd
data = [['Alex',10, 2.0],
        ['Bob',12, 3.0],
        ['Clarke',13, 2.0],
        ['Tosho', 11, 3.0], 
        ['Gosho', 15, 2.0], 
        ['Pesho', 16, 4.0]]
df = pd.DataFrame(data,columns=['Name','Age', 'Grade'])
print(df)

#For filtering, the expression has to look something like this:
# resultingDataFrame = dataFrame[<boolean expression>]
# whatever passes the boolean expression - stays

filteredByAge= df[df['Age'] > 12] #only those who are above 12 remain
print(filteredByAge)

def greater_than(age, limit):
    return age > limit

filteredByAgeViaFunc = df[greater_than(df['Age'], 12)] #same result
print(filteredByAgeViaFunc)

def greater_than_v2(dataFrame, limit):
    return dataFrame['Age'] > limit

filteredByAgeViaFunc2 = df[greater_than_v2(df, 12)]
print(filteredByAgeViaFunc2)

print(len(filteredByAgeViaFunc2.index)) # getting the count of rows of a dataframe