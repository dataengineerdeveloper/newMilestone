"""
criar um programa pra indicar os litros tinta que sejam necessários para pintar uma parede.
"""

area = int(input(' Qual o numero da area a ser pintada: '))

litros = area //3
if area % 3 > 0:
    litros = litros + 1
    
latas = litros // 18
if litros % 18 > 0:
    latas = latas + 1
print('tu vais precisar de', latas, 'latas')
print('e o valor é de ', latas*80)

# print(litros)
# print(latas)
# print(latas*18)