##############################
##   LOOPS / interations    ##
##############################

nums = [1,2,3,4,5]

#exemplo 1
#for nums in num:
 #   print(nums)

#exemplo 2

#BREAK  - para sempre que é encontrado o valor colocado no if

for num in nums:
    if num == 3:
        print('Found it!')
        break
    print(num)

#CONTINUE - encontra o valor e print a mensagem de found, contudo continua o Loop
for num in nums:
    if num == 3:
        print('Found it!')
        continue
    print(num)


#exemplo 3

#usar um loop dentro de um loop
#NOTAS >> o loop vai iterar por cada valor 'abc', os numeros que estão na list de nums

for num in nums:
    for letter in 'abc':
        print(num,letter)

#exemplo 4
# se quisermos que seja colocados numero de 1 a 10, se colocassemos um range(10), iamos ter apenas numero de 0 a 9,   solução é ter como está apresentado
for i in range (1,11):
        print(i)

x = 0

# vai ser feito loop até que o valor chegue a 10
'''while x < 10:
    print(x)
    x +=1
'''

#aqui loop vai parar quando o valor encontrar o 5
'''while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
'''

'''
while True:
    print(x)
    x += 1

'''


x = 0 
y = 1
e = 5
f = 3
while x < y:
    x +=1
    print(x)
    if f > 0:
        continue
    if x == e:
        print('hit e')
        break
    print('end loop')
    

