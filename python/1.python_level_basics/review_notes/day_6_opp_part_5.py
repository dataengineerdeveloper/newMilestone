'''
things that i'll learn

1. destructor
2. punlic & private access modifier
3. getter & setter methods
4.getter & setter properties

'''


# destructor,  isto tem de ser criar como function de forma a que execute com sucesso

class Car:
    #class attributes / variables
    no_of_tires =  4
    #class constructor /initializer(methods with a special name)
    def __init__(self,make,model,year,color,moon_roof= False):
        #object atrributes / varibles
        self.make = make
        self.model = model
        self.year = year
        self.color =  color
        self.moon_roof =  moon_roof
        self.engine_runnning =  False
    #methods
    def start_the_engine(self):
        self. engine_running = True
    
    def stop_engine_running(self):
        self.engine_running = False

#destructor
    def __del__ (self):
        #caso nao acrescentarmos mais nda vamos ter este print duas vezes, que é referente a  car1 e car2
        #ao usarmos os argv vamos ber quais foram os attributos que forma apagados, atraves do make e do model
        print('{} {} destructor invoked'.format(self.make,self.model))

def main():
    print("hello from the main() method!")
    car1 = Car('ford', 'mustang', 2010, 'blue', True)
    car2 = Car('tesla', 'model 3', 2021, 'red', True)

    #accessing car1 attributes

    print('print car1 details:'.center(50, '-'))
    print('make : {}'.format(car1.make))
    print('model : {}'.format(car1.model))
    print('year : {}'.format(car1.year))
    print('color : {}'.format(car1.color))
    print('moon_roof : {}'.format(car1.moon_roof))


    #accessing car2 attributes
    print('print car2 details:'.center(50, '-'))
    print('make : {}'.format(car2.make))
    print('model : {}'.format(car2.model))
    print('year : {}'.format(car2.year))
    print('color : {}'.format(car2.color))
    print('moon_roof : {}'.format(car2.moon_roof))

    #Class attributes

    print('Class Attributes:'.center(50, '-'))
    print('car1:',car1.no_of_tires)
    print('car2:',car2.no_of_tires)
    print('Car:',Car.no_of_tires)

    #11.  destructor = delete
    print('deleting objects'.center(50, '-'))
    del car1
    del car2

if __name__ == '__main__':
    main()
