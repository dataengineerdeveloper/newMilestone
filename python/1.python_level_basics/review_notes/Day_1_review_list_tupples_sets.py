#list -  vamos ver []
#tuple -  bvamos ver ()
#set - vamos ver {}



#LISTS

#courses = ['mat','port','ingles']


#FUNCTIONS

# append -  faz o insert de um novo dado
#courses.append('music')

# insert  - server para fazermos o novo insert e indicarmos a posicao onde vai ficar o novo insert
#courses.insert(0,'music')

''' extend -  por exemplo,  supondo que temos duas listas e que queremos usar o extend para colocar
uma lista dentro de outra lista

courses_2 = ['compscience','calculus']
courses.extend(courses_2)
print(courses)

Neste caso conseguimos colocar uma lista dentro de outra lista

'''
# remove - supondo que precisamos de remover alguma string dentro desta lista, aqui
#vamos ver que vao desaparecer o 'mat'

#courses.remove('mat')
#print(courses)


#pop -  vai apagar o ultimo elemento da lista

#popped =  courses.pop()

#print(popped)
#print(courses)

#ou seja vamos ver que o elemento que vai saltar, será ingles


# reverse -  revertemos a ordem da lista,  sendo que o ingles passa a ser o primeiro elemento

#courses = ['mat','port','ingles']
#courses.reverse()
#print(courses)


#sort -  pode fazer sentido para o caso onrganizar a lista por ordem alfabetica

#ex1:  imaginemos que queremos colocar de forma ascendente o numero dentro de uma lista, podemos usar o sort
#ex2:  agora vamos colocar o nos numeros de forma descendente:  podemos usar o sort.reverse // .sort(reverse=true)

courses = ['mat','port','ingles']
num = [2,5,8,8,9,4,7,78]
courses.sort()
courses.sort(reverse=False)
#order nos numero de forma ascente
##>>>num.sort()
#ordenar os numero de forma descendente
##>>>num.sort(reverse=True)
print(courses)
print(num)
print(max(num))
print(sum(num))
print(courses.index('ingles'))


#Quando precisamos de confirmar um valor para vermos se esse valor é true ou false
print('mat'in courses)
#>>>input result: True


# criamos um for loop para que o nosso codigo va inumerando elemento dentro da lista

for item in courses:
    print(item)


# enumerator -  supondo que preciso que para alem da lista de elementos dentro da lista quero que seja apresentada o index

#for index, course in enumerate(courses):
 #   print(index, course)

#supondo que queremos começar a iteração num index especifico

for index, course in enumerate(courses, start=0):
    print(index, course)


course_str = ' - '.join(courses)
print(course_str)




courses[0] = 'Art'
print(courses)



#MUTAVEL - este exemplo mostra que esta lista é mutavel.  ouse ja tudo que seja alterado ma list_1 vai ser alterado tb na lsit_2

list_1 = ['a','b','c','d']
list_2 = list_1

# vaos alterar o index 0 por y
list_1[0] = 'y'

print(list_1)
print(list_2)


#TUPLES

''' IMUTAVEL -  aqui é a  grande diferencia entre usar um dicionario/lista ou um tuple. se corrermos o que este codigo vai bater,
porque no caso dos tuples nao conseguimos fazer alteraçoes, tal comonas lista
'''

tuple_1=('a','b','c','d')
tuple_2 = tuple_1


print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'y'

print(tuple_1)
print(tuple_2)



# SETS

#um dos usas dos set, é que os duplicados sao removidos +  a ordem num set não importa, até, porque se corrermos várias vezes nunca vamos ter a mesma ordemw

SET_1 = {'a','b','c','d','a'}
SET_2 =  {'a','b','d','a','t'}
print(SET_1)
#vai dar false, porque nao está a no set
print('t' in SET_1)
#valida se existem valores iguais
print(SET_1.intersection(SET_2))


#difference > apresenta todas as diferenças qu existem entre um set e o outro
print(SET_1.difference(SET_2))



#union
print(SET_1.union(SET_2))


#empty lists

empty_list = []
empty_list = list()