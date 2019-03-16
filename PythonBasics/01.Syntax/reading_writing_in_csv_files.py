# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:21:17 2019

@author: sa6o6
"""
#resource used: https://realpython.com/python-csv/

import numpy as np

words = np.array(['word1', 'word2', 'word3']);
print(' | '.join(words)) #concatenate elements of an array with delimiter

oneWord = 'Hello!'
print(f'Inserting variables: {oneWord}') #allows a bit of code into the curly brackets

import csv

filePath = 'C:/AleksandarUser/Programming/GitHubRepositories/TU-Data-Mining/Data/data.csv'
with open(filePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'Record {line_count}:')
            print(f'\tLoan amount: {row[0]}')
            print(f'\tLoan period in months: {row[1]}')
            
            goodClient = ''
            if (row[2] == 0):
                goodClient = 'No'
            else:
                goodClient = 'Yes'
                
            print(f'\tGood client: {goodClient}')
            print(f'\tClient score: {row[3]}')
            line_count += 1
            if (line_count > 10):
                break
            
clear()

# =============================================================================
# Reading the data onto a dictionary
# =============================================================================
with open(filePath, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 1
    for row in csv_reader:
        print(f'Record {line_count}:')
        print(f'\tLoan amount: {row["LoanAmount0"]}')
        print(f'\tLoan period in months: {row["LoanPeriod0"]}')
        
        goodClient = ''
        if (row['Good'] == 0):
            goodClient = 'No'
        else:
            goodClient = 'Yes'
        print(f'\tGood client: {goodClient}')
        print(f'\tClient score: {row["PredictedGood0"]}')
        if (line_count == 10):
            break
        line_count += 1
        
# =============================================================================
# Reading the file via pandas library (the better solution for large files)
# =============================================================================
import pandas
myDataFrame = pandas.read_csv(filePath)
print(myDataFrame) 
#uses the first row values as names for the columns.
#Note: numbers are converted into ints and floats. But if there were dates,
#then it wouldn't be able to make a convert to a date type variable.

print(myDataFrame['LoanAmount0'] [0]) # 2100 - accessing first row loan amount
print(myDataFrame.loc[0]) #prints first row

columnOneSeries = myDataFrame.get('LoanAmount0')
print(columnOneSeries) #prints entire first column
print(columnOneSeries[0]) #prints first column, first element

rowOneSeries = myDataFrame.loc[0] #extracting a row
print(type(rowOneSeries)) #<class 'pandas.core.series.Series'>
print(rowOneSeries['LoanAmount0']) #extracting a value from the row

#df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
#the upper code gives more options. If every customer had a unique id, then I could
#use that id as index_col and extract data about specific customers much easier