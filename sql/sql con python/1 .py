import sqlite3
import pandas as pd

square = lambda x: x*x

" conectando con base de datos "
conexion = sqlite3.connect('sql/nothwind.db')
'esto inicia automaticamente una transaccion'

'creando la funcion en sql (nombre_en_sql , numero_de_parametros , nombre_de_la_funcion_de_python)'
conexion.create_function("square",1,square)

cursor = conexion.cursor()

'ejecutando la consulta' 
cursor.execute("""
    SELECT * FROM Employees
""")

result = cursor.fetchall()

data_frame = pd.DataFrame(result)

#establece los cambios en la base de datos
conexion.commit()

#conexion.rollback() -- regresa al estado anterior de la base de datos

'cerrando el cursor'
cursor.close()

'cerrando la conexion'
conexion.close()

print(data_frame)
