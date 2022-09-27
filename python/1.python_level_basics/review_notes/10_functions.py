'''
com uma  functions basicmanete podemos usar a logica para varias variaveis,
não tendo a necessidade de criar a logica multiplas vezes

como começarmos uma functions a unica coisa que temos de fazer é começar com
def


'''



'''
1.
inicii da funcçao mas de deixar apenas a funcção com está não vai acontecer nada
relativamente ás duas logicas uqe foram criadas para age,  age2.

>>>> run_code_example_1

age = 18
age2 = 15

if age2 < 18:
    print('opps not an adult')
else:
    print('yes, its an adult')

2. 
Vamos apagar as duas logicas criadas para fazer o check da age, e ag2 e vamos colocar por de baixo da
functions = def a logica
'''
''''
>>>>run_code_example_2
age = 18
age2 = 15


def check_age ():
        if age < 18:
            print('opps not an adult')
        else:
            print('yes, its an adult')

check_age()
'''
'''
3. 
podemos ainda fazerduas coisa como colocar um parametro dentro da faunctions

def check_age(age)

e no fim da logica indicarmos que parametro é que queremos que seja validado

'''
'''
>>>> run_code_example_3

age = 18
age2 = 15


def check_age (age):
        if age < 18:
            print('opps not an adult')
        else:
            print('yes, its an adult')

check_age(age)
check_age(age2)

'''

'''
4.
    vamos suport que desta vez nao tinhamos nenhuma variaveis, podemos colocar no fim
    check_age() um valor

    no caso de nao passarmos nada o que nos vai dizer é que a variavel nao esta definida


O resultado deste comando vai ser basicamente a indicação de 3 resultado,  neste caso se é ou nao adulto
'''

def check_age (age):
        if age < 18:
            print('opps not an adult')
        else:
            print('yes, its an adult')

check_age(18)
check_age(17)
check_age(99)
