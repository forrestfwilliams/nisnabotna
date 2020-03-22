# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:29:23 2020

@author: 4rest
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('chemSampleGrouped.csv')
data['type'] = data['type'].str.capitalize()
aimm = pd.read_csv('resultsTypeOrder.csv')
aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] = aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] * -1

ppArgs = {'hue':'type', 'dodge':0.2, 'palette':['#F1BE48', '#C8102E']}
sns.set('poster', font='serif', style='white')

# P by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.pointplot('order','P (mg/kg)', ax=ax1 , data = data, ci=68, linestyles='--', **ppArgs)
ax1.set(xlabel='Strahler Stream Order', ylabel='Total Phosphorus $(mg/kg)$')
ax1.legend(loc='upper left', frameon=False)
sns.despine()
plt.savefig('P.png')

# Density by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.pointplot('order','Density (g/cm3)', data = data, ax=ax1, ci=68, linestyles='--',  **ppArgs)
ax1.set(xlabel='Strahler Stream Order', ylabel='Soil Bulk Density $(g/cm^3)$')
ax1.legend(loc='center left', frameon=False)
sns.despine()
plt.savefig('Density.png')

erd = aimm[aimm['type'] == 'erosion']
erd['offset'] = erd['order'].subtract(2.8)
dep = aimm[aimm['type'] == 'deposition']
dep['offset'] = dep['order'].subtract(3.2)

# Volume export by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.barplot('order','Volume (m3)', data = aimm, ax=ax1, ci=None, **ppArgs)
eBar = ax1.errorbar(x='offset', y='Volume (m3)', yerr='dVolume (m3)', fmt='none', ecolor='grey', label=None, data = erd)
dBar = ax1.errorbar(x='offset', y='Volume (m3)', yerr='dVolume (m3)', fmt='none', ecolor='grey', label=None, data = dep)
ax1.set(xlabel='Strahler Stream Order', ylabel='Sediment Input $(m^3)$')
ax1.legend(loc='upper left', frameon=False, labels=['Deposition','Erosion'])
sns.despine()
plt.savefig('VExport.png')

# Sediment export by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.barplot('order','Sed export (Mg)', data = aimm, ax=ax1, ci=None, **ppArgs)
eBar = ax1.errorbar(x='offset', y='Sed export (Mg)', yerr='dSed export (Mg)', fmt='none', ecolor='grey', label=None, data = erd)
dBar = ax1.errorbar(x='offset', y='Sed export (Mg)', yerr='dSed export (Mg)', fmt='none', ecolor='grey', label=None, data = dep)
ax1.set(xlabel='Strahler Stream Order', ylabel='Sediment Input $(Mg)$')
ax1.legend(loc='upper left', frameon=False, labels=['Deposition','Erosion'])
sns.despine()
plt.savefig('SExport.png')

# P export by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.barplot('order','P export (Mg)', data = aimm, ax=ax1, ci=None, **ppArgs)
eBar = ax1.errorbar(x='offset', y='P export (Mg)', yerr='dP export (Mg)', fmt='none', ecolor='grey', label=None, data = erd)
dBar = ax1.errorbar(x='offset', y='P export (Mg)', yerr='dP export (Mg)', fmt='none', ecolor='grey', label=None, data = dep)
ax1.set(xlabel='Strahler Stream Order', ylabel='Total Phosphorus Input $(Mg)$')
ax1.legend(loc='upper left', frameon=False, labels=['Deposition','Erosion'])
sns.despine()
plt.savefig('PExport.png')

#Erosion Density by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
erosion = data[data['type'] == 'Erosion']
sns.pointplot('order','Density (g/cm3)', data = erosion, ax=ax1, ci=68, color='#C8102E', linestyles='--')
ax1.set(xlabel='Strahler Stream Order', ylabel='Soil Bulk Density $(g/cm^3)$')
sns.despine()
plt.savefig('erosionDensity.png')

#Deposition Density by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
deposition = data[data['type'] == 'Deposition']
sns.pointplot('order','Density (g/cm3)', data = deposition, ax=ax1, ci=68, color='#F1BE48', linestyles='--')
ax1.set(xlabel='Strahler Stream Order', ylabel='Soil Bulk Density $(g/cm^3)$')
sns.despine()
plt.savefig('depositionDensity.png')

# Density by unit
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
erosion = data[data['type'] == 'Erosion']
sns.pointplot('unit','Density (g/cm3)', data = erosion, ax=ax1, ci=68, color='#C8102E', linestyles='--')
ax1.set(xlabel='Unit', ylabel='Soil Bulk Density $(g/cm^3)$')
sns.despine()
plt.savefig('unitDensity.png')

# P by unit
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
erosion = data[data['type'] == 'Erosion']
sns.pointplot('unit','P (mg/kg)', data = erosion, ax=ax1, ci=68, color='#C8102E', linestyles='--')
ax1.set(xlabel='Unit', ylabel='Total Phosphorus $(mg/kg)$')
sns.despine()
plt.savefig('unitP.png')
