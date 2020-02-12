# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:48:05 2020
#https://medium.com/human-in-a-machine-world/mae-and-rmse-which-metric-is-better-e60ac3bde13d
@author: fwillia1
"""
import pandas as pd

aimm = pd.read_csv('aimm.csv')
chem = pd.read_csv('p_groupedOrder.csv')

aimm = aimm.rename({'StrmOrder':'order','area':'Area (m2)', 'vol_chg':'Volume (m3)', 'hdiff':'Height (m)'}, axis = 1)

aimm = aimm[aimm['order'].isin([3,4,5,6])]
types = {1:'deposition', 2:'erosion'}
aimm['type'] = aimm['gridcode'].map(types)
aimm['Volume (m3)'] = aimm['Area (m2)'] * aimm['Height (m)']

# depFrac = 6500.8833/11715.741
# erdFrac = 3239.7751/9901.04
depFrac = 12198.848/25769.896
erdFrac = 5922.1353/27193.312
hgtFrac = 0.5/2
areaError = {'deposition':depFrac, 'erosion':erdFrac}

grouped = aimm.groupby(['type', 'order']).sum()[['Volume (m3)']].reset_index()

grouped['dAreaFrac'] = grouped['type'].map(areaError)
grouped['dVolume (m3)'] = (grouped['dAreaFrac'].pow(2) + (hgtFrac**2)).pow(0.5) * grouped['Volume (m3)']

grouped = grouped.merge(chem, on=['order', 'type'])

grouped['Sed export (Mg)'] = grouped['Volume (m3)'] * grouped['Density (g/cm3) mean'] * 1e6 * 1e-6
grouped['dSed export (Mg)'] = ((grouped['dVolume (m3)'].div(grouped['Volume (m3)']).pow(2) + 
                          grouped['Density (g/cm3) sem'].div(grouped['Density (g/cm3) mean']).pow(2))
                          **0.5) * grouped['Sed export (Mg)'].abs()

grouped['P export (Mg)'] = grouped['Sed export (Mg)'] * grouped['P (mg/kg) mean'] * 1e-6
grouped['dP export (Mg)'] = ((grouped['dSed export (Mg)'].div(grouped['Sed export (Mg)']).pow(2) +
                          grouped['P (mg/kg) sem'].div(grouped['P (mg/kg) mean']).pow(2))
                          **0.5) * grouped['P export (Mg)'].abs()

grouped[['dV2', 'dS2', 'dP2']] = grouped[['dVolume (m3)', 'dSed export (Mg)', 'dP export (Mg)']].pow(2)

cols = ['Volume (m3)', 'dVolume (m3)', 'Sed export (Mg)', 'dSed export (Mg)', 'P export (Mg)', 'dP export (Mg)']
squares = ['dV2', 'dS2', 'dP2']
errors = ['dVolume (m3)', 'dSed export (Mg)', 'dP export (Mg)']

types = grouped.groupby('type').sum().reset_index()
types[errors] = types[squares].pow(0.5)
types = types[['type']+cols]

order = grouped.groupby('order').sum().reset_index()
order[errors] = order[squares].pow(0.5)
order = order[['order'] + cols]

full = grouped[cols + squares].sum()
full = grouped.sum()
full[errors] = full[squares].pow(0.5)
full = full[cols]

grouped = grouped[['type', 'order'] + cols]

grouped.to_csv('typeOrder.csv')
order.to_csv('order.csv')
types.to_csv('type.csv')
full.to_csv('full.csv')
print(full)