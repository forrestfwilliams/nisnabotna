# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:29:23 2020

@author: 4rest
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cLength = pd.read_excel('channelLength.xlsx', sheet_name='3to6')
aimm = pd.read_csv('resultsOrder.csv')
aimm = aimm.set_index('order').join(cLength.set_index('Strm_order')).reset_index()
aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] = aimm[['Volume (m3)', 'Sed export (Mg)', 'P export (Mg)']] * -1
# aimm['scaled'] = aimm['%']*aimm['Volume (m3)'].sum()
# aimm = aimm[['order', 'Volume (m3)', 'dVolume (m3)', 'scaled']]

ppArgs = {'hue':'type', 'dodge':0.2, 'palette':['#F1BE48', '#C8102E']}
sns.set('poster', font='serif', style='white')

f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
ax1 = sns.pointplot(x='order', y='Volume (m3)', data=aimm, color='#C8102E')
ax2 = ax1.twinx()
p2 = sns.pointplot(x='order', y='Length (m)', ax=ax2, data=aimm, color='grey')
p2.text(-.3, 9.5e5, "Length", horizontalalignment='left', size='medium')
p2.text(-.3, 0.9e5, "Volume", horizontalalignment='left', size='medium')
ax1.set(xlabel='Strahler Stream Order', ylabel='Net Sediment Input $(m^3)$', ylim=(0, 8.2e6))
ax2.set(xlabel='Strahler Stream Order', ylabel='Channel Length $(m)$', ylim=(0, 1.1e6))
sns.despine(ax=ax1, right=True, left=True)
sns.despine(ax=ax2, left=False, right=False)
plt.savefig('VExport_CL.png',bbox_inches='tight')