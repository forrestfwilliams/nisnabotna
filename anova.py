# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:29:23 2020

@author: 4rest
"""
import pandas as pd
import scipy.stats as stats

def anova(row, col, data):
    names = list(data[row].dropna().unique())
    print(*names)
    vals = []
    for name in names:
        val = data.loc[data[row]==name][col].dropna()
        vals.append(val)
    #print(vals)
    result = stats.f_oneway(*vals)
    print(result[1])

data = pd.read_csv('chemSampleGrouped.csv')
data['type'] = data['type'].str.capitalize()

anova('order', 'P (mg/kg)', data[data['type'] == 'Erosion']) # Difference
anova('order', 'P (mg/kg)', data[data['type'] == 'Deposition']) # Difference

anova('order', 'Density (g/cm3)', data[data['type'] == 'Erosion']) # Difference
anova('order', 'Density (g/cm3)', data[data['type'] == 'Deposition']) # Difference

anova('unit', 'P (mg/kg)', data[data['type'] == 'Erosion']) # No Difference
anova('unit', 'Density (g/cm3)', data[data['type'] == 'Erosion']) # Difference

anova('type', 'Density (g/cm3)', data) # Difference
anova('type', 'P (mg/kg)', data) # Difference