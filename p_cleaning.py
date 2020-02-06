# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:17:42 2019

@author: 4rest
"""
import os
import pandas as pd


os.chdir('C:\\Users\\4rest\\Documents\\GitHub\\iowa')
raw = pd.read_excel('ars_totalP_codes.xlsx', 'p_data')
codeTbl = pd.read_excel('ars_totalP_codes.xlsx', 'codes')
coreTbl = pd.read_excel('ars_totalP_codes.xlsx', 'cores')
depTbl = pd.read_excel('ars_totalP_codes.xlsx', 'dep')
wgtTbl = pd.read_excel('ars_totalP_codes.xlsx', 'weights')

codes = dict(zip(list(codeTbl['ars_code']), list(codeTbl['core_code'])))
weights = dict(zip(list(wgtTbl['Name']), list(wgtTbl['Weight (g)'])))

raw = raw[['Site ID', 'P 213']]
raw['replicate'] = raw['Site ID'].str.extract(r'([a-z])')
raw['ars_code'] = raw['Site ID'].str.extract(r'(\d*)').astype('int16')
raw['weight (g)'] = raw['Site ID'].map(weights)
raw['core_code'] = raw['ars_code'].map(codes)
raw.loc[raw.core_code == '051e', 'core_code'] = '5105'
raw['core_code'] = raw['core_code'].astype('str')
raw['core_code'] = raw['core_code'].str.zfill(5)

#For Bank Samples
ordersBank = dict(zip(list(coreTbl['Number']), list(coreTbl['Order'])))
units = {1:'Camp Creek', 2:"Robert's Creek", 3:'Gunder', 4:'Gunder'}

bank = raw[raw['core_code'].str.contains("_") == False]

bank['core'] = bank['core_code'].str[:2].astype('int16')
bank['unit'] = bank['core_code'].str[2].astype('int16')
bank['depth'] = bank['core_code'].str[3:].astype('int16')/10
bank['order'] = bank['core'].map(ordersBank)
bank['type'] = 'erosion'

#For Dep Samples
ordersDep = dict(zip(list(depTbl['Site']), list(depTbl['Order'])))

dep= raw[raw['core_code'].str.contains("_")]
dep['core'] = dep['core_code'].str[:3].astype('int16')
dep['order'] = dep['core'].map(ordersDep)
dep['type'] = 'deposition'

clean = bank.append(dep)
clean['P mgkg'] = clean['P 213'] * 50 / clean['weight (g)']
clean.to_csv('p_clean.csv')