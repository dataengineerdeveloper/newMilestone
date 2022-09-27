first_name='luis '
last_name ='nogueira'

full_name = first_name.capitalize()+last_name.upper()
print(full_name)  
print(len(first_name))
print(len(last_name))
##aqui vamos usar o endswith,  para validar se o que vem no fim full_name é 'hello', o output é False
print(full_name.endswith('hello'))