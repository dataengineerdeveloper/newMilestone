#pip install tabulate
from tabulate import tabulate

heading = ['name','age','professional']
Data = [['luis','32','DE'],['eduardo','34','DA']]
#print(tabulate(Data, headers=heading))
print(tabulate(Data, headers=heading, tablefmt='grid'))
print("*from tabulate")