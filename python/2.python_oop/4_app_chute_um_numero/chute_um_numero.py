#criar um algortimo que gere m valor aleatorio e eu tenho de que ficar tentando o numero até eu acertar
import random

class chute:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo =  100
        self.tentardenovo = True
        
    def iniciar(self):
        self.gerarnumeroaleatorio()
        self.pedirvaloraleatorio()
        while self.tentardenovo == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print('chute um valor mais baixo: ')
                self.pedirvaloraleatorio()
            elif int(self.valor_do_chute)< self.valor_aleatorio:
                print('chute um valor mais alto: ')
                self.pedirvaloraleatorio()
            if int(self.valor_do_chute) == self.valor_aleatorio:
                self.tentardenovo = False
                print('parabens acertaste!')

                
    def pedirvaloraleatorio(self):
        self.valor_do_chute = input('chute um numero: ')
    def gerarnumeroaleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)
    
chute= chute()
chute.iniciar()
    