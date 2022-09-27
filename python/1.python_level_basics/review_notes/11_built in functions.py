def check_age (age):
        if age < 18:
            print('opps not an adult')
        else:
            print('yes, its an adult')

'''python já tem um cnjunto de funcoes, upper, lower, capitalize,startswith, etc existe imensas
neste 2 casos os que vamos fazer é passar o argumento  hello e validar em que letra é que termina'''
print('hello'.endswith('O'))
print('hello'.endswith('o'))

'''o que vemos dentro do check_age é um argument'''
check_age(18)
check_age(17)
check_age(99)
