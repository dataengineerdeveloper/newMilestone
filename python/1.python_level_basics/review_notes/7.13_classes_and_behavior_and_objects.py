
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
        '''vamos acrescentar mais 2 behaviors,  lembrando que começar sempre por def tal como as functions'''

    '''1. behavior'''

    def walk(self):
                print(self.name + ' is walking...')

    '''2. behavior'''

    def speak(self):
                 print('hello my name is ' + self.name + ' and i am ' + str(self.age) + ' years old')


'''agora vamos invocar as functions/ behavior que acabamos de criar como tal termod e colocar o nome john ou mariam e colocar o behaviors seguido de ()'''
'''john é o objeto'''
john = Person('john',31)
john.speak()
john.walk()

print('-----------------------------------------')
'''Mariam é o objeto'''
mariam = Person('Maraim', 18)
mariam.speak()
mariam.walk()