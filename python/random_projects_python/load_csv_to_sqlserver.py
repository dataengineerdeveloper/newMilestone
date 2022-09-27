import pyodbc # pip install pypyodbc
import pandas as pd # pip install pandas

SERVER_NAME = 'BI4ALLWSN357\MSSQLSERVER01'
DATABASE_NAME = 'python'

"""
Step 1. Importing dataset from CSV
"""
df = pd.read_csv('C:\Datasets\Real-Time_Traffic_Incident_Reports.csv')

"""
Step 2.1 Data clean up
"""
df['Published Date'] = pd.to_datetime(df['Published Date']).dt.strftime('%Y-%m-%d %H:%M:%S')
df['Status Date'] = pd.to_datetime(df['Published Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

df.drop(df.query('Location.isnull() | Status.isnull()').index, inplace=True)


"""
Step 2.2 Specify columns we want to import
"""
columns = ['Traffic Report ID', 'Published Date', 'Issue Reported', 'Location', 
            'Address', 'Status', 'Status Date']

df_data = df[columns]
records = df_data.values.tolist()

"""
Step 3.1 Create SQL Servre Connection String
"""
DRIVER = 'SQL Server'
SERVER_NAME = 'BI4ALLWSN357\MSSQLSERVER01'
DATABASE_NAME = 'python'

def connection_string(driver, server_name, database_name):
    conn_string = f"""
        DRIVER={{{driver}}};
        SERVER={server_name};
        DATABASE={database_name};
        Trust_Connection=yes;        
    """
    return conn_string


"""
Step 3.2 Create database connection instance
"""
try:
    conn = pyodbc.connect(connection_string(DRIVER, SERVER_NAME, DATABASE_NAME))
except pyodbc.DatabaseError as e:
    print('Database Error:')    
    print(str(e.value[1]))
except pyodbc.Error as e:
    print('Connection Error:')
    print(str(e.value[1]))


sql_insert = '''
    INSERT INTO [python].[dbo].[Austion_Traffic_Incident]
    VALUES (?, ?, ?, ?, ?, ?, ?, GETDATE())
'''

try:
    cursor = conn.cursor()
    cursor.executemany(sql_insert, records)
    cursor.commit();    
except Exception as e:
    cursor.rollback()
    print(str(e[1]))
finally:
    print('Task is complete.')
    cursor.close()
    conn.close()