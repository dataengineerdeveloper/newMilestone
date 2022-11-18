from os import system
from datetime import datetime


def menu(dicionario):
   
    system('cls')

    print('\033[1m''                      MENU\n'+'\033[0m')
    print('      1.  Ver dicionario\n')
    print('      2.  Limpar dicionário\n')
    print('      3.  Categoria Legumes\n')
    print('      4.  Categoria Frutos\n')
    print('      5.  Fechar aplicação\n')

    opmenu(dicionario)



def opmenu(dicionario):

    opcao = input('Inserir opção: ')

    if opcao == '1':
            print(f"\nDados do dicionário:\n{dicionario}\n")
            aguardar()
            menu(dicionario)
        
    if opcao == '2':
            dicionario.clear()
            print("\nDicionário limpo!")
            aguardar()
            menu(dicionario)
        
    if opcao == '3':
            while verificardici(dicionario, "legume"):
                submenu("legume")
            
    if opcao == '4':
            while verificardici(dicionario, "fruto"):
                submenu("fruto")

    if opcao == '5':
            system('cls')
            gravarfich(construirfich(dicionario))       
            print("\nAplicação fechada!\n")

    else:
            print("\nTente novamente!")
            aguardar()
            menu(dicionario)
          

def submenu(tipo):
    
    system('cls')

    print(f'\033[1m'+f'                 SUBMENU {tipo.upper()}S\n'+'\033[0m')
    print(f'      1.  Listar {tipo}s\n')
    print(f'      2.  Remover {tipo}\n')
    print(f'      3.  Adicionar novo {tipo}\n')
    print(f'      4.  Editar nome de {tipo}\n')
    print(f'      5.  Menu anterior\n')

    opsubmenu(tipo)


def opsubmenu(tipo):
    
    opcao = input('Inserir opção: ')

    

    if opcao == '1':
            print(f"\nOs {tipo}s elementos dos dicionário :\n")
            listar(tipo)
            aguardar()
            submenu(tipo)
        
    if opcao == '2':
            print(f"O {tipo} «{remover(tipo)}» foi removido")
            aguardar()
            submenu(tipo)
        
    if opcao == '3':
            print(f"O {tipo} «{adicionar(tipo)}» foi adicionado")
            aguardar()
            submenu(tipo)            

    if opcao == '4':
            escolha1,escolha2 = editar(tipo)
            print(f"O {tipo} «{escolha1}» foi alterada para «{escolha2}»!")
            aguardar()
            submenu(tipo) 
            
    if opcao == '5':
            system('cls')
            menu(dicionario)     

    else:
            print("Tente novamente!")
            aguardar()
            submenu(tipo)

def listar(tipo):
    
    for item in dicionario.items():
        if item[0] == tipo:
            print(item[1])
            
    print('\n')    


def remover(tipo):
    
    escolha = 0
    while escolha not in dicionario[tipo]:
        escolha = input(f'\nIntroduza o {tipo} a remover: ').lower()
    
    for indice, item in enumerate (dicionario[tipo]):
        if item == escolha:
            dicionario[tipo].remove(dicionario[tipo][indice])
            
    return(escolha)

def adicionar(tipo):
    
    escolha = ''
    while escolha == '':
        escolha = input(f'\nIntroduza o {tipo} a adicionar: ').lower()

    while escolha in dicionario[tipo]:
        escolha = input(f"\nO {tipo} «{escolha}» já existe no dicionário.\nInserir outro {tipo}: ")

    dicionario[tipo].append(escolha)
    return(escolha)
            

        
def editar(tipo):
    
    escolha1 = 0
    while escolha1 not in dicionario[tipo]:
        escolha1 = input(f'\nIntroduza o {tipo} a editar: ').lower()
    
    escolha2 = ''
    while escolha2 =='':
        escolha2 = input(f'\nInserir o nome a alterar {tipo} {escolha1}: ').lower()    
        
    for indice, item in enumerate (dicionario[tipo]):
        if item == escolha1:
            dicionario[tipo][indice] = escolha2
            
    return(escolha1,escolha2)   
           
def construirfich(dicionario):

    ncont = []

    for chave in dicionario:
        for item in range (len(dicionario[chave])):
            ncont.append(chave)
            ncont.append(',')
            ncont.append(dicionario[chave][item])
            ncont.append('\n')

    return ncont

def gravarfich(ncont):

    data_e_hora = datetime.now().strftime('%d-%m-%Y %Hh%M')

    datahora = data_e_hora.split(' ')

    nomefich = str('frutos_legumes_'+(datahora[0])+'_'+(datahora[1])+'.txt')

    try:
        
        fich = open(nomefich, 'w', encoding='UTF-8-SIG')
        fich.writelines(ncont)
        fich.close()
        print(f"Ficheiro salvo: {nomefich}")

    except:
        
        print("Erro a salvar!")


def aguardar():
    
    input("\nPrima «Enter» para continuar.")



def verificardici(dicionario, tipo):

    try:
        if len(dicionario[tipo])>0:
            return True
    except:
        print(f"\nO dicionário contem {tipo}s. Escolhe outra opção.\n")
        aguardar()
        menu(dicionario)

try:
    
    fich = open('trabalho.txt', 'r', encoding='UTF-8-SIG')
    cont = fich.readlines()
    fich.close()

except:
    
    print("Erro ao abrir!")


dicionario = {}

for dados in cont:
    item = dados.split(',') 
    tipo = item[0]
    nome = item[1].replace('\n','')
    
    if tipo not in dicionario:
        dicionario[tipo] = [nome]
    else:
        dicionario[tipo] = dicionario[tipo] + [nome]
 


menu(dicionario)

