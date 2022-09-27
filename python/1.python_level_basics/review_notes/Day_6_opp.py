 '''
essentials

classes & bjects
constructor / initializar (__init__)
create classand bject attributes
acessing class / object attributes
changing class / objects attributes
methods
__name__ & __main__

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

if __name__ == '__main__':
    main()



