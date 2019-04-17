# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:19:04 2019

@author: sa6o6
"""
import numpy as np

def pretty_string(row):
    goodCustomer = 'Yes' if row['Good'] == 1 else 'No' #ternary operator
    
    return ('%s: %s | %s: %s leva | %s: %s months | %s: %s | %s: %s' % (
          'Customer id', row['CustomerId'],
          'LoanAmount0', row['LoanAmount0'],
          'LoanPeriod0', row['LoanPeriod0'],
          'Good', goodCustomer,
          'PredictedGood0', row['PredictedGood0']
            ))

def pretty_print(row):   
    print(pretty_string(row))

def pretty_print_dataframe(dataFrame): #prints all data
    for index, row in dataFrame.iterrows() :
        pretty_print(row)
        
def print_dataframe(dataFrame): #prints all data
    for index, row in dataFrame.iterrows() :
        print(row)
        
def print_dataframe_firstRows(dataFrame, firstRows): #prints number of data
    for index, row in dataFrame.iterrows() :
        pretty_print(row)
        firstRows -= 1
        if (firstRows <= 0):
            break
    
def filter_data_frame_by_good(dataFrame):
    return dataFrame['Good'] == 1
            
def get_good_loans_count(dataFrame):
    return len(dataFrame[dataFrame['Good'] == True])

def get_bad_loans_count(dataFrame):
    return len(dataFrame[dataFrame['Good'] == False])

def get_bad_rate(dataFrame):
    return get_bad_loans_count(dataFrame) / get_good_loans_count(dataFrame)

def get_good_clients_data_frame(dataFrame):
    return dataFrame[dataFrame['Good'] == 1]

def get_gray_zone_data_frame(dataFrame, parValues, cutOff):
    resultDf = dataFrame.iloc[0:0]
    
    for index, row in dataFrame.iterrows() :
        values = np.array([row['LoanAmount0'], row['LoanPeriod0']])
        calculation = row['PredictedGood0'] + values * parValues
        isDenied = (calculation[0] >= cutOff) and (calculation[1] >= cutOff)
        if (isDenied):
            resultDf = resultDf.append(row)
    
    return resultDf;
        
    
#def filter_accepted_people(col, parValues, cutOff): #TODO how to make a proper filter
#    values = np.array([col['LoanAmount0'], col['LoanPeriod0']]) #buggy code. Fix!!!!
#    calculation = values * parValues
#    isAcceptable = (calculation[0] < cutOff) and (calculation[1] < cutOff)
#    return not isAcceptable
   
    















                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    