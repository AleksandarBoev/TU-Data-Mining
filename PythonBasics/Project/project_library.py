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
    
def print_dataframe(dataFrame): #prints all data
    for index, row in dataFrame.iterrows() :
        print(row)

def pretty_print_dataframe(dataFrame): #prints all data
    for index, row in dataFrame.iterrows() :
        pretty_print(row)
        
def pretty_print_dataframe_firstRows(dataFrame, firstRows): #prints number of data
    for index, row in dataFrame.iterrows() :
        pretty_print(row)
        firstRows -= 1
        if (firstRows <= 0):
            break
    
def filter_data_frame_by_good(dataFrame):
    return dataFrame['Good'] == 1

def filter_data_frame_by_bad(dataFrame):
    return dataFrame['Good'] == 0
            
def get_good_loans_count(dataFrame):
    return len(dataFrame[dataFrame['Good'] == True])

def get_bad_loans_count(dataFrame):
    return len(dataFrame[dataFrame['Good'] == False])

def get_bad_rate(dataFrame):
    return get_bad_loans_count(dataFrame) / get_good_loans_count(dataFrame)

def get_good_rate(dataFrame):
    return get_good_loans_count(dataFrame) / get_bad_loans_count(dataFrame)

def get_good_clients_data_frame(dataFrame):
    return dataFrame[filter_data_frame_by_good(dataFrame)]

def get_bad_clients_data_frame(dataFrame):
    return dataFrame[filter_data_frame_by_bad(dataFrame)]

def get_gray_zone_data_frame(dataFrame, parValues, cutOff):
    resultDf = dataFrame.iloc[0:0]
    
    for index, row in dataFrame.iterrows() :
        values = np.array([row['LoanAmount0'], row['LoanPeriod0']])
        calculation = row['PredictedGood0'] + values * parValues
        isAccepted = (calculation[0] >= cutOff) and (calculation[1] >= cutOff)
        if (not isAccepted):
            resultDf = resultDf.append(row)
    
    return resultDf;

def filter_people_with_score_above(dataFrame, cutOff):
    return dataFrame['PredictedGood0'] >= cutOff

def filter_people_with_score_below(dataFrame, cutOff):
    return dataFrame['PredictedGood0'] < cutOff

def get_people_with_lower_score(dataFrame, cutOff):
    return dataFrame[filter_people_with_score_below(dataFrame, cutOff)]
   
    















                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    