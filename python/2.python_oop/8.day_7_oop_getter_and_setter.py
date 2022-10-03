class Employee:
    # este é a forma comoo criamos uma propriedade como rad-only,  desta forma pode ser usada por multiplos objectos
    __bonus_percentage = 0.20

    # Class Constructor (Method with a special name)
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__base_annual_salary = 0


    # Methods
    def get_monthly_gross(self):
        return self.__base_annual_salary / 12

    def get_standard_annual_bonus_amount(self):
        return self.__base_annual_salary * self.__bonus_percentage
#getter - getting value from a private variable usamos a @
    @property
    def base_annual_salary(self):
        return self.__base_annual_salary

    @property
    def bonus_percentage(self):
        return self.__bonus_percentage
#setter
    #base_anual_salary vem do metodo anterior
    @base_annual_salary.setter
    def base_annual_salary(self, base_annual_salary):
        if 45000.00 <= base_annual_salary <= 120000.00:
            self.__base_annual_salary = base_annual_salary
        else:
            print("Annual base salary must be between 45k and 120k!")


def main():
    employee1 = Employee("Kara", "Smith")
    employee1.base_annual_salary = 50000.00

    monthly_gross_pay = employee1.get_monthly_gross()
    standard_annual_bonus = employee1.get_standard_annual_bonus_amount()

#aqui qunado vejo {:.2f}  tem a ver com a formatação de float
    print("Annual Salary : {:.2f}".format(employee1.base_annual_salary))
    print("Monthly Gross Salary : {:.2f}".format(monthly_gross_pay))
    print("Annual Standard Bonus : {:.2f}".format(standard_annual_bonus))


if __name__ == '__main__':
    main()