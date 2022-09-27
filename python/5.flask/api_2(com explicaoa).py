from urllib import request
import pandas as pd
#posso usar o jsonify que é uma extensao o flask para devolver a resposta em formato de json
from flask import Flask, jsonify


app = Flask(__name__)

#aqui vamos ter de criar um decorator que basimcamente é o link para aceder ao homepage
@app.route('/')
# criar funcionalidades(para cada pagina de um site tenhode criar um funcao def)
def homepage():
    #etsa é a mensagem que me aparece sempre que entro no site
    return 'API is live'

#Este comando tb deu erro,  mas penso que foi por causa do formato do ficheiro
#@app.route -  é um caminho dentro do site
@app.route('/sales')
#funcao de sales para ter visibilidade dos dados
def sales():
    #posso testar este codifo no jupyter antes de passar para dentro desta função
    table = pd.read_csv('C:/advertising.csv')
    total_sales = table['vendas'].sum()
    resquest = {'total_sales': total_sales}
    #usar a extensao de jsonify antes da  varivael request
    return jsonify(request)
    
# esta foi a segunda opção de usar um gile json, contudo nao funcionoiu deu erro
#@app.route('/sales')
#def sales():
 #   table = pd.read_json('C:\Datasets\Advertising.json')
  #  table.vendas.sum()
   # request = {'table': table}
    #return(request)

#comando para executar a api
app.run()