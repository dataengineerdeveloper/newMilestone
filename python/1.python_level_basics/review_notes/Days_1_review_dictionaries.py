###################
##  Dictionaries ## 
###################

# aqui vamos ver o coceito de key e de value, sendo que o key >> name:'john'<< value


student = {'name':'luis','age':31,'courses': ['math','compsci'] }
print(student)

# 1º forma de fazer um update a um dictionaries, para add apenas passamos a variavel e colocamos  key da mesma forma que está no dictionary
student['phone'] = '555-6666'
student['name'] = 'eduardo'

# 2º forma de fzer um update

#UPDATE
student.update({'name':'santos','age':85,'phone': '999-999'})

print(student)

#supondo que precisamos de procurar um key que nao existe no dicionario, o que vai aocntecer é que vamos ter um erro.
#contudo se usar o method GET,  vamos ter o resultado de NONE,  mas se quisermos colocar uma mensagem para nao ter o NONE, colocamos logo a seguir á key que estamos a tentar encontrar
#print(student.get('phone','not found'))

# supondo que precisamos de remover um key do dictionary.

#DELETE
#del student['age']
#print(student)

#POP
#OUTRO METODO PARA REMOVER ALGUMA KEY DO DICTIONARY

#ao corrermos este print vamos ver o a key age vai ser removida do dictionary
age = student.pop('age')
print(student)
print(age)

#LEN

#SE QUISERESMOS SABER O NUMERO DE KEYS QUE TEMOS NO NOSSO DICTIONARY
print(len(student))
#ainda se quiser ver que keys sao basta fazer 
print(student.keys())
#vemos apenas os valores 
print(student.values())
#vemos as keys e values
print(student.items())


#loop through dict
for keys,values in student.items():
    print(keys, values)













