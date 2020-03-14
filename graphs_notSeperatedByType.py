# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:29:23 2020

@author: 4rest
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

aimm = pd.read_csv('resultsOrder.csv')
aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] = aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] * -1
aimm['offset'] = aimm['order'] - 3

sns.set('poster', font='serif', style='white')

# Volume export by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.barplot('order','Volume (m3)', data = aimm, ax=ax1, color='#C8102E', ci=None)
eBar = ax1.errorbar(x='offset', y='Volume (m3)', yerr='dVolume (m3)', fmt='none', ecolor='grey', label=None, data=aimm)
ax1.set(xlabel='Strahler Stream Order', ylabel='Sediment Exported (m3)')
sns.despine()
plt.savefig('VExport_noType.png')

# Sediment export by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.barplot('order','Sed export (Mg)', data = aimm, ax=ax1, color='#C8102E', ci=None)
eBar = ax1.errorbar(x='offset', y='Sed export (Mg)', yerr='dSed export (Mg)', fmt='none', ecolor='grey', label=None, data=aimm)
ax1.set(xlabel='Strahler Stream Order', ylabel='Sediment Exported (Mg)')
sns.despine()
plt.savefig('SExport_noType.png')

# P export by stream order
f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
sns.barplot('order','P export (Mg)', data = aimm, ax=ax1, color='#C8102E', ci=None)
eBar = ax1.errorbar(x='offset', y='P export (Mg)', yerr='dP export (Mg)', fmt='none', ecolor='grey', label=None, data=aimm)
ax1.set(xlabel='Strahler Stream Order', ylabel='TP Exported (Mg)')
sns.despine()
plt.savefig('PExport_noType.png')