# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:17:42 2019

@author: 4rest
"""
import os
import pandas as pd

def toDic(key, value):
    dic = dict(zip(list(key), list(value)))
    return(dic)
    

os.chdir('C:\\Users\\4rest\\Documents\\GitHub\\iowa')

#Load various data files
raw = pd.read_excel('ars_totalP_codes.xlsx', 'p_data')
codeTbl = pd.read_excel('ars_totalP_codes.xlsx', 'codes')
coreTbl = pd.read_excel('ars_totalP_codes.xlsx', 'cores')
depTbl = pd.read_excel('ars_totalP_codes.xlsx', 'dep')
wgtTbl = pd.read_excel('ars_totalP_codes.xlsx', 'weights')
dnsErdTbl = pd.read_excel('ars_totalP_codes.xlsx', 'densityErd')
dnsDepTbl = pd.read_excel('ars_totalP_codes.xlsx', 'densityDep')

weights = toDic(wgtTbl['Name'], wgtTbl['Weight (g)'])
codes = toDic(codeTbl['ars_code'], codeTbl['core_code'])

raw = raw[['Site ID', 'P 213']]

raw['replicate'] = raw['Site ID'].str.extract(r'([a-z])')
raw['ars_code'] = raw['Site ID'].str.extract(r'(\d*)').astype('int16')
raw['weight (g)'] = raw['Site ID'].map(weights)
raw['core_code'] = raw['ars_code'].map(codes)

raw.loc[raw.core_code == '051e', 'core_code'] = '5105'
raw['core_code'] = raw['core_code'].astype('str')
raw['core_code'] = raw['core_code'].str.zfill(5)


#Deposition
dnsErdTbl['name'] = dnsErdTbl['Sample #'].astype('str').str[:-1]
dnsErdTbl['name'] = dnsErdTbl['name'].str.zfill(5)
dnsErdMrg = dnsErdTbl.groupby('name').mean()
dnsErd = toDic(dnsErdMrg.index, dnsErdMrg['Final Density (g/cm3)'])

dnsDep = toDic(dnsDepTbl['Name'].str.zfill(5), dnsDepTbl['density (g/cm3)'])

dns = {**dnsErd , **dnsDep}

#For Bank Samples
ordersBank = toDic(coreTbl['Number'], coreTbl['Order'])
units = {1:'Camp Creek', 2:"Robert's Creek", 3:'Gunder', 4:'Gunder'}

bank = raw[raw['core_code'].str.contains("_") == False]

bank['core'] = bank['core_code'].str[:2].astype('int16')
bank['unit'] = bank['core_code'].str[2].astype('int16').map(units)
bank['depth'] = bank['core_code'].str[3:].astype('int16')/10
bank['order'] = bank['core'].map(ordersBank)
bank['type'] = 'erosion'

#For Dep Samples
ordersDep = toDic(depTbl['Site'], depTbl['Order'])

dep= raw[raw['core_code'].str.contains("_")]
dep['core'] = dep['core_code'].str[:3].astype('int16')
dep['order'] = dep['core'].map(ordersDep)
dep['type'] = 'deposition'

clean = bank.append(dep)
clean['Density (g/cm3)'] = clean['core_code'].map(dns)
clean['P (mg/kg)'] = clean['P 213'] * 50 / clean['weight (g)']
clean['P Density (kg/m3)'] = clean['P (mg/kg)'] * clean['Density (g/cm3)'] / 1000
clean = clean.drop(['Site ID', 'P 213', 'replicate', 'ars_code', 'weight (g)', 'core'], axis=1)
clean.to_csv('p_clean.csv')

clean['P (mg/kg)'] = clean['P (mg/kg)'].astype('float')
clean['Density (g/cm3)'] = clean['Density (g/cm3)'].astype('float')
clean['P Density (kg/m3)'] = clean['P Density (kg/m3)'].astype('float')

clean[['core_code', 'unit', 'depth', 'order', 'type']] = clean[['core_code', 'unit', 'depth', 'order', 'type']].astype('str')
grouped = clean.groupby(['core_code', 'unit', 'depth', 'order', 'type']).mean().reset_index()
grouped.to_csv('p_grouped.csv')