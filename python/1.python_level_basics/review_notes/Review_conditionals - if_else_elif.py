#if elif, else 

language =  'sql'

if language == 'python':
    print('a linguagem é python')
elif language == 'java':
    print('a linguagem é Java')
elif language == 'sql':
    print('a linguagem é sql')
else:
    print('Condição falsa')



    # por exemplo,  object identification normalmente usamos o IS , que pode gerar confusao com o ==

a = [1,2]
b = [1,2] 
print(a==b)
    #>>true,  são objetos iguais
print(a is b)
    #>>false , isto porque me memoria sao objetos distintos.este é o conceito de objecto identity,  fizer o id de cada um dos objetos vamos ver que sao diferentes

print(id(a))
#>>>2500244979072
print(id(b))
#>>>2500248227072

# um forma de contornar o A ser igual a B, na variavel temos de indicar que a==b e depois podemos fazer um double check e fazer um print(a==b)>>> TRUE

'''
a = [1,2,3]
b = a

print(id(a))
print(id(b))
print(a==b)
print(id(a) == id(b))
'''

#if statement

h = int(input('value to check: '))

if h > 50:
    print("gretaer than 50")
elif h > 20:
    print('less than 20')
elif h == 51:
    print('exact value')
else:
    print('betwwn 20 and 50')


#while statement
'''
import time as t

n = 1
while True:
    print(n)
    n = n+1
    t.sleep(0.5)
'''

# for

value = int(input('insert the value: '))
print('this',value,'will be multipled by 10')
for count in range (1,11):
    print(value,'x',count,'=',value*count)


