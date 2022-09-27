
'''class deve de começar sempre por maiuscula
1. a definicao de class consiste na base para qualquer objecto que possa existeir no codigo
2. Por exemplo, estabelecemos a estrutura para um objecto depois podemos criar multiplos objectos
como, o caso que vamos fazer
3.  classes sao construidas com a base de propriedades e behaviors(sao o que uma partilhar class pode fazer)
'''
class Person:
    def __init__(self,name,age):
        '''a linha 10 e 11 são propriedades da class,  ou seja sao simples atributos como vemos o name, age'''
        self.name = name
        self.age = age

'''estes sao os objetos'''
john = Person('john',31)
mariam = Person('Maraim', 18)

'''se nao fizermos a conversao de str vamos ter erro que nao é possivel concatenar str com int'''
print(john.name + ' ' +str(john.age))
print(mariam.name + ' ' +str(mariam.age))