#Concatenate Pandas DataFrames Without Duplicates

import pandas as pd

df1 = pd.DataFrame({ 'colA': [10, 20, 30],
                     'colB': [100, 200, 300]})

df2 = pd.DataFrame({ 'colA': [40, 20, 50],
                     'colB': [400, 200, 500]})
    
new_df = pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True)
print(new_df)


#Check Duplicate Records Before Append New Records 

import pandas as pd

df = pd.DataFrame({
    'Name': ['Joe', 'Mary'],
    'Age': [29, 30]
})

records = [['Mary', 30], ['Steve', 31]]

for record in records:
    if not record in df.values:
        df = df.append(pd.Series(record, index=df.columns), ignore_index=True)
print(df)