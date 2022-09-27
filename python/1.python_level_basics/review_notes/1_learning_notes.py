##########################################
####        PYTHON -  CHEAT SHEET     ####
##########################################

#Sempre que for necessário pedir ao utilizador para inseriro alguma valor basta apenas de colocar o input('')

##################
####INPUT
##################


name = input('como te chamas?')
print('hello ' + name)

#######################
## #VARAIVEIS
######################

name = 'julia'
age = 12
new_var = 3.14
list_of_cars= ['bmw','volvo']

# ASSINALATUDO QUE ETSÁ DENTRO DO DICIONARIO
print(list_of_cars)

#CONSEGUIMOS VER QUAL O TIPO DE DADOS
print(type(name))

#VEMOS QUE QUEREMOS TRAZER O INDEX 0,  QUE NESTE CASO DE ACORDO COM A LISTA NA VARIABLE É O BMW
print('hello my car is ' + list_of_cars[0])
# neste exemplo imaginaemos que quero juntar um string com um int,  nao consigo fazer a concatenação de forma direta
# a unica forma é convert o que está na variavel para string e ai ja vou conseguir
print('my age is ' + str(age))


#######################
## string functions
######################

##conceitos como concatename variaveis // len()  // upper. // lower.  // capitalize.

first_name='luis '
last_name ='nogueira'

full_name = first_name.capitalize()+last_name.upper()
print(full_name)  
print(len(first_name))
print(len(last_name))
##aqui vamos usar o endswith,  para validar se o que vem no fim full_name é 'hello', o output é False
print(full_name.endswith('hello'))