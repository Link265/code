import sqlite3
import pandas as pd

with sqlite3.connect('../nothwind.db') as archivo:

    df  = pd.read_sql('SELECT * FROM Products',archivo)

    print(df)

    