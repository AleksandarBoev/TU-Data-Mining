# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:30:52 2019

@author: sa6o6
"""

#-------------------Extracting data from csv file onto data frame--------------
import pandas   
import numpy as np
import project_library as pl #reimport each time a change has been made to the library!

rootFilePath = 'C:/AleksandarUser/Programming/GitHubRepositories/TU-Data-Mining/Data/'
dataFilePath = rootFilePath + 'data.csv'

df = pandas.read_csv(dataFilePath)
#========================Calculation parameters================================
par = np.array([-0.0250382262277766, 59.0719735110589])
cutOff = 684.0

#============================Dividing clients into 3 groups:
#1) initially accepted clients
#2) accepted clients after loan attributes adjustments
#3) denied clients after loan attributes adjustments
acceptedClientsDf = pl.get_accepted_clients(df, cutOff)
riskyClientsDf = pl.get_risky_clients(df, cutOff)

clientsWithOptimizedLoansDf = pl.get_optimized_clients_df(riskyClientsDf, par, cutOff)

acceptedClientsAfterOptimizationDf = pl.get_accepted_clients_after_optimization(clientsWithOptimizedLoansDf, cutOff)
deniedClientsAfterOptimizationDf = pl.get_denied_clients_after_optimization(clientsWithOptimizedLoansDf, cutOff)

#==================Writing results onto .csv files=============================
acceptedClientsFilePath = rootFilePath + 'accepted_clients.csv'
acceptedClientsAfterAdjustmentsFilePath = rootFilePath + 'accepted_clients_after_adjustments.csv'
deniedClientsAfterAdjustmentsFilePath = rootFilePath + 'denied_clients_after_adjustments.csv'

acceptedClientsDf.to_csv(acceptedClientsFilePath, index = False)
acceptedClientsAfterOptimizationDf.to_csv(acceptedClientsAfterAdjustmentsFilePath, index = False)
deniedClientsAfterOptimizationDf.to_csv(deniedClientsAfterAdjustmentsFilePath, index = False)


