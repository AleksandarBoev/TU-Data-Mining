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
cutOff = 684.0

#================Data preparations, calculations and filtering=================
clients_with_scores = pl.get_df_with_client_score(df, par)
pl.print_dataframe_firstRows(clients_with_scores, 10)

print()
print()

print('Accepted clients: ')
accepted_clients = pl.get_accepted_clients(df, cutOff)
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

#=======================Testing stuffs=========================================
print(df.loc[31])
var = df.loc[31]
results = pl.get_optimized_loan_attributes(var['LoanAmount0'], var['LoanPeriod0'], var['PredictedGood0'], par, cutOff) #works
print(results)

rounded_results = pl.get_rounded_iptimized_loan_attributes(var['LoanAmount0'], var['LoanPeriod0'], var['PredictedGood0'], par, cutOff, 100)
print(rounded_results)

#==========================Again testing stuff=================================
risky_df = pl.get_risky_clients(df, 684.0)
ten_of_them = risky_df.iloc[0:0]
ten_of_them = pl.get_client_by_id(df, 111331)
counter = 0

for index, row in risky_df.iterrows() :
    ten_of_them = ten_of_them.append(row)
    counter += 1
    if (counter == 5):
        break
    
optimized_clients = pl.get_optimized_customer_df(ten_of_them, par, cutOff)
pl.print_dataframe(optimized_clients)
    
optimized_clients.to_csv(acceptedCustomersAfterAdjustmentsFilePath, index = False)

worst_client = pl.get_client_by_id(df, 111331)
print(worst_client)
optimized = pl.get_optimized_loan_attributes(worst_client['LoanAmount0'], worst_client['LoanPeriod0'], worst_client['PredictedGood0'], par, cutOff)
optimized_score = pl.calculate_new_client_score(worst_client['LoanAmount0'], worst_client['LoanPeriod0'], worst_client['PredictedGood0'], optimized[0], optimized[1], par)

print(optimized)
print(optimized_score)




