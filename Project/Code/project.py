# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:30:52 2019

@author: sa6o6
"""

#===================Extracting data from csv file onto data frame==============
import pandas   
import numpy as np
import project_library as pl #reimport each time a change has been made to the library!

rootFilePath = 'C:/AleksandarUser/Programming/GitHubRepositories/TU-Data-Mining/Project/Data/'
dataFilePath = rootFilePath + 'data.csv'

df = pandas.read_csv(dataFilePath)
#==================Initializing calculation parameters=========================
par = np.array([-0.0250382262277766, 59.0719735110589])
cutOff = 350.0

#============================Dividing clients into 3 groups:
#1) initially accepted clients
#2) accepted clients after loan attributes adjustments
#3) denied clients after loan attributes adjustments
acceptedClientsDf = pl.get_accepted_clients(df, cutOff)
riskyClientsDf = pl.get_risky_clients(df, cutOff)

#Heavy calculations on 18k records! Time to execute: around 6 secods per record
#Use the "partial_writing_onto_csvfile" function from "project_library"
#clientsWithOptimizedLoansDf = pl.get_optimized_clients_df(riskyClientsDf, par, cutOff) 
#TODO lets say calculations were done. Load the calculated optimized clients from file
acceptedClientsAfterOptimizationDf = pl.get_accepted_clients_after_optimization(clientsWithOptimizedLoansDf, cutOff)
deniedClientsAfterOptimizationDf = pl.get_denied_clients_after_optimization(clientsWithOptimizedLoansDf, cutOff)

#==================Writing results onto .csv files=============================
acceptedClientsFilePath = rootFilePath + 'accepted_clients.csv'
acceptedClientsAfterAdjustmentsFilePath = rootFilePath + 'accepted_clients_after_adjustments.csv'
deniedClientsAfterAdjustmentsFilePath = rootFilePath + 'denied_clients_after_adjustments.csv'

#to append to a file, instead of rewriting it: df.to_csv('my_csv.csv', mode='a', header=False, index = False)
acceptedClientsDf.to_csv(acceptedClientsFilePath, index = False)
acceptedClientsAfterOptimizationDf.to_csv(acceptedClientsAfterAdjustmentsFilePath, index = False)
deniedClientsAfterOptimizationDf.to_csv(deniedClientsAfterAdjustmentsFilePath, index = False)

#====================Result Analysis===========================================
pandas.set_option('display.max_columns', 500)

partOfRiskyClients = pl.get_part_of_data_frame(riskyClientsDf, 10)
optimizedClientsRoundedValues = pl.get_optimized_clients_df_first_rows(riskyClientsDf, par, cutOff, 10)
print(optimizedClientsRoundedValues)

a = 0.9
fResults = [] #TODO some stuff
for index, row in optimizedClientsRoundedValues.iterrows() :
    #fResult.append([(row['LoanAmount0'], ])
    f = (a * ((row['LoanAmount0'] - row['RoundedOptimizedLoanAmount']) / row['LoanAmount0'])**2) + (1 - a) * (((row['LoanPeriod0'] - row['RoundedOptimizedLoanPeriod']) / row['LoanPeriod0']) ** 2)
    print(f)
    
print(fResults)

#TODO new df which adds rounded values and new RoundedPredictedGood
#TODO also the function thingy, which is calculated on the ROUNDED values. Call it "Deviation"


