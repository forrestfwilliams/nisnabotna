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


data[data['type'] == 'Erosion'].groupby('order').mean().round()
data[data['type'] == 'Erosion'].groupby('order').sem().round(2)

data[data['type'] == 'Deposition'].groupby('order').mean().round(3)
data[data['type'] == 'Deposition'].groupby('order').sem().round(3)


data.groupby('type').mean()
densDif = 1.241348/0.339643 # ~3.5x

order3prop = -960003.4031309992/1.03957e+06

erd = aimm[aimm['type'] == 'Erosion']
dep = aimm[aimm['type'] == 'Deposition']

test = aimm[['order', 'type', 'Volume (m3)']]
pivoted = test.pivot(index='order', columns='type')['Volume (m3)'].reset_index().set_index('order')
pivoted.columns.name = None
# pivoted = pivoted.set_index('order')
pivoted['prop'] = pivoted.deposition/pivoted.erosion*-1

pivoted.loc[6,'erosion']/pivoted.erosion.sum()

aimm2 = pd.read_csv('resultsOrder.csv').set_index('order')
aimm2.loc[6,'Volume (m3)']/aimm2['Volume (m3)'].sum()
