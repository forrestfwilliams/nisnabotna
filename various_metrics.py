# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:08:37 2020

@author: 4rest
"""
import pandas as pd

data = pd.read_csv('chemSampleGrouped.csv')
data['type'] = data['type'].str.capitalize()
aimm = pd.read_csv('resultsTypeOrder.csv')
aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] = aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] * -1

data[data['type'] == 'Erosion'].groupby('order').mean().round(2)
data[data['type'] == 'Erosion'].groupby('order').sem().round(2)

data[data['type'] == 'Deposition'].groupby('order').mean().round(3)
data[data['type'] == 'Deposition'].groupby('order').sem().round(3)


data.groupby('type').mean()
densDif = 1.241348/0.339643 # ~3.5x