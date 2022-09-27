#1 exercise
''''
import time as t

value = int(input('insert your value'))
while True:
    print(value)
    value = value+1
    t.sleep(0.5)
'''
#2 exercise
'''
number = int(input('insert the value to multiple: '))   
print('your value',number)
for count in range(1,11):
    print(number,'x',count,'=',number*count)
'''

#example incremetal value through the while
n = 11
count = 0
while count < n:
    print(count)
    count = count +1
    
    
n = 5
count = 0
while count< n:
    print(count)
    count= count +1
#exercise 3
#how to apply the follow operation without using **  2**3    and 2**4

base_value = int(input('insert base number: '))
exponent_value = int(input('insert your exponent number: '))

count = 0
product = 1

while count < exponent_value:
    product = product*base_value
    count = count +1

print(base_value, 'elevated',exponent_value,'=',product)



# factorial number

n = int(input('insert n: '))

prod = n
count = n-1

while count > 1:
    prod = prod*count
    count = count - 1

print(n,'! =',prod)




# other example


prod =  1
count = 2

while count <= n:
    prod = prod * count
    count = count + 1



############################
##   nested while loops   ##
############################

i = 0
n = 5

while i < n:
    j = 0
    while j < n:
        print(i,j)
        j = j + 1
    i = i + 1



#exercise 5

n = int(input("Insert the amount of companies: "))
m = int(input("Insert the numbrt of months: "))

empresa = 1

while empresa> n:
    mes = 1
    print('empresa',empresa,':')
    while mes <= m:
        print('Mes',mes,': ')
        profit = int(input('insert the profit from your company: '))
        expenses = int(input('insert the expenses from your company: '))
        balance = balance + (profit - expenses)
        print('')
        mes = mes + 1

    if balance == 0:
        print('your company',empresa, 'stayed neutral (balance 0 dollars)')
    elif balance > 0:
        print('your company',empresa, 'had prodit of',balance)
    else:
        print('your company',empresa, 'stayed bellow the targe',balance)
    empresa = empresa + 1
    print("")







