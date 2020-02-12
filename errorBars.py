# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:43:52 2020

@author: 4rest
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('typeOrder.csv')
df["lb"] = df["m"]-df["lb"]
df["ub"] = df["ub"]-df["m"]

def func(x,y,h,lb,ub, **kwargs):
    data = kwargs.pop("data")
    # from https://stackoverflow.com/a/37139647/4124317
    errLo = data.pivot(index=x, columns=h, values=lb)
    errHi = data.pivot(index=x, columns=h, values=ub)
    err = []
    for col in errLo:
        err.append([errLo[col].values, errHi[col].values])
    err = np.abs(err)
    p = data.pivot(index=x, columns=h, values=y)
    p.plot(kind='bar',yerr=err,ax=plt.gca(), **kwargs)

g = sns.FacetGrid(df, col="variables", size=4, aspect=.7,  ) 
g.map_dataframe(func, "grp2", "m", "grp1", "lb", "ub" , color=["limegreen", "indigo"]) 
g.add_legend()

plt.show()