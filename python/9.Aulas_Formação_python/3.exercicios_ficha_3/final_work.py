##################################################
#        FICHA 3 - EXERCICIO 6 (TRABALHO)        #
##################################################


#importar bibliotecas

from os import system
from datetime import datetime


#FUNÇÕES:

#menu principal

def menu(dicionario):
   
    system('cls')

    print('\033[1m''                      Main Menu\n'+'\033[0m')
    print('      1.  View dictionary\n')
    print('      2.  Clear dictionary\n')
    print('      3.  Legumes\n')
    print('      4.  Frutos\n')
    print('      5.  Close app\n')

    opmenu(dicionario)


#opções do menu principal

def opmenu(dicionario):

    op = input('Enter your option: ')

    match op:

        case '1':
            print(f"\ndictionary view :\n{dicionario}\n")
            esperartecla()
            menu(dicionario)
        
        case '2':
            dicionario.clear()
            print("\nClear dictionary!")
            esperartecla()
            menu(dicionario)
        
        case '3':
            while verificardici(dicionario, "legume"):
                submenu("legume")
            
        case '4':
            while verificardici(dicionario, "fruto"):
                submenu("fruto")

        case '5':
            system('cls')
            gravarfich(construirfich(dicionario))       
            print("\nClose app!\n")

        case _:
            print("\nInvalid Option!")
            esperartecla()
            menu(dicionario)
          
            
#submenus

def submenu(tipo):
    
    system('cls')

    print(f'\033[1m'+f'                 Submenu {tipo.upper()}S\n'+'\033[0m')
    print(f'      1.  List {tipo}s\n')
    print(f'      2.  Remove {tipo}\n')
    print(f'      3.  Add new {tipo}\n')
    print(f'      4.  Edit type {tipo}\n')
    print(f'      5.  Previous menu\n')

    opsubmenu(tipo)


#opções dos submenus

def opsubmenu(tipo):
    
    op = input('Enter your option: ')

    match op:

        case '1':
            print(f"\nOs {tipo}s constantes do dicionário são:\n")
            listar(tipo)
            esperartecla()
            submenu(tipo)
        
        case '2':
            print(f"O {tipo} «{remover(tipo)}» foi removido!")
            esperartecla()
            submenu(tipo)
        
        case '3':
            print(f"O {tipo} «{adicionar(tipo)}» foi adicionado!")
            esperartecla()
            submenu(tipo)            

        case '4':
            escolha1,escolha2 = editar(tipo)
            print(f"O {tipo} «{escolha1}» foi editado para «{escolha2}»!")
            esperartecla()
            submenu(tipo) 
            
        case '5':
            system('cls')
            menu(dicionario)     

        case _:
            print("Opção inválida!")
            esperartecla()
            submenu(tipo)
  
    
#listar por tipo

def listar(tipo):
    
    for item in dicionario.items():
        if item[0] == tipo:
            print(item[1])
            
    print('\n')    
  
  
#remover por tipo

def remover(tipo):
    
    escolha = 0
    while escolha not in dicionario[tipo]:
        escolha = input(f'\nIntroduza o {tipo} a remover: ').lower()
    
    for indice, item in enumerate (dicionario[tipo]):
        if item == escolha:
            dicionario[tipo].remove(dicionario[tipo][indice])
            
    return(escolha)
        
    
#adicionar por tipo

def adicionar(tipo):
    
    escolha = ''
    while escolha == '':
        escolha = input(f'\nIntroduza o {tipo} a adicionar: ').lower()

    while escolha in dicionario[tipo]:
        escolha = input(f"\nO {tipo} «{escolha}» já existe no dicionário.\nIntroduza um outro {tipo}: ")

    dicionario[tipo].append(escolha)
    return(escolha)
            
       
#editar por tipo
        
def editar(tipo):
    
    escolha1 = 0
    while escolha1 not in dicionario[tipo]:
        escolha1 = input(f'\nIntroduza o {tipo} a editar: ').lower()
    
    escolha2 = ''
    while escolha2 =='':
        escolha2 = input(f'\nIntroduza o nome que irá editar o {tipo} {escolha1}: ').lower()    
        
    for indice, item in enumerate (dicionario[tipo]):
        if item == escolha1:
            dicionario[tipo][indice] = escolha2
            
    return(escolha1,escolha2)   
           

#construir novo conteúdo para gravar ficheiro

def construirfich(dicionario):

    ncont = []

    for chave in dicionario:
        for item in range (len(dicionario[chave])):
            ncont.append(chave)
            ncont.append(',')
            ncont.append(dicionario[chave][item])
            ncont.append('\n')

    return ncont


#gravar novo conteúdo num ficheiro com nome, data e hora

def gravarfich(ncont):

    data_e_hora = datetime.now().strftime('%d-%m-%Y %Hh%M')

    datahora = data_e_hora.split(' ')

    nomefich = str('frutos_legumes_'+(datahora[0])+'_'+(datahora[1])+'.txt')

    try:
        
        fich = open(nomefich, 'w', encoding='UTF-8-SIG')
        fich.writelines(ncont)
        fich.close()
        print(f"Ficheiro gravado com o nome: {nomefich}")

    except:
        
        print("Erro ao gravar ficheiro!")


#esperar entrada de teclado

def esperartecla():
    
    input("\nPrima a tecla «Enter» para continuar.")


#verificar existência de chaves no dicionário

def verificardici(dicionario, tipo):

    try:
        if len(dicionario[tipo])>0:
            return True
    except:
        print(f"\nO dicionário não contem {tipo}s. Escolha outra opção.\n")
        esperartecla()
        menu(dicionario)


#PROGRAMA PRINCIPAL:

#importar dados do ficheiro

try:
    
    fich = open('trabalho.txt', 'r', encoding='UTF-8-SIG')
    count = fich.readlines()
    fich.close()

except:
    
    print("Erro ao abrir ficheiro!")


#construir dicionário

dicionario = {}

for dados in count:
    item = dados.split(',') 
    tipo = item[0]
    nome = item[1].replace('\n','')
    
    if tipo not in dicionario:
        dicionario[tipo] = [nome]
    else:
        dicionario[tipo] = dicionario[tipo] + [nome]
 

#apresentar o menu principal

menu(dicionario)

##################################################