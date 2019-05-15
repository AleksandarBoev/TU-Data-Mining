# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:23:44 2019

Code, showing how dataframes work

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
print(df.loc[0])
print(df.loc[0]['Name'])
print(len(df)) #length of dataframe
print(df.columns.values) #array of column names

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

print(len(filteredByAge)) #getting the count

#==============Iterating a data frame:=========================================
for index, row in df.iterrows() :
    print(index)
    calculation = row['Age'] + row['Grade']
    print(calculation)

#=====================Adding a new row=========================================
#This way of adding a new row is costly and inefective if it is done multiple times
#Better solution is to make a list, add to it what is needed and add all it's elements
df2 = df.iloc[0:0] #Result: an empty data frame with same column names
df2 = df2.append(df) #Add all rows from df to df2
df2 = df2.append({'Name': 'Stamat', 'Age' : 20, 'Grade' : 5.89}, ignore_index=True) #Add one row
df2 = df2.append(df.loc[0]) #Add row from other df
df2 = df2.append(df[df['Name'] == 'Pesho']) #Again add row
print(df2)
print(df == df2)

#==Adding all elements from one df to another, which has an additional column==
df3 = pd.DataFrame(data,columns=['Name','Age', 'Grade', 'Calculation'])

for index, row in df.iterrows() :
    calculation = row['Age'] * row['Grade']
    
    df3 = df3.append(row) #SLOW operation! It is slow because a new df is created every .append()
#A faster operation would be appending to a "[]" and after that creating a new df with it's values

df = df.append(data) #broken! Don't use this!


#=============Appending multiple rows==========================================
#   Most optimized way to do it:
#   1) Copy all information from dataframe onto "[]"
#   2) Add new data into the "[]"
#   3) Create new dataframe with the data in "[]" and using the column names from old dataframe

#   Step 1):
resultData = []
for index in range(0, 5): #or from 0 to len(df)
    resultData.append(df.loc[index].values)
    
# Step 2):
resultData.append(['Bai Ivan', 26, 6.0])
resultData.append(['Bai Gosho', 28, 5.75])
#add more data...

# Step 3):
df343 = pd.DataFrame(resultData,columns=df.columns.values)
print(df343)

