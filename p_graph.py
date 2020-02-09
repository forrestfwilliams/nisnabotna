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

data = pd.read_csv('p_grouped.csv')

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


ppArgs = {'hue':'type', 'dodge':0.2, 'palette':['#C8102E', '#F1BE48'], 'linestyles':'--',
          'data':data}
sns.set('poster', font='serif', style='white')

f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.pointplot('order','P (mg/kg)', ax=ax1 , **ppArgs)
ax1.set(xlabel='Strahler Stream Order', ylabel='P (mg/kg)')
ax1.legend(loc='upper left', frameon=False)
sns.despine()
plt.savefig('P.png')

f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.pointplot('order','Density (g/cm3)', ax=ax1, **ppArgs)
ax1.set(xlabel='Strahler Stream Order', ylabel='P (g/cm3)')
ax1.legend(loc='best', frameon=False)
sns.despine()
plt.savefig('Density.png')

f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.pointplot('order','P Density (kg/m3)', ax=ax1, **ppArgs)
ax1.set(xlabel='Strahler Stream Order', ylabel=r'P Density (kg/m^3)')
ax1.legend(loc='upper left', frameon=False)
sns.despine()
plt.savefig('P Density.png')