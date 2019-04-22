# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:30:52 2019

@author: sa6o6
"""



#-------------------Extracting data from csv file------------------------------
import pandas
import numpy as np    
import project_library as pl #the fix: needed to run the file [F5]. Not debug it [Ctrl] + [F5]
rootFilePath = 'C:/AleksandarUser/Programming/GitHubRepositories/TU-Data-Mining/Data/'
dataFilePath = rootFilePath + 'data.csv'
df = pandas.read_csv(dataFilePath)


par = np.array([-0.0250382262277766, 59.0719735110589])
cutOff = 600.0

#================Data preparations, calculations and filtering=================
clients_with_scores = pl.get_df_with_client_score(df, par)
pl.print_dataframe_firstRows(clients_with_scores, 10)

print()
print()

print('Accepted clients: ')
accepted_clients = pl.get_accepted_clients(clients_with_scores, cutOff)
pl.print_dataframe_firstRows(accepted_clients, 10)

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print('Risky clients: ')
risky_clients = pl.get_risky_clients(clients_with_scores, cutOff)
pl.print_dataframe_firstRows(risky_clients, 10)

print(len(accepted_clients))
print(len(risky_clients))

#==================Writing results onto .csv files=============================
acceptedCustomersFilePath = rootFilePath + 'accepted_customers.csv'
accepted_clients.to_csv(acceptedCustomersFilePath, index = False)
deniedCustomersAfterAdjustmentsFilePath = rootFilePath + 'denied_customers_after_adjustments.csv'
acceptedCustomersAfterAdjustmentsFilePath = rootFilePath + 'accepted_customers_after_adjustments.csv'







