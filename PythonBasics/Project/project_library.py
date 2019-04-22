# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:19:04 2019

@author: sa6o6
"""
import numpy as np
import pandas as pd

#====================DataFrame printing functions==============================
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
    
#========================Good/Bad clients functions============================
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

#=====================Client score functions===================================

def calculate_client_score(row, par):
    values = np.array([row['LoanAmount0'], row['LoanPeriod0']])
    arrayMultiplicationResult = values * par
    arraySum = arrayMultiplicationResult[0] + arrayMultiplicationResult[1]
    client_score = arraySum + row['PredictedGood0'] #client_score = PredictedGood(x)
    return client_score

def get_df_with_client_score(dataFrame, par):
    data = []
    for index, row in dataFrame.iterrows() :
        client_score = calculate_client_score(row, par)
        data.append([row['CustomerId'], row['LoanAmount0'], row['LoanPeriod0'], row['Good'], row['PredictedGood0'], client_score])
            
    return pd.DataFrame(data, columns=['CustomerId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'ClientScore'])

def get_risky_clients(dataFrame, cutOff):
    return dataFrame[dataFrame['ClientScore'] < cutOff]

def get_accepted_clients(dataFrame, cutOff):
    return dataFrame[dataFrame['ClientScore'] >= cutOff]
    
   
#=================















                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    