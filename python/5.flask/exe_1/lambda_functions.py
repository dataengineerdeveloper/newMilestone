price = 1000

def calc_tax(price):
    #usamos o return, para termos o retorno de um reultado
    return price * 0.3
print(calc_tax(price))

#esta linha de codigo é exatamente a mesma coisa que temos mais a cima,  so por dizer que no lugar de x está a colocar o price
calc_tax2 = lambda x: x * 0.3
print(calc_tax2(price))



### exemplo 1
"""
MAP = serve para quando precisamos de usar uma função com parametro para outra funcção // para o MAP funcionar precisa de 2 coisas função e lista
neste exemplo temos uma lista de preço e precisamos de calcular a tax para cada um dos valores representados

    
"""

prices = [100,500,10,25]

tax = list(map(lambda x:x * 0.3, prices))
print(tax)

