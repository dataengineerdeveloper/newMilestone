import requests

#exemplo1: este link vem de awesome api, onde passamos o link,  e depois no mmomento do print apenas temos de colocar .json, ta ter visibilidade do dicionario em formato json
#data = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#print(data.json())

#METHOD GET
#exemplo2: aqui vamos tirar um conjunto de dados do firebase
#data = requests.get("https://testapi-61af4-default-rtdb.europe-west1.firebasedatabase.app/.json")
#print(data)
#print(data.json())


#METHOD POST
#No firebase sempre que vamos fazer oinsert de um dados o id é determinado pelo firebase
#insert_data = '{"Nome": "Luis Eduardo"}'
#data =  requests.post("https://testapi-61af4-default-rtdb.europe-west1.firebasedatabase.app/.json",data=insert_data)
#print(data)
#print(data.json())

#METHOD PATCH (Usado normalmente para fazer o update de um dado)
#o firebase crio o seguinte id '-MtZ0VLNmUhqToIsEMd7',  no codigo seguinte o que tenho de indicar é que quero fazer um update no nome desse id
#update_data = '{"Nome": "Lu Eduardo", "ultimo nome": "Santos", "idade": "34"}'
#data = requests.patch("https://testapi-61af4-default-rtdb.europe-west1.firebasedatabase.app/-MtZ0VLNmUhqToIsEMd7.json", data=update_data)
#print(data)
#print(data.json())

#METHOD DELETE
#imaginemos que por algum motivo crei um duplicado dentro de um user o firebase vai cria rum novo id, mas este vai estar dentro de um usaer o que está mal
#neste caso,  devemos de usar o metodo de DELETE

data = requests.delete("https://testapi-61af4-default-rtdb.europe-west1.firebasedatabase.app/-MtZ0VLNmUhqToIsEMd7/-MtZ5qb1FKqy8U7GE9gH.json")


