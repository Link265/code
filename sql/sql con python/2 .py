import sqlite3 as sql
import pandas as pd

square = lambda x: x*x

with sql.connect('sql/nothwind.db') as conexion:
    conexion.create_function('square',1,square)

    #se podria abrir el cursor tambien con with pero sqlite no lo permite
    cursor = conexion.cursor()
    cursor.execute('SELECT *,square(Price) as precio_al_cuadrado FROM Products')

    result = cursor.fetchall()

    cursor.close()

    date_frame = pd.DataFrame(result)

print(date_frame)