
number = int(input('number: '))
print(number)
if number % 2 == 0:
    print('par')
else:
    print('impar')


number = int(input('number: '))
print('number')

for count in range(1,11):

    print(number,'x',count,'=',number*count)


#
import time as t

x = 1
while True:
    print(x)
    x=x+1
    t.sleep(0.5)



