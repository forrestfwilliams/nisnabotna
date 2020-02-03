# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:17:42 2019

@author: 4rest
"""
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#from scipy.stats import zscore
#implement Dixon Q?
os.chdir('C:\\Users\\4rest\\Documents\\GitHub\\iowa')
raw = pd.read_excel('ars_totalP_codes.xlsx', 'p_data')
codeTbl = pd.read_excel('ars_totalP_codes.xlsx', 'codes')
coreTbl = pd.read_excel('ars_totalP_codes.xlsx', 'cores')

codes = dict(zip(list(codeTbl['ars_code']), list(codeTbl['core_code'])))
orders = dict(zip(list(coreTbl['Number']), list(coreTbl['Order'])))
units = {1:'Camp Creek', 2:"Robert's Creek", 3:'Gunder', 4:'Gunder'}

raw['replicate'] = raw['Site ID'].str.extract(r'([a-z])')
raw['ars_code'] = raw['Site ID'].str.extract(r'(\d*)').astype('int16')

raw['core_code'] = raw['ars_code'].map(codes)
raw.loc[raw.core_code == '051e', 'core_code'] = '5105'

raw = raw[pd.notna(raw['core_code'])]
missing = raw[pd.isna(raw['core_code'])]
missing.to_csv('missing.csv')

raw['core_code'] = raw['core_code'].astype(str).str.zfill(5)
raw['core'] = raw['core_code'].str[:2].astype('int16')
raw['unit'] = raw['core_code'].str[2].astype('int16')
raw['depth'] = raw['core_code'].str[3:].astype('int16')/10
raw['P 213'] = raw['P 213']*100
raw['order'] = raw['core'].map(orders)

raw = raw.rename(columns={'Site ID':'ars_full', 'P 213':'p_mgkg'})

counts = pd.DataFrame(raw.groupby('core_code', as_index = False).size())
counts = counts.rename(columns={0:'count'})
raw = raw.join(counts, on='core_code')
#raw['z_score'] = raw.groupby('core_code').p_gkg.transform(lambda x : zscore(x))

clean = raw[['core_code','ars_code', 'replicate', 'p_mgkg', 'core', 'unit', 
             'depth', 'order', 'round', 'count']]
clean.to_csv('p_clean.csv')

grouped = clean.groupby('core_code', as_index = False).mean()
grouped.unit = grouped.unit.map(units)
grouped.to_csv('p_grouped.csv')
print(grouped['p_mgkg'].mean())
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))
sns.distplot(grouped['p_mgkg'], kde = False, ax=ax1)
sns.boxplot(x='unit', y='p_mgkg', data=grouped, ax=ax2)
sns.boxplot(x='order', y='p_mgkg', data=grouped, ax=ax3)
plt.savefig('initial_graphs.pdf')
#raw['P 213'].mean()
#
#sns.boxplot(x='unit', y='P 213', data=raw)
#raw.unit.unique()
