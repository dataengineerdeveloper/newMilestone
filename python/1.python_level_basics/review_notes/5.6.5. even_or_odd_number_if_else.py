'''
Odd and Even numbers:

If you divide a number by 2 and it gives a remainder of 0 then it is known as even number, otherwise an odd number.

Even number examples: 2, 4, 6, 8, 10, etc.

Odd number examples:1, 3, 5, 7, 9 etc.

See this example:

'''

def check_value(num):

    if (num % 2) == 0:
        print('{0} valor é par'.format(num))
    else:
        print('{0} valor é inteiro'.format(num))

num= int(input('digite o seu valor:'))
check_value(num)