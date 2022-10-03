'''essentials

classes & bjects
constructor / initializar (__init__)
create classand bject attributes
acessing class / object attributes
changing class / objects attributes
methods
__name__ & __main__
9.create objects
print objects/class attributes
10. access class attributes and object attributes
11. changing object / class attributes

'''

'''
# class construct and object -  definição de um objecto,  como é um objecto deve de parecer e como é que ele se deve de comportar  
 vai descrever um objecto



 class: 
        - a car with 4 wheels,  5 seat capacity and 4 or 2 doors

object:
    - built based on the definition 

real world object -  car
    -  attriutes / properties
    - actions
attributes / properties
    - 4 wheels
    - 5 seatting capacity
    - 4 or 2 doors
Actions
    - start enginer
    - move/ acceleate
    -  stop engine
    - etc
'''

# class definition


class Car:
    #class attributes / variables
    # functions within a class is call a METHOD

#class attribute - it's going to be the same for every object bellow
    no_of_tires = 4

    #class constructor/initializer (method with a special name)
    def __init__(self, make, model, year, color, moon_roof=False) -> None:
    #object attributes/variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        #no caso de nao passar nada neste atributoso default é oqu está no parametro do init,  False
        self.moon_roof = moon_roof
        self.engine_running = False

# __init__ arguments


#methods
    def start_the_engine(self):
        self.engine_running =  True

    def stop_the_engine(self):
        self.engine_running =  False

#outside the class
def main():
    print('hello from the main() method!')
    #9.create objects_here is where we are going to create objects
    car1 = Car('ford','mustang',2010,'blue')
    car2 = Car('tesla','model 3',2020,'red',True)

    #10_access class and objects
    #access attributes  simple example
    '''
    make1 = car1.make
    print(make1)
    model1 = car1.model
    print(model1)
    '''
#10 .accessing car1 attributes
    print('Printing car1 details:'.center(50, '-'))
    print('make : {}'.format(car1.make))
    print('model : {}'.format(car1.model))
    print('year : {}'.format(car1.year))
    print('color : {}'.format(car1.color))
    print('moon Roof : {}'.format(car1.moon_roof))

#10. accessing car2 attributes / access value from object attributes
    print('Printing car1 details:'.center(50, '-'))
    print('make : {}'.format(car2.make))
    print('model : {}'.format(car2.model))
    print('year : {}'.format(car2.year))
    print('color : {}'.format(car2.color))
    print('moon Roof : {}'.format(car2.moon_roof))

#10.  Class attributes
    print('class attributes: '.center(50, '-'))
    print('car1: ',car1.no_of_tires)
    print('car2: ',car2.no_of_tires)
    print('car: ',Car.no_of_tires)

if __name__ == '__main__':
    main()



