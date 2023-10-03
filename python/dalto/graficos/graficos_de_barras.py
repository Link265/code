#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:23:26 2010

@author: Link
"""

#grafico de barras

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("python/dalto/graficos/cofla.csv")

#estableciendo las x y 
#junto con el archivo que se va a leer
sns.barplot(x="fuentes",y="ingresos",data=df)

total_ingresos = df["ingresos"].sum()

print(f"el total de todos los ingresos es {total_ingresos}")

#mostrando el grafico
plt.show()





