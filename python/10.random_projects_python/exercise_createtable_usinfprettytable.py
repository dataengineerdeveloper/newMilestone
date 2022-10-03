#pip install prettytable
from prettytable import PrettyTable

Table = PrettyTable(['name','age','occupation','city'])

Table.add_row(['luis','32','DE','Porto'])
Table.add_row(['eduardo','50','DA','Lisboa'])

print(Table)
print("*from prettytable")