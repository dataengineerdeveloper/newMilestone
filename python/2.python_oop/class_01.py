#class
class computador:
    #init, serve to iniitaliazate and app
    # para alem disso depois de ter o self dentro dos paramentros tenho de passar novos argumentos,  nesta caos vai ser marca,l  memoria_ram, placa_grafica
    def __init__(self,marca, memoria_ram, placa_grafica):
        #using self in a functions help us to call methods from other functions.  in this casse the values are hardecoded,  but we need to build this dynamically
        #self.marca = 'asus'
        #here i can find a couple of attributes within a class    
        self.marca = marca    
        self.memoria_ram = memoria_ram
        self.placa_grafica = placa_grafica
#in a program i can get a option to turn on,  turn off and  show configuratuions

    def turnon(self):
        print("starting program")
        
    def turnoff(self):
        print("turning off")
    
    #PT - se precisarmos de usar uns attributos especificos numa outra funcao eu devo de usar o self,  porque neste exemplo eu usei o self logo no inicio e desta foram estoua usar novamente
    #neste nova funcao
    def showconfig(self):
        print(self.marca, self.placa_grafica, self.placa_grafica)
        

computador_1 = computador('hp','8g','nvidia')
computador_1.turnon()
computador_1.turnoff()
computador_1.showconfig()    

#i have to pass the arguments in order to see them whern i run the file
'''
#this things as call instancias
computador_1 = computador('hp','8g','nvidia')
computador_2 = computador('lenovo', '16g','nvidiaxpto')
computador_3 = computador('msi', '32g','nvidiaptox')
print(computador_1.marca,computador_1.memoria_ram, computador_1.placa_grafica)
print(computador_2.marca,computador_2.memoria_ram, computador_2.placa_grafica)
print(computador_3.marca,computador_3.memoria_ram, computador_3.placa_grafica)'''

        

