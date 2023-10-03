#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:41:55 2010

@author: Link
"""

#grafico de dispersion


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("python/dalto/graficos/datos3.csv")

sns.scatterplot(x="tiempo",y="dinero",data=df)

plt.show()


 
