import random
'''
1. define all variables needded(lower_case,  upper_case, symbols)
2. create a var that concatenate the 3 variables
3. create a extrat variable to define de length of password
4. creare variable password ("".join(random.sample(use_for,length_for_pass)))

'''

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!"#$%&/()=?'
use_for=lower_case+upper_case+numbers+symbols
length_for_pass = 20


password="".join(random.sample(use_for,length_for_pass))

print(password)
