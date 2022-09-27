##################
## CONDITIONALS ##
##################


## 1 exemplo
'''
language = 'sql'

if language == 'python':
    print('language is correct, python')
elif language == 'java':
    print('language is java')
elif language in ('sql','swift'):
    print('might be sql or swift')
else:
    print('no match')
'''

# 2 exemplo

#AND
user =  'admin'
#esta variavel vai servir para validar o se o sujeito pode aceder á pagina,  se a variavel tiver a false,  vais dar 'wrong access'
logged_in = True

if user == 'admin' and logged_in:
    print('admin page')
else:
    print('wrong access')


#OR
user =  'admin'
#esta variavel vai servir para validar o se o sujeito pode aceder á pagina,  se a variavel tiver a false,  vais dar 'wrong access'
logged_in = False
# se usar o OR vai satisfazer pelo menos uma das condições
if user == 'admin' or logged_in:
    print('admin page')
else:
    print('wrong access')


# aqui pode ser um bocado confuso, mas vamos ver da seguinte forma,  IF NOT False
user = 'admin'
logged_in = False
if not logged_in:
    print('please login')
else:
    print('welcome')


c = [1,2,3]
d = [1,2,3]

#Vai ser True
print(c == d)
#vai dar false,  por A e B são considerados diferentes objectos em memoria
#a forma como temos para validar isso é procurar pelo id de cada variavel
print(c is d)
print(id(c))
print(id(d))

#mas se dissermos que a = b aqui vamos conseguir contornar
c = [1,2,3]
d = 1
print(c == d)
print(c is d)
print(id(c) == id(c))



#isto aqui serve pra validar o que pode ser considerado como True e comoo False, podemo testar (none, 0, 1 (),[], {}, 10), de forma  aperceber o que pode ser considerado como False e Teue

condition = 'test'

if condition:
    print('evaluated to True')
else:
    print('Evaluated to False')


#small program to insert week day and return name of the weekday

#1 program
dia = int(input('Insert Week day: '))

if dia == 1:
    print('Monday')
elif dia == 2:
    print('Thuesday')
elif dia == 3:
    print('wendsday')
elif dia == 4:
    print('Thrusday')
elif dia == 5:
    print('Friday')
elif dia == 6:
    print('Saturday')
elif dia == 7:
    print('Sunday')
else:
    print('wrong value')

#2 program

num = int(input('insert your value: '))

if num < 15:
    print('your value is bellow 15')
elif num < 20:
    print('your value is bellow 20')
else:
    print('other value')


# 3 program

value_1 = int(input('insert your 1 value:'))
value_2 = int(input('insert your 2 value:'))
value_3 = int(input('insert your 3 value:'))

if value_1 >= value_2 >= value_3:
    print(value_1,value_2,value_3)
elif value_1 >= value_3 >= value_2:
    print (value_1,value_3,value_2)
elif value_2 >= value_1 >= value_3:
    print(value_2,value_1,value_3)
elif value_2 >= value_3 >= value_1:
    print(value_2,value_3,value_1)
elif value_3 >= value_1 >= value_2:
    print(value_3,value_1,value_2)
else:
    print(value_3,value_2,value_1)


'''
Execise

simulate a ATM 
user must insert the value that he needs do withdral and after that the user will know thw amount 
of billing he's going to receive.  there's only available 1, 5, 10, 50, 100 dollars.

minumun value 10 dollars and maximun value 600 dollars

test 1:  withdral 256 (2*100 // 50 // 5 // 1)
test 2:  withdral 399 (3*100 // 50 // 4*5 // 4*1)

'''

ATM_Value = int(input('How much money you need?: '))

if 10 <= ATM_Value <=600:
    billing_100 = ATM_Value // 100
    ATM_Value = ATM_Value % 100

    billing_50 = ATM_Value // 50
    ATM_Value = ATM_Value % 50

    billing_10 = ATM_Value // 10
    ATM_Value = ATM_Value % 10

    billing_5 = ATM_Value // 5
    ATM_Value = ATM_Value % 5
    
    billing_1 = ATM_Value // 1

# difference between elif vs if in the previous exercise i use elif because the variables were related throught the conditional,  however when i used if it is beacusa all variabels are different to valiadate

    if billing_100 > 0:
        print(billing_100,'bill of 100 dollar')
    if billing_50 > 0:
        print(billing_50,'bill of 50 dollar')
    if billing_10 > 0:
        print(billing_10,'bill of 10 dollar')
    if billing_5 > 0:
        print(billing_5,'bill of 5 dollar')
    if billing_1 > 0:
        print(billing_1,'bill of 1 dollar')
else:
        print('there''s no money')



