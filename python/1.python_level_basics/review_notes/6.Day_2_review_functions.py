##################
## FUNCTIONS    ##
##################

# dentro da def, quando nao temso nenhum paramaetro para adicionar, podemos usar o PASS,  de forma a que o codigo passe esta def sem dar erro

def hello_func():
    print('hello function.')
#we don't have any result once there isn't nothing within the function
#print(hello_func())
#concept DRY (don't repite yourself)

#imagine that we print our function 4 times and for some reasopm

print('hello function!')
print('hello function!')
print('hello function!')
print('hello function!')
#>>> imagine that we have to update ! by . and if we follow this approach we will have to change the 4 prints
#however if we change our funtions we only have to change once
hello_func()
hello_func()
hello_func()
hello_func()

