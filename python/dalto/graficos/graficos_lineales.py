#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:04:15 2010

@author: Link
"""

# graficos lineales

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#leyendo csv
df = pd.read_csv("python/dalto/graficos/estudio.csv")

#estableciendo las x y 
#junto con el archivo que se va a leer
sns.lineplot(x="fecha",y="cantidad",data=df)

#resaltando un punto del grafico
plt.plot("01-09",11,"o")
#es importante el parametro "o"

#mostrando el grafico
plt.show()




