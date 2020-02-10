# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:48:05 2020

@author: fwillia1
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

aimm = pd.read_csv('aimm.csv')
chem = pd.read_csv('p_groupedOrder.csv')

aimm = aimm.rename({'StrmOrder':'order'}, axis = 1)

aimm = aimm[aimm['order'].isin([3,4,5,6])]
types = {1:'deposition', 2:'erosion'}
aimm['type'] = aimm['gridcode'].map(types)

aimm = aimm.merge(chem, on=['order', 'type'])
aimm['P (Mg)'] = aimm['vol_chg'] * aimm['P Density (kg/m3) mean'] / 1000
aimm['Soil Loss (Mg)'] = aimm['vol_chg'] * aimm['Density (g/cm3) mean']

sums = aimm.groupby(['order', 'type']).sum()[['vol_chg', 'P (Mg)', 'Soil Loss (Mg)']].reset_index()

sns.barplot(x='order', y='vol_chg', data=sums, ci=None)
sns.barplot(x='order', y='vol_chg', hue='type', data=sums, ci=None)

sns.barplot(x='order', y='P (Mg)', data=sums, ci=None)
sns.barplot(x='order', y='P (Mg)', hue='type', data=sums, ci=None)

print(sums['vol_chg'].sum())
print(sums['P (Mg)'].sum())
print(sums['Soil Loss (Mg)'].sum())
