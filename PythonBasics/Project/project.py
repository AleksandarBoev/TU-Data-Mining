# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:30:52 2019

@author: sa6o6
"""



#-------------------Extracting data from csv file------------------------------
filePath = 'C:/AleksandarUser/Programming/GitHubRepositories/TU-Data-Mining/Data/data.csv'

import pandas
import project_library as pl #the fix: needed to run the file [F5]. Not debug it [Ctrl] + [F5]
myDataFrame = pandas.read_csv(filePath)

#=====================Testing library methods==================================
print(pl.get_good_loans_count(myDataFrame))
print(pl.get_bad_loans_count(myDataFrame))
print(pl.get_bad_rate(myDataFrame))


#==============================================================================


#==============================================================================
#Целта е да се увеличи броят на приеманите кандидати за кредит, без 
#статистически да се влоши съотношението на "лошите" към приеманите кредитополучатели.
#За качеството на популацията от приемани кандидати се използва статистическият 
#показател Bad_Rate = Bads/Accepts.
#--------Separating the good from the bad (the goods should stay)--------------


#==============================================================================
#--------------------Identifying clients in "gray" area------------------------
#Параметри за оптимизация
#x = [LoanAmount LoanPeriod]' - два параметъра на кредита, чиито оптимални стойности се 
#търсят за всеки отхвърлян кандидат. 
#Кандидатът се приема за отхвърлян, ако PredictedGood(x) = PredictedGood0 + x'*par >= cut-off, 
#където par = [-0.0250382262277766    59.0719735110589]'.
import numpy as np    

x = np.array([myDataFrame.loc[0]['LoanAmount0'], myDataFrame.loc[0]['LoanPeriod0']])
par = np.array([-0.0250382262277766, 59.0719735110589])
result = x * par #multiplies 1st elements of each array and then the 2nd element of each array
print(result)

cutOff = 684.0 #граничен скор
isAcceptable = (result[0] < cutOff) & (result[1] < cutOff)

goodClientsDf = pl.get_good_clients_data_frame(myDataFrame)
pl.print_dataframe_firstRows(goodClientsDf, 10)
grayZoneClients = pl.get_gray_zone_data_frame(myDataFrame, par, cutOff)


#======================Testing the advanced filter=============================

grayZoneDf = pl.get_gray_zone_data_frame(myDataFrame, par, cutOff)
print('The data in the "gray zone" is: ')
pl.pretty_print_dataframe(grayZoneDf)
grayZoneNumber = len(grayZoneDf)
print(grayZoneNumber)
print(grayZoneNumber / len(myDataFrame))

lowerScorePeople = pl.get_people_with_lower_score(myDataFrame, 684.0)
pl.pretty_print_dataframe_firstRows(pl.get_good_clients_data_frame(myDataFrame), 20)