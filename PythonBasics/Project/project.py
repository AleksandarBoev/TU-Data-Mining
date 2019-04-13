# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:30:52 2019

@author: sa6o6
"""

#-------------------Extracting data from csv file------------------------------
filePath = 'C:/AleksandarUser/Programming/GitHubRepositories/TU-Data-Mining/Data/data.csv'

import pandas
myDataFrame = pandas.read_csv(filePath)
#print(myDataFrame) 

#==============================================================================
#-----------------------Defining functions-------------------------------------
def pretty_print(row):
    goodCustomer = 'Yes' if row['Good'] == 1 else 'No' #ternary operator
    
    print('%s: %s leva | %s: %s months | %s: %s | %s: %s' % (
          'LoanAmount0', row['LoanAmount0'],
          'LoanPeriod0', row['LoanPeriod0'],
          'Good', goodCustomer,
          'PredictedGood0', row['PredictedGood0']
            ))
    
def filter_bads(row):
   # return row['Good'] #not easy to read and understand
    if (row['Good'] == False):
        return False #bads are filtered out
    else:
        return True #goods stay

def print_dataframe(dataFrame): #prints all data
    for index, row in dataFrame.iterrows() :
        pretty_print(row)
        
def print_dataframe_firstRows(dataFrame, firstRows): #prints number of data
    for index, row in dataFrame.iterrows() :
        pretty_print(row)
        firstRows -= 1
        if (firstRows <= 0):
            break
    
def filter_data_frame_by_good(dataFrame):
    return dataFrame['Good'] == 1

def get_bad_and_good_count(dataFrame, badsCount, goodsCount): #can't change values of parameters
    for index, row in dataFrame.iterrows() :
        if (row['Good'] == False):
            badsCount += 1
        else:
            goodsCount += 1
    
#==============================================================================
#Целта е да се увеличи броят на приеманите кандидати за кредит, без 
#статистически да се влоши съотношението на "лошите" към приеманите кредитополучатели.
#За качеството на популацията от приемани кандидати се използва статистическият 
#показател Bad_Rate = Bads/Accepts.
#--------Separating the good from the bad (the goods should stay)--------------
print_dataframe(myDataFrame)
print_dataframe_firstRows(myDataFrame, 5)

for index, row in myDataFrame.iterrows() :
    if (row['Good'] == False):
        pretty_print(row)
    
goodLoansCount = 0 #count of loans with Good: 1
badLoansCount = 0 #count of loans with Good: 0

for index, row in myDataFrame.iterrows() :
    if (row['Good'] == False):
        badLoansCount += 1
    else:
        goodLoansCount += 1

print('Good loans: %d' % (goodLoansCount))
print('Bad loans: %d' % (badLoansCount))
badRate = badLoansCount / goodLoansCount
print(badRate)

goodClientsDf = myDataFrame[filter_data_frame_by_good(myDataFrame)] #works
print_dataframe_firstRows(goodClientsDf, 10)
#==============================================================================
#--------------------Identifying clients in "gray" area------------------------
#Параметри за оптимизация
#x = [LoanAmount LoanPeriod]' - два параметъра на кредита, чиито оптимални стойности се 
#търсят за всеки отхвърлян кандидат. 
#Кандидатът се приема за отхвърлян, ако PredictedGood(x) = PredictedGood0 + x'*par >= cut-off, 
#където par = [-0.0250382262277766    59.0719735110589]'.
import numpy as np    

x = np.array([myDataFrame.loc[0]['LoanAmount0'], myDataFrame.loc[0]['LoanPeriod0']])
par = np.array([-0.0250382262277766, 59.0719735110589])
result = x * par #multiplies 1st elements of each array and then the 2nd element of each array
print(result)

cutOff = 684.0

isAcceptable = (result[0] < cutOff) & (result[1] < cutOff)
print(isAcceptable)
#TODO filter out the accepted people and leave the ones who are not
def filter_accepted_people(row, parValues, cutOff): #TODO how to make a proper filter
    values = np.array([row['LoanAmount0'], row['LoanPeriod0']]) #buggy code. Fix!!!!
    calculation = values * parValues
    isAcceptable = (calculation[0] < cutOff) and (calculation[1] < cutOff)
    return not isAcceptable

filteredDf = myDataFrame[filter_accepted_people(myDataFrame, par, cutOff)]
print_dataframe_firstRows(filteredDf, 10)

# copy paste this into the console on the right runfile('C:/AleksandarUser/Programming/GitHubRepositories/TU-Data-Mining/PythonBasics/Project/project_library.py', wdir='C:/AleksandarUser/Programming/GitHubRepositories/TU-Data-Mining/PythonBasics/Project')
import project_library as pl #the fix: needed to run the file [F5]. Not debug it [Ctrl] + [F5]
pl.print_greeting()

