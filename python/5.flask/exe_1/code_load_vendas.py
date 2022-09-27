"""
Para este desenvolvimento,  vamos usar 3 lib:
pandas
openpyxl
twilio

Vamos fazer uma pequena analise com base de 3 ficheiros com dados de vendas e vamos ver qual o vendedor que atingiu um determinado valor
e em que mes é que ocorreu, depois disso vamos enviar os dados via sms com o resultado final

email de twilio: dataengineer.developer@gmail.com // password: !Q"W#E$R%T&Y/U(I)O
account sid: AC0bd8efb921b70b677db0d6ba731c435a
token: da4969a74f114bba567cbaccac8d7941

phone number:  +16067220261

Codigo testado funcionou com sucesso


"""

import pandas as pd
from twilio.rest import Client
 
 #account_sid
account_sid = 'AC0bd8efb921b70b677db0d6ba731c435a'
auth_token = 'da4969a74f114bba567cbaccac8d7941'
Client = Client(account_sid, auth_token)
 
lista_de_meses = ['janeiro','Fevereiro','Março']

for mes in lista_de_meses:
    #f' é usado quando precisamos de formatar algo no codigo,  nesta situação preciso de tornar aquilo que está dentro da listad e lista_de_meses,  de forma dinamica
    tabela_de_vendas = pd.read_excel(f'c:/DataEngineer/100DaysDataEngineer/1. SPRINTS/SPRINT_1/PYTHON/Develop_python_skill/exe_1/{mes}.xlsx')
    #.any() caso seja encontradod algum valor maior que 8000
    #comando vai validar nos diferentes ficheiros na coluna de vendas se existe algum vamor acima de 8000
    if (tabela_de_vendas['vendas']>8000).any():
        #nota: qunado uso o .loc vou querer que seja faça uma localização do um valor, e que me vai ser apresentado vai ser uma tabela, no caso de precisas apenas de uma valor devo de passar no fim .values[0]
        vendedor = tabela_de_vendas.loc[tabela_de_vendas['vendas']>8000,'vendedor'].values[0]
        vendas = tabela_de_vendas.loc[tabela_de_vendas['vendas']>8000,'vendas'].values[0]
        print(f'no mes de {mes} o vendedor {vendedor} atingiu um valor de {vendas}€')
        message = Client.messages.create(
            to = '+351918091647',
            from_='+16067220261',
            body = f'no mes de {mes} o vendedor {vendedor} atingiu um valor de {vendas}€')
        print(message.sid)
        
    


