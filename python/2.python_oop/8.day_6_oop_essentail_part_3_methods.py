#using methods

class my_calc:
    #class constructor/initializer (nethod with a special name)
    def __init__(self,num1, num2) -> None:
        #object attributes/variables
        self.num1 = num1
        self.num2 = num2

    # methods
    def total(self):
        return self.num1 + self.num2

    def diff(self):
        return self.num1 - self.num2

def main(): 
    print('hello from the main() method!')
    #valores a entrarem a class
    calc1 = my_calc(10,20)
    #nome da variavel anterior.total dos metodos dentro da class neste caso,  total e diff
    total1 = calc1.total()
    diff1 = calc1.diff()
    print('total: ',total1)
    print('diff1: ',diff1)

    print('------------------')
    #calculo numero 2
    calc2 = my_calc(5,25)
    total2 = calc2.total()
    diff2 = calc2.diff()
    print('total: ',total2)
    print('diff1: ',diff2)

if __name__ == '__main__':
    main()