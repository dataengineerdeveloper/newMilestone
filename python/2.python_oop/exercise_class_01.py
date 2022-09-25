#create class car

class car():
    def __init__(self,brand, colour, year)->str:
        self.brand = brand
        self.colour = colour
        self.year = year
    
    def turnonCar(self):
        print('start car')
        
    def turnoffCar(self):
        print('trun off car')
    
    def showcaracteristics(self):
        print(self.brand,self.colour,self.year)
    
car1=car('bmw','black','2020')
car1.turnonCar()
car1.turnoffCar()
car1.showcaracteristics()
        
    
        