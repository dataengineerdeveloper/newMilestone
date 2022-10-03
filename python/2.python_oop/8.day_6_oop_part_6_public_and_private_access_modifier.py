#public & public access modifier

class emplyoee:

    #classconstructor(methof with a special name)
    def __init__(self,first_name, last_name, base_anual_salary,bonus_percentage):
        self.first_name = first_name
        self.last_name = last_name
        self.base_anual_salary = base_anual_salary
        #self.bonus_percentage = bonus_percentage
        #unica forma de tornar a funcção definida na class escrondida é aplicar o __bonus_percentage, oqeu vai fazer é que mesmo que tente alterar nas funcções fora da class o valor vai ser sempre o que esá na class
        self.__bonus_percentage = bonus_percentage
    
    #methods

    def  get_monthly_gross(self):
        return self.base_anual_salary / 12

    def get_standard_anual_bonus_amount(self):
        return self.base_anual_salary * (self.__bonus_percentage/100)

    #para termos um methods hide, basta colocar o duplo underscore __
    def __get_employee_id(self):
        first_name = self.first_name
        return '111-222-333'

    def get_empid (self):
        first_name = self.first_name
        return self.__get_employee_id()
        
def main():
    print('hello from main()!')

    employee1 =  emplyoee('luis',  'nogueira', 100000.00,10)
    monthly_gross_pay =  employee1.get_monthly_gross()
    #mesmo que tente colocar o mesmo nome da variavel apra mudar o nome nao vou conseguir,  vai manter na mesma o valor 10
    employee1.__bonus_percentage = 25
    standard_anual_bonus =  employee1.get_standard_anual_bonus_amount()
    #add empid
    empid = employee1.get_empid()

#aqui qunado vejo {:.2f}  tem a ver com a formatação de float
    #add empid
    print('Emp ID : {}'.format(empid))
    print('Anual salary : {:.2f}'.format(employee1.base_anual_salary))
    print('monthly gross salary : {:.2f}'.format(monthly_gross_pay))
    print('Anual standard bonus : {:.2f}'.format(standard_anual_bonus))

if __name__ == '__main__':
    main()