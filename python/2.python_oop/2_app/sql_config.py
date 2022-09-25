import pyodbc

data_connections = (
    "Driver={SQL Server};"
    "Server=localhost;"
    "Database=Northwind;"
    "UID=sa;"
    "PWD=YourPassword123;"
    "Trusted_Connection=yes;"
)

connection=pyodbc.connect(data_connections)
print("connection established")


cursor = connection.cursor()

comand = """SELECT TOP(100) * FROM Northwind.dbo.Categories"""

cursor.execute(comand)
cursor.commit()