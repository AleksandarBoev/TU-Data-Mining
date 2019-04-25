# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:03:50 2019

Testing functions

@author: sa6o6
"""

import pandas   
import numpy as np
import project_library as pl #reimport each time a change has been made to the library!

rootFilePath = 'C:/AleksandarUser/Programming/GitHubRepositories/TU-Data-Mining/Data/'
dataFilePath = rootFilePath + 'data.csv'
acceptedClientsAfterAdjustmentsFilePath = rootFilePath + 'accepted_clients_after_adjustments.csv'


df = pandas.read_csv(dataFilePath)
#========================Calculation parameters================================
par = np.array([-0.0250382262277766, 59.0719735110589])
cutOff = 684.0

riskyClientsDf = pl.get_risky_clients(df, cutOff)

#========================Testing stuff=========================================
ten_risky_clients = pl.get_part_of_data_frame(riskyClientsDf, 10)
ten_optimized_clients = pl.get_optimized_clients_df(ten_risky_clients, par, cutOff)

#appending to a csv file instead of wiping it clean and writing on it
ten_risky_clients.to_csv(acceptedClientsAfterAdjustmentsFilePath, mode='a', header=False, index = False) 


#=========================Testing optimization=================================
#CustomerId        100032.00000
#LoanAmount0         4000.00000
#LoanPeriod0           10.00000
#Good                   0.00000
#PredictedGood0      -322.00000
#ClientScore          168.56683

results = pl.get_optimized_loan_attributes(4000, 10, -200000, par, cutOff)
print(results)