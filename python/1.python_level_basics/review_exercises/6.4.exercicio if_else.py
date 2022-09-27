'''
Pra este exercio que é pretendido é que se coloque um valor, pode ser negativo ou positivo e o nosso program term validar se o valor é negativo ou positivo
'''

a = float(input('insira o valor:'))

def number_check(a):
    if a > 0:
        print('valor positivo')
    elif a < 0:
        print('valor é negativo')
    else:
         print('valor não não conhecido')

    number_check(a)
