# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 08:22:16 2020

@author: fwillia1
"""
import matplotlib.pyplot as plt
import pandas as pd

width = 0.35
aimm = pd.read_csv('typeOrder.csv')
erd = aimm[aimm['type'] == 'erosion']
dep = aimm[aimm['type'] == 'deposition']
dep['offset'] = dep['order'] + width

fig, ax = plt.subplots(1,1,figsize=(10,10))
bar1 = ax.bar('order', 'Volume (m3)', width, bottom=0, yerr='dVolume (m3)', data = erd)
bar2 = ax.bar('offset', 'Volume (m3)', width, bottom=0, yerr='dVolume (m3)', data = dep)
plt.show()
##plt.savefig('test.png')
