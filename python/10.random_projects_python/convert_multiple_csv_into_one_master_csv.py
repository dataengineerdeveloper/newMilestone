import pandas as pd

csv_list = ['C:\Datasets\Real-Time_Traffic_Incident_Reports.csv', 'C:\Datasets\Real-Time_Traffic_Incident_Reports_1.csv']

df_master = pd.read_csv('C:\Datasets\Master.csv')

for csv_file in csv_list:
    df = pd.read_csv(csv_file)
    df.to_csv('Master.csv', mode='a', header=False, index=False)