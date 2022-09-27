cars =['bmw','tesla','mercedes','toyota','honda']

'''
1.
basicamente  for: é o inicio do loop
car : é o que faz referencia a cada elemento da lista
cars : é a referncia da list em questao
quando fazemos o print car, vamos ter a lista de todos os carros dentro da lista
'''


'''
2.
desta forma o que o codigo vai fazer será um loop:
    se o carro tiver o nome de 'bmw', será colocado como upper
    outros apenas colocar a primeira letra como maiuscola

'''
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.capitalize())

