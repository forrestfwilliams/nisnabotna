# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:29:23 2020

@author: 4rest
"""
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt

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
aimm = pd.read_csv('resultsTypeOrder.csv')
aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] = aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] * -1

# anova('unit', 'P (mg/kg)', data) #No Difference
# anova('unit', 'Density (g/cm3)', data) #Difference

# anova('type', 'P (mg/kg)', data) #Difference (when order >= 3)
# anova('type', 'Density (g/cm3)', data) #Difference

# anova('order', 'P (mg/kg)', data[data['type'] == 'erosion']) # Difference
# anova('order', 'P (mg/kg)', data[data['type'] == 'deposition']) # Difference

# anova('order', 'Density (g/cm3)', data[data['type'] == 'erosion']) # Difference
# anova('order', 'Density (g/cm3)', data[data['type'] == 'deposition']) # Difference

# anova('order', 'P Density (kg/m3)', data[data['type'] == 'erosion']) # Difference
# anova('order', 'P Density (kg/m3)', data[data['type'] == 'deposition']) # Difference


ppArgs = {'hue':'type', 'dodge':0.2, 'palette':['#C8102E', '#F1BE48']}
sns.set('poster', font='serif', style='white')

f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.pointplot('order','P (mg/kg)', ax=ax1 , data = data, ci=68, linestyles='--', **ppArgs)
ax1.set(xlabel='Strahler Stream Order', ylabel='P (mg/kg)')
ax1.legend(loc='upper left', frameon=False)
sns.despine()
plt.savefig('P.png')

f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.pointplot('order','Density (g/cm3)', data = data, ax=ax1, ci=68, linestyles='--',  **ppArgs)
ax1.set(xlabel='Strahler Stream Order', ylabel='P (g/cm3)')
ax1.legend(loc='center left', frameon=False)
sns.despine()
plt.savefig('Density.png')

erd = aimm[aimm['type'] == 'erosion']
erd['offset'] = erd['order'].subtract(2.8)
dep = aimm[aimm['type'] == 'deposition']
dep['offset'] = dep['order'].subtract(3.2)

f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.barplot('order','Sed export (Mg)', data = aimm, ax=ax1, ci=None, **ppArgs)
eBar = ax1.errorbar(x='offset', y='Sed export (Mg)', yerr='dSed export (Mg)', fmt='none', ecolor='grey', label=None, data = erd)
dBar = ax1.errorbar(x='offset', y='Sed export (Mg)', yerr='dSed export (Mg)', fmt='none', ecolor='grey', label=None, data = dep)
ax1.set(xlabel='Strahler Stream Order', ylabel='Sediment Exported (Mg)')
ax1.legend(loc='upper left', frameon=False, labels=['Deposition','Erosion'])
sns.despine()
plt.savefig('SExport.png')

f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.barplot('order','P export (Mg)', data = aimm, ax=ax1, ci=None, **ppArgs)
eBar = ax1.errorbar(x='offset', y='P export (Mg)', yerr='dP export (Mg)', fmt='none', ecolor='grey', label=None, data = erd)
dBar = ax1.errorbar(x='offset', y='P export (Mg)', yerr='dP export (Mg)', fmt='none', ecolor='grey', label=None, data = dep)
ax1.set(xlabel='Strahler Stream Order', ylabel='TP Exported (Mg)')
ax1.legend(loc='upper left', frameon=False, labels=['Deposition','Erosion'])
sns.despine()
plt.savefig('PExport.png')