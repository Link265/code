#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:49:36 2010

@author: Link
"""

#grafico de cajas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("python/dalto/graficos/bigotes.csv")

sns.boxplot(x="categoria",y="valor",data=df)

plt.show()

