import random

class simuladordedado:
    def __init__(self):
        #aqui vamos colocar o parametros para definir a nossa app,  basicmanete vamos definir um valor min, valor max,  e a mensagem
        self.valor_minimo=1
        self.valor_maximo=6
        self.menssagem = 'gerar um novo valor? '
    
    def iniciar(self):
        #a resposta á menmsagem vai ser em formato de input,  de forma eu conseguir perceber se o utilizar quer gerar um novo valor ou nao.
        resposta = input(self.menssagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.gerarvalordodado()
            elif resposta == 'não' or resposta =='nao' or resposta =='n':
                print('agradecemos a usa participação')
            else:
                print('favor de digitar sim ou nao')
        except:
            print('ocorreu um erro')
    
    def gerarvalordodado(self):
        #este valores foram definidos na primeira funcção depois usando o random, o valor vai gerar entre 1 a 6 sendo o valor maximo
        print(random.randint(self.valor_minimo,self.valor_maximo))
        

simulador=simuladordedado()
simulador.iniciar()