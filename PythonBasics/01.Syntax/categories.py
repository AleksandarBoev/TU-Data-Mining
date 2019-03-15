# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:53:54 2019

@author: sa6o6
"""

#Creating nominal variables
#(nominals can't be ordered)
import numpy as np
import pandas as pd

nominalData = np.array(['BG', 'EN', 'GB', 'DE', 'zz', 'EN'])
nominalCategories = np.array(['GB', 'EN', 'BG', 'DE'])

categoricalNominalData = pd.Categorical(nominalData, nominalCategories)

print(notSure)

#print results:
# =============================================================================
#    [BG, EN, GB, DE, NaN, EN] 
#    Categories (4, object): [GB, EN, BG, DE]
# =============================================================================
#'zz' is not in the categories, so it is turned into Nan

nominalSeries = pd.Series(categoricalNominalData)
print(nominalSeries)

#print results:
# =============================================================================
# 0     BG
# 1     EN
# 2     GB
# 3     DE
# 4    NaN
# 5     EN
# dtype: category
# Categories (4, object): [GB, EN, BG, DE]
# =============================================================================
#just gives the data indexes

print(nominalSeries[3]) #prints 'DE'

nominalSeries2 = pd.Series(categoricalNominalData, dtype='category')
print(nominalSeries2) 
#just changes the type. I think this makes it possible to work 
#with other libraries, which work with categories

np.append(nominalSeries2, 'BG')
print(nominalSeries2)
#===================================================================

ordinalData = np.array(['Old', 'Middle', 'Middle', 'Young',
                        'Middle', 'Young', 'Old', 'Young',
                        'Baby'])
ordinalCategories = np.array(['Baby', 'Young', 'Middle', 'Old'])

categoricalOrdinalData = pd.Categorical(ordinalData,
                                        categories=ordinalCategories,
                                        dtype = 'category',
                                        ordered = True)
#dtypes are: bool, object, category, int64, int8 and other
print(categoricalOrdinalData)

#===================================================================

nowThisIsCool = pd.DataFrame({'Sasho' : ['Java', 'Python', 'JS']})
print(nowThisIsCool)
