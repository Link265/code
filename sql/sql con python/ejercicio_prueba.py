import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

with sql.connect('sql/nothwind.db') as conn:
    #obteniendo cuanto genero cada empleado
    query = '''
    SELECT FirstName,revenue 
    FROM Employees e LEFT JOIN (SELECT sum(ganancia) as revenue,EmployeeID FROM (SELECT OrderID,sum(price*Quantity) as ganancia 
    FROM OrderDetails od INNER JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY OrderID) ord INNER JOIN Orders o ON o.OrderID = ord.OrderID
    GROUP BY EmployeeID) ide ON ide.EmployeeID = e.EmployeeID
    ORDER BY revenue ASC
    LIMIT 5
    '''

    grafico = pd.read_sql_query(query,conn)
    grafico.plot(x = 'FirstName', y = 'revenue',kind = 'box',figsize = (10,5))
    plt.xticks(rotation = 0)
    plt.xlabel('empleados')
    plt.ylabel('revenue')
    plt.show()

    