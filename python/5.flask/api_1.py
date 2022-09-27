#cep to use: 01001000
#https://viacep.com.br/ws/01001000/json/unicode/


import requests
import os

os.system('clear')


cep = input('insert cep code: ')
#var link to use
#var will ask always for cep to indentify which json shlould i provide
r = requests.get('https://viacep.com.br/ws/{}/json/unicode/'.format(cep))
#var format
data =  r.json()

print('Print data below: ')
print()
print('cep: {}'.format(data['cep']))
print('logradouro: {}'.format(data['logradouro']))
print('Bairro: {}'.format(data['bairro']))
print('Localidade: {}'.format(data['localidade']))
print('UF: {}'.format(data['uf']))


