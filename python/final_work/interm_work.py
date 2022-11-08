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

    print('\033[1m''                      MENU\n'+'\033[0m')
    print('      1.  Visualizar conteúdo do dicionário\n')
    print('      2.  Limpar dicionário\n')
    print('      3.  Legumes\n')
    print('      4.  Frutos\n')
    print('      5.  Terminar aplicação\n')

    opmenu(dicionario)


#opções do menu principal

def opmenu(dicionario):

    op = input('Introduza a opção pretendida: ')

    if op == '1':
            print(f"\nO conteúdo do dicionário é:\n{dicionario}\n")
            esperartecla()
            menu(dicionario)
        
    if op == '2':
            dicionario.clear()
            print("\nDicionário limpo!")
            esperartecla()
            menu(dicionario)
        
    if op == '3':
            while verificardici(dicionario, "legume"):
                submenu("legume")
            
    if op == '4':
            while verificardici(dicionario, "fruto"):
                submenu("fruto")

    if op == '5':
            system('cls')
            gravarfich(construirfich(dicionario))       
            print("\nAplicação terminada!\n")

    else:
            print("\nOpção inválida!")
            esperartecla()
            menu(dicionario)
          
            
#submenus

def submenu(tipo):
    
    system('cls')

    print(f'\033[1m'+f'                 SUBMENU {tipo.upper()}S\n'+'\033[0m')
    print(f'      1.  Listar {tipo}s\n')
    print(f'      2.  Remover {tipo}\n')
    print(f'      3.  Adicionar novo {tipo}\n')
    print(f'      4.  Editar nome de {tipo}\n')
    print(f'      5.  Menu anterior\n')

    opsubmenu(tipo)


#opções dos submenus

def opsubmenu(tipo):
    
    op = input('Introduza a opção pretendida: ')

    

    if op == '1':
            print(f"\nOs {tipo}s constantes do dicionário são:\n")
            listar(tipo)
            esperartecla()
            submenu(tipo)
        
    if op == '2':
            print(f"O {tipo} «{remover(tipo)}» foi removido!")
            esperartecla()
            submenu(tipo)
        
    if op == '3':
            print(f"O {tipo} «{adicionar(tipo)}» foi adicionado!")
            esperartecla()
            submenu(tipo)            

    if op == '4':
            escolha1,escolha2 = editar(tipo)
            print(f"O {tipo} «{escolha1}» foi editado para «{escolha2}»!")
            esperartecla()
            submenu(tipo) 
            
    if op == '5':
            system('cls')
            menu(dicionario)     

    else:
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
    cont = fich.readlines()
    fich.close()

except:
    
    print("Erro ao abrir ficheiro!")


#construir dicionário

dicionario = {}

for dados in cont:
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