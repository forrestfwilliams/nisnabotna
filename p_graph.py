# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:29:23 2020

@author: 4rest
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

clean = pd.read_csv('p_clean.csv')
grouped = clean.groupby('core_code', as_index = False).mean()
grouped.unit = grouped.unit.map(units)
grouped.to_csv('p_grouped.csv')
print(grouped['p_mgkg'].mean())
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))
sns.distplot(grouped['p_mgkg'], kde = False, ax=ax1)
sns.boxplot(x='unit', y='p_mgkg', data=grouped, ax=ax2)
sns.boxplot(x='order', y='p_mgkg', data=grouped, ax=ax3)
plt.savefig('initial_graphs.pdf')