#rentabilidad

import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

conexion  = sql.connect('sql/nothwind.db')

#obteniendo los 10 productos mas rentables
query = '''
    SELECT ProductName,sum(Price * Quantity) as revenue FROM Products p 
    INNER JOIN OrderDetails od
    ON od.ProductID = p.ProductID
    GROUP BY p.ProductID
    ORDER BY revenue DESC
    LIMIT 10
'''

top_products = pd.read_sql_query(query,conexion)

top_products.plot(x = 'ProductName',y = 'revenue',kind = 'bar',figsize = (10,5),legend = False)

plt.title('10 productos mas rentables')
plt.xlabel('Products')
plt.ylabel('revenue')

#rotando los nombre de los productos 90 grados para que no se encimen uno encima del otro
plt.xticks(rotation = 90)

# plt.show()


#obteniendo los 10 empleados mas efectivos

# || en sql es un operador de concatenacion de columnas 
query2 = '''
    SELECT FirstName || " " || LastName as employee, COUNT(*) as total
    FROM Orders o INNER JOIN Employees e
    ON o.EmployeeID = e.EmployeeID  
    GROUP BY o.EmployeeID
    ORDER BY total DESC
'''

top_employees = pd.read_sql_query(query2,conexion)
top_employees.plot(x = 'employee',y = "total",kind = 'bar',legend = False,figsize = (10,5))

plt.xticks(rotation = 45)

plt.show()



