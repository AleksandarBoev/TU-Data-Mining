# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:19:04 2019

@author: sa6o6
"""
import numpy as np
import pandas as pd

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
        
def print_dataframe_firstRows(dataFrame, firstRows): #prints number of data
    for index, row in dataFrame.iterrows() :
        print(row)
        print('_________________________________________________')
        firstRows -= 1
        if (firstRows <= 0):
            break

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

def calculate_predicted_good(row, par):
    values = np.array([row['LoanAmount0'], row['LoanPeriod0']])
    arrayMultiplicationResult = values * par
    arraySum = arrayMultiplicationResult[0] + arrayMultiplicationResult[1]
    predictedGood = arraySum + row['PredictedGood0']
    return predictedGood

def get_gray_zone_data_frame(dataFrame, parValues, cutOff):
    resultDf = dataFrame.iloc[0:0] #TODO add new row --> predicted good
    
    for index, row in dataFrame.iterrows() :
        predictedGood = calculate_predicted_good(row, parValues)
        isAccepted = predictedGood >= cutOff
        if (not isAccepted):
            resultDf = resultDf.append(row)
    
    return resultDf;

def get_risky_clients(dataFrame, par, cutOff): #TODO test it out
    data = []
    for index, row in dataFrame.iterrows() :
        predictedGood = calculate_predicted_good(row, par)
        isDenied = predictedGood < cutOff
        if (isDenied):
            data.append([row['CustomerId'], row['LoanAmount0'], row['LoanPeriod0'], row['Good'], row['PredictedGood0'], predictedGood])
            
    return pd.DataFrame(data, columns=['CustomerId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'CalculatedPredictedGood'])
    

def filter_people_with_score_above(dataFrame, cutOff):
    return dataFrame['PredictedGood0'] >= cutOff

def filter_people_with_score_below(dataFrame, cutOff):
    return dataFrame['PredictedGood0'] < cutOff

def get_people_with_lower_score(dataFrame, cutOff):
    return dataFrame[filter_people_with_score_below(dataFrame, cutOff)]
   
    















                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    