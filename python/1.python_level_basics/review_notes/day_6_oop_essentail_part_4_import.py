#IMPORT
'''vamos fzer o from da pasta onde esteja os ficheiros,  e depois identificamos o ficheiro
'''
from PYTHON.day_6_oop_essentail_part_3_methods import my_calc

calc1 = my_calc(100,50)
#nome da variavel anterior.total dos metodos dentro da class neste caso,  total e diff
total1 = calc1.total()
diff1 = calc1.diff()
print('total: ',total1)
print('diff1: ',diff1)

print('------------------')
#calculo numero 2
calc2 = my_calc(50,25)
total2 = calc2.total()
diff2 = calc2.diff()
print('total: ',total2)
print('diff1: ',diff2)