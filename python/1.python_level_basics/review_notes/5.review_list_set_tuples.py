
######################
##       LISTS      ##
######################

#built-in functions to use on list

course = ['b','a','c']

#REMOVE
#remover um elemento da lista em especifico
#course.remove('c')

#POP
#supondo que quer remover o ultimo campoda lista,  mas que nao sei qual é
#course.pop()

#supondo que para alem de remover o ultimo elemento eu quero ver qual é o elemento, crio uma veriavel popped para ver
#popped = course.pop()
#print(popped)
#print(course)

nums= [1,2,3,4]

#SORT ELEMENTOS
#aqui dos exemplos se precisar de ordernar os valores da lista sendo numeros ou strings, posso usar o sort

#course.sort()
#nums.sort()

#REVERSE = TRUE
#a outra opção é fazer o reverse=true,  para ter os elementos organizadosde forma invertida

#course.sort(reverse=True)
#nums.sort(reverse=True)
#print(nums)
#print(course)

#SORTED
#existe ainda outra forma de fazer o sorted para caso de ao ter de atlerar a lista original, ouse ja vamos criar uma variavel para cnseguir ordernar os elemendos da variavel original
#sorted = sorted(course)
#print(sorted)

#MIN / MAX/ SUM
# podemos ainda aplicar agregações de valores dentro da lista
#print(min(nums))
#print(max(nums))
#print(sum(nums))

#INDEX
#para descobrir qual o index de ume elemento da lista .index('colocar o elemento que procuramos')
#print(course.index('b'))

#se quisermos validar se um elementos está dentro da list de forma a ser retornado um true or false, neste caso o exemplo vai ser FALSE

#print('d' in course)

#LOPPING

for item in course:
    print(item)

#outra forma para conseguir ter o index para os respetivos elementos,  depois do for tenho de colocar o que pretendo que o loop precorra, depois disso colcor no print

for index,item in enumerate(course):
    print(index,item)

#imaginemos que nao quero que o index comece pelo 0,  tenho de passar o segundo parametro start=1
for index,item in enumerate(course,start=1):
    print(index,item)


#JOIN  //split   >>>aqui podemos ter 2 abordagens ou usamos o join e vai fazer o join entre elementos por '-', ou então fazer  separação usando o split

course_str = '-'.join(course) 
new_list = course_str.split(' - ')

print(course_str)
print(new_list)




######################
##      TUPLES      ##
######################

#TUPLES NAO PODEM SER ALTERADOS,  ISTO É CHAMADO COMO MUTABLE AND INMUTABLE

"""
#######   MUTABLE     ########

Conceito de mutable supondo que estou ausar uma 2º variavel a dizer que a var1 = var2

se fizer um print

print(var1)
print(var2)

o resultado vai ser o mesmo. ainda assim se fizer uma alteração um dos elementos da list e correr novamente o print o a alteração vai ser refletida nas duas

var1[0] = 'art'

portanto isto indica que que sempre que seja feita alguma alteração esta é sempre refletida noutras variaveis


#######   IMMUTABLE     ########

neste caso podemos usar um tuples a unica diferença é que nao usamos [], mas sim ().

e se tentarmos usar o mesmo exemplo de  var1=var2 num tuple vai dar erro quando executarmos, porque nao permite alteraçoes






"""
######################
##      Sets        ##
######################


#par o caso de sets nao existe necessidad de ter uma ordem

cs_course = {'a','b','c'}
cs_art = {'d','a','b','i'}

print(cs_course.intersection(cs_art))
#resultado: vemos os elementos dos set que sao iguais

print(cs_course.difference(cs_art))
#resultado: unica diferencas neste csao é apenas o 'c'

print(cs_course.union(cs_art))
#resultado: vais juntar os elementos presentes nos 2 sets

#outro ponto importante para conseguirmos criar um empty list, set ou tuple
#primeira opção está errada, para cada um dos 3 temos de usar sempre a função respetiva
empty_list = []
empty_list = list()


empty_tuple = ()
empty_tuple = tuple()

empty_set = {}
empty_set = set()

















'''
### exercise review MULTIPLICACAO#####
value = int(input('place the value: '))
print('your value',value,'will be multipled by 10')
for count in range(1,11):
    print(value,'x',count,'=',value*count)

#### exercice review NUMERO INCREMENTAL###
import time as t

value =  1
while True:
    print(value)
    value = value +1
    t.sleep(0.5)

'''






