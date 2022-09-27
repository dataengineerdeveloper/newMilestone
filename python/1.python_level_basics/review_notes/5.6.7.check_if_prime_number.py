'''
Prime numbers:

If the natural number is greater than 1 and having no positive divisors other than 1 and the number itself etc.

For example: 3, 7, 11 etc are prime numbers.

Composite number:

Other natural numbers that are not prime numbers are called composite numbers.

For example: 4, 6, 9 etc. are composite numbers.

Let us look at the following example to understand the implementation.


Funcões e logicas utilizdas:
    - nested if else condition
Logica:
    1.  primeiro temos de validar se o numero é maior do que 1 ou nao;
    2.  se o valor nao for maior do que um vai logo para o else;
    3. o valor que vai para o loop,  se for um valor completamente divisivel por 'i' então o valor nao é primo, caso contrario é.

'''

def prime_number(a):
    if a > 1:
        for b in range(2,int(a/2)+1):
            if(a % b)==0:
                print(a, 'não um valor primo')
                break
            else:
                print(a, 'é um vlor primo')
a = int(input('insere o valor: ')) 

prime_number(a)
