# exercices let create a class for employee where we'll have
# a class will work as a 'blueprint' and each employee will be a instance
# imagine that you need to leave a class empty without any parameter or functions just use 'pass' then you 'll skip the error
class Employee:
 
    num_of_emps = 0
    raise_amount = 1.04

#method_1 // __init__ =  initialize 
    def __init__(self,first, last, pay):
        #instances variables
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@company.com'
        
            Employee.num_of_emps =+ 1

#another method where we are going to use self instead of emp_1 or emp_2
#method_2
    def fullname(self):
# here we want to format first last 'Luis Nogueira'
            return '{} {}'.format(self.first, self.last) 

    def apply_raise(self):
        #     self.pay = int(self.pay * 1.05)
             self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee ('Luis', 'Nogueira', 500)
emp_2 = Employee ('jorge', 'Nogueira', 6000)

print(Employee.num_of_emps)



# print(emp_1.fullname())
# print(emp_1.pay)

# print(emp_1.raise_amount)
#when we need to know all data in a row
# print(emp_1.__dict__)
# print(Employee.__dict__)

# print(Employee.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.fullname(emp_1))
# print(emp_1.apply_raise)



