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

#=========================Dividing clients into 3 groups:======================
#1) initially accepted clients
#2) accepted clients after loan attributes adjustments
#3) denied clients after loan attributes adjustments
acceptedClientsDf = pl.get_accepted_clients(df, cutOff)
riskyClientsDf = pl.get_risky_clients(df, cutOff)

#Heavy calculations on 7k records! Time to execute: around 6 secods per record
optimizedClientsFilePath = rootFilePath + 'optimized_clients_data.csv'
pl.define_csv_file_columns([
        'ClientId',
        'LoanAmount0', 
        'LoanPeriod0', 
        'Good', 
        'PredictedGood0', 
        'OptimizedLoanAmount', 
        'OptimizedLoanPeriod', 
        'OptimizedPredictedGood'
        ], optimizedClientsFilePath)
pl.optimize_and_write_to_csv_in_chunks(riskyClientsDf, par, cutOff, 100, optimizedClientsFilePath)
optimizedClientsDf = pandas.read_csv(optimizedClientsFilePath) #already calculated

acceptedClientsAfterOptimizationDf = pl.get_accepted_clients_after_optimization(optimizedClientsDf, cutOff)
roundedAttributesAcceptedClients = pl.replace_optimized_attributes_with_rounded_values(acceptedClientsAfterOptimizationDf, par)

deniedClientsAfterOptimizationDf = pl.get_denied_clients_after_optimization(optimizedClientsDf, cutOff)

#==================Writing results onto .csv files=============================
acceptedClientsFilePath = rootFilePath + 'accepted_clients.csv'
acceptedClientsAfterAdjustmentsFilePath = rootFilePath + 'accepted_clients_after_optimizations.csv'
deniedClientsAfterAdjustmentsFilePath = rootFilePath + 'denied_clients_after_optimizations.csv'

acceptedClientsDf.to_csv(acceptedClientsFilePath, index = False)
roundedAttributesAcceptedClients.to_csv(acceptedClientsAfterAdjustmentsFilePath, index = False)
deniedClientsAfterOptimizationDf.to_csv(deniedClientsAfterAdjustmentsFilePath, index = False)

#====================Result Analysis===========================================
roundedOptimizedClientsDeviation = pl.add_deviation_column_to_rounded_optimized_clients_df(roundedAttributesAcceptedClients)
analysisFilePath = rootFilePath + 'analysis.csv'
roundedOptimizedClientsDeviation.to_csv(analysisFilePath, index = False)
