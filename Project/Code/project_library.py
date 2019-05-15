# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:19:04 2019

Important notes: rerun this file each time a change has been made! And then
reimport it where-ever it is used

@author: sa6o6
"""
import numpy as np
import pandas as pd
import math
from gekko import GEKKO  
import random  

#====================DataFrame printing functions==============================
def print_dataframe(dataFrame): #prints all data
    for index, row in dataFrame.iterrows() :
        print(row)
        print('_________________________________________________')
        
def print_dataframe_firstRows(dataFrame, firstRows): #prints number of data
    for index, row in dataFrame.iterrows() :
        print(row)
        print('_________________________________________________')
        firstRows -= 1
        if (firstRows <= 0):
            break

def pretty_string(row):
    goodCustomer = 'Yes' if row['Good'] == 1 else 'No' #ternary operator
    
    return ('%s: %s | %s: %s leva | %s: %s months | %s: %s | %s: %s' % (
          'Client id', row['ClientId'],
          'LoanAmount0', row['LoanAmount0'],
          'LoanPeriod0', row['LoanPeriod0'],
          'Good', goodCustomer,
          'PredictedGood0', row['PredictedGood0']
            ))

def pretty_print_dataframe(dataFrame): #prints all data
    for index, row in dataFrame.iterrows() :
        print(pretty_string(row))
        
def pretty_print_dataframe_firstRows(dataFrame, firstRows): #prints number of data
    for index, row in dataFrame.iterrows() :
        print(pretty_string(row))
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

#=====================Roundung loan attributes=================================
def round_floor_loan_amount_by(loanAmount, step): #1580 , 100
    residue = loanAmount % step
    loanAmount -= residue
    return loanAmount    

def round_loan_amount(loanAmount):
    if (loanAmount > 1000):
        return round_floor_loan_amount_by(loanAmount, 100)
    else:
        return round_floor_loan_amount_by(loanAmount, 50)
    
def round_loan_period(loanPeriod):
    return math.ceil(loanPeriod)

#=============Loan attributes optimization functions===========================
    
def get_optimized_loan_attributes(loanAmount0, loanPeriod0, predictedGood0, par, cutOff):
    n = GEKKO() #internet connection is needed for the GEKKO library to work!
    
    #'a' - value between '0' and '1'. 
    #Closer to '1' means loan amount will not change much. 
    #Closer to '0' - loan period will not change much
    a = 0.9

    x1 = n.Var(loanAmount0, 200.0, 160000.0) #starting value, lower boundary, upper boundary
    x2 = n.Var(loanPeriod0, 2.0, 60.0)

    n.Equation(predictedGood0 - par[0] * loanAmount0 - par[1] * loanPeriod0 + par[0] * x1 + par[1] * x2 > cutOff)

    n.Obj(a*(((x1 - loanAmount0)/loanAmount0)**2) + (1 - a)*(((x2 - loanPeriod0)/loanPeriod0)**2))
    
    try:
        n.solve(disp=False)
        return [x1.value[0], x2.value[0]]
    except: #TODO don't know how to only intercept "Solution Not Found" exception
        return [0, 0]

def get_rounded_iptimized_loan_attributes(loanAmount0, loanPeriod0, predictedGood0, par, cutOff, loanAmountStep):
    result = get_optimized_loan_attributes(loanAmount0, loanPeriod0, predictedGood0, par, cutOff)
    result[0] = round_floor_loan_amount_by(result[0], 100)
    result[1] = round_loan_period(result[1])
    return result

#=====================Client score functions=================================== 

#client_score = PredictedGood(x)
def calculate_new_client_score(loanAmount0, loanPeriod0, predictedGood0, optimizedLoanAmount, optimizedLoanPeriod, par):
    if (optimizedLoanAmount == 0 or optimizedLoanPeriod == 0):
        return 0.0
    
    values = np.array([optimizedLoanAmount, optimizedLoanPeriod])
    arrayMultiplicationResult = values * par
    arraySum = arrayMultiplicationResult[0] + arrayMultiplicationResult[1]
    new_client_score = arraySum + predictedGood0 - par[0] * loanAmount0 - par[1] * loanPeriod0 
    
    return new_client_score

def get_optimized_clients_df(dataFrame, par, cutOff):
    data = []
    for index, row in dataFrame.iterrows() :
        optimizedLoanAttributes = get_optimized_loan_attributes(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], par, cutOff)
        
        new_client_score = calculate_new_client_score(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], optimizedLoanAttributes[0], optimizedLoanAttributes[1], par)
        
        data.append([row['ClientId'], row['LoanAmount0'], row['LoanPeriod0'], row['Good'], row['PredictedGood0'], optimizedLoanAttributes[0], optimizedLoanAttributes[1], new_client_score])
            
    return pd.DataFrame(data, columns=['ClientId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'OptimizedLoanAmount', 'OptimizedLoanPeriod', 'OptimizedPredictedGood'])

def add_rounded_optimized_attributes_columns(optimizedClientsDf, par):
    data = []
    for index, row in optimizedClientsDf.iterrows() :
        roundedOptimizedLoanAmount = round_loan_amount(row['OptimizedLoanAmount'])
        roundedOptimizedLoanPeriod = round_loan_period(row['OptimizedLoanPeriod'])
        clientScoreWithRoundedValues = calculate_new_client_score(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, par)
                
        data.append([row['ClientId'], row['LoanAmount0'], row['LoanPeriod0'], row['Good'], row['PredictedGood0'], row['OptimizedLoanAmount'], row['OptimizedLoanPeriod'], row['OptimizedPredictedGood'], roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, clientScoreWithRoundedValues])
            
    return pd.DataFrame(data, columns=['ClientId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'OptimizedLoanAmount', 'OptimizedLoanPeriod', 'OptimizedPredictedGood', 'RoundedOptimizedLoanAmount', 'RoundedOptimizedLoanPeriod', 'OptimizedClientScoreWithRoundedValues'])

def calculate_deviation(loanAmount0, optimizedLoanAmount, loanPeriod0, optimizedLoanPeriod):
    a = 0.9
    return (a * ((loanAmount0 - optimizedLoanAmount) / loanAmount0)**2) + (1 - a) * (((loanPeriod0 - optimizedLoanPeriod) / loanPeriod0) ** 2)

#=======================Writing results========================================
#Since the GEKKO library works slowly and takes around 6 seconds for calculations
#per record, calculating all 7325 records at once is risky. It is better to do it
#in chunks. Note: ONLY using this function will not generate the column names.
#Before starting calculations make sure the file has only the column names defined.
def partial_writing_onto_csvfile(riskyClientsDf, par, cutOff, fromIndex, toIndex, csvFilePath):
    partOfRiskies = get_dataframe_from_index1_to_index2_exclusive(riskyClientsDf, fromIndex, toIndex)
    partOfOptimized = get_optimized_clients_df(partOfRiskies, par, cutOff)

    partOfOptimized.to_csv(csvFilePath, mode='a', header = False, index = False)

    print('Done from %s to %s' % (fromIndex, toIndex))

#=======================Get certain clients====================================
def get_client_by_id(dataframe, clientId):
    return dataframe.loc[dataframe['ClientId'] == clientId]

def get_risky_clients(dataFrame, cutOff):
    return dataFrame[dataFrame['PredictedGood0'] < cutOff]

def get_accepted_clients(dataFrame, cutOff):
    return dataFrame[dataFrame['PredictedGood0'] >= cutOff]   

def get_accepted_clients_after_optimization(optimizedDf, cutOff):
    return optimizedDf[optimizedDf['OptimizedPredictedGood'] >= cutOff]

#Clients, which couldn't be optimized automatically, get value of 0 for 'OptimizedPredictedGood'
def get_denied_clients_after_optimization(optimizedDf, cutOff):
    return optimizedDf[optimizedDf['OptimizedPredictedGood'] < cutOff]

#===================Result analysis============================================
def get_random_records(dataframe, numberOfRecordsWanted):
    if (numberOfRecordsWanted > len(dataframe)):
        return
    
    alreadyTakenIndices = {-1} #set. Need the -1, because there is no "do while" loops in Python
    result = []
    while (len(result) != numberOfRecordsWanted):
        randomIndex = -1
        while (randomIndex in alreadyTakenIndices): #do this loop until the randomly generated num is new and unused
            randomIndex = random.randint(0, len(dataframe) - 1)
            
        alreadyTakenIndices.add(randomIndex)
        result.append(dataframe.loc[randomIndex])
    return pd.DataFrame(result, columns=['ClientId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'OptimizedLoanAmount', 'OptimizedLoanPeriod', 'OptimizedPredictedGood'])


#==================Functions for testing the code==============================
def get_part_of_data_frame(dataFrame, count): #SLOW operation. More efficient would be like in "optimized clients"
    result = dataFrame.iloc[0:0] #Result: an empty data frame with same column names

    for index, row in dataFrame.iterrows() :
        result = result.append(row)
        count -= 1
        if (count <= 0):
            break;
            
    return result


#===================Additional functions=======================================
def get_dataframe_from_index1_to_index2_exclusive(dataframe, index1, index2):
    data = []
    for index in range(index1, index2): #exclusive! --> index1, index1 + 1, ... index2 - 1
        data.append(dataframe.loc[index].values)
        
    #creates a dataframe with new data and column names same as old dataframe
    return pd.DataFrame(data,columns=dataframe.columns.values) 

def get_optimized_clients_df_first_rows(dataFrame, par, cutOff, numberOfRows):
    data = []
    for index, row in dataFrame.iterrows() :
        optimizedLoanAttributes = get_optimized_loan_attributes(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], par, cutOff)
        
        new_client_score = calculate_new_client_score(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], optimizedLoanAttributes[0], optimizedLoanAttributes[1], par)
        
        data.append([row['ClientId'], row['LoanAmount0'], row['LoanPeriod0'], row['Good'], row['PredictedGood0'], optimizedLoanAttributes[0], optimizedLoanAttributes[1], new_client_score])
        
        numberOfRows -= 1
        if (numberOfRows <= 0):
            break
    return pd.DataFrame(data, columns=['ClientId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'OptimizedLoanAmount', 'OptimizedLoanPeriod', 'OptimizedPredictedGood'])

def get_optimized_clients_df_rounded_attributes(dataFrame, par, cutOff):
    data = []
    for index, row in dataFrame.iterrows() :
        optimizedLoanAttributes = get_optimized_loan_attributes(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], par, cutOff)
        roundedOptimizedLoanAmount = round_loan_amount(optimizedLoanAttributes[0])
        roundedOptimizedLoanPeriod = round_loan_period(optimizedLoanAttributes[1])
        new_client_score = calculate_new_client_score(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, par)
        
        data.append([row['ClientId'], row['LoanAmount0'], row['LoanPeriod0'], row['Good'], row['PredictedGood0'], roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, new_client_score])
            
    return pd.DataFrame(data, columns=['ClientId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'RoundedOptimizedLoanAmount', 'RoundedOptimizedLoanPeriod', 'OptimizedPredictedGood'])

def get_optimized_clients_df_rounded_attributes_first_rows(dataFrame, par, cutOff, numberOfRows):
    data = []
    for index, row in dataFrame.iterrows() :
        optimizedLoanAttributes = get_optimized_loan_attributes(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], par, cutOff)
        roundedOptimizedLoanAmount = round_loan_amount(optimizedLoanAttributes[0])
        roundedOptimizedLoanPeriod = round_loan_period(optimizedLoanAttributes[1])
        new_client_score = calculate_new_client_score(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, par)
        
        data.append([row['ClientId'], row['LoanAmount0'], row['LoanPeriod0'], row['Good'], row['PredictedGood0'], roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, new_client_score])
        numberOfRows -= 1
        if (numberOfRows <= 0):
            break
        
    return pd.DataFrame(data, columns=['ClientId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'RoundedOptimizedLoanAmount', 'RoundedOptimizedLoanPeriod', 'OptimizedPredictedGood'])

def get_optimized_clients_df_rounded_and_not(dataFrame, par, cutOff):
    data = []
    for index, row in dataFrame.iterrows() :
        optimizedLoanAttributes = get_optimized_loan_attributes(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], par, cutOff)
        
        roundedOptimizedLoanAmount = round_loan_amount(optimizedLoanAttributes[0])
        roundedOptimizedLoanPeriod = round_loan_period(optimizedLoanAttributes[1])
        
        new_client_score = calculate_new_client_score(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], optimizedLoanAttributes[0], optimizedLoanAttributes[1], par)
        new_client_score_with_rounding = calculate_new_client_score(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, par)

        data.append([row['ClientId'], row['LoanAmount0'], row['LoanPeriod0'], row['Good'], row['PredictedGood0'], optimizedLoanAttributes[0], optimizedLoanAttributes[1], new_client_score, roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, new_client_score_with_rounding])
            
    return pd.DataFrame(data, columns=['ClientId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'OptimizedLoanAmount', 'OptimizedLoanPeriod', 'OptimizedPredictedGood', 'RoundedOptimizedLoanAmount', 'RoundedOptimizedLoanPeriod', 'ClientScoreOptimizedRoundedAttributes']) 


def get_optimized_clients_df_rounded_and_not_first_rows(dataFrame, par, cutOff, numberOfRows):
    data = []
    for index, row in dataFrame.iterrows() :
        optimizedLoanAttributes = get_optimized_loan_attributes(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], par, cutOff)
        
        roundedOptimizedLoanAmount = round_loan_amount(optimizedLoanAttributes[0])
        roundedOptimizedLoanPeriod = round_loan_period(optimizedLoanAttributes[1])
        
        new_client_score = calculate_new_client_score(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], optimizedLoanAttributes[0], optimizedLoanAttributes[1], par)
        new_client_score_with_rounding = calculate_new_client_score(row['LoanAmount0'], row['LoanPeriod0'], row['PredictedGood0'], roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, par)

        data.append([row['ClientId'], row['LoanAmount0'], row['LoanPeriod0'], row['Good'], row['PredictedGood0'], optimizedLoanAttributes[0], optimizedLoanAttributes[1], new_client_score, roundedOptimizedLoanAmount, roundedOptimizedLoanPeriod, new_client_score_with_rounding])
        numberOfRows -= 1
        if (numberOfRows <= 0):
            break
            
    return pd.DataFrame(data, columns=['ClientId','LoanAmount0', 'LoanPeriod0', 'Good', 'PredictedGood0', 'OptimizedLoanAmount', 'OptimizedLoanPeriod', 'OptimizedPredictedGood', 'RoundedOptimizedLoanAmount', 'RoundedOptimizedLoanPeriod', 'ClientScoreOptimizedRoundedAttributes']) 










                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    