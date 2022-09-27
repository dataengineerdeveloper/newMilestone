'''
a logica para  utizacao do while é que o que está detro do while é sempre verdade
sempre que ouver  uma ocorrencia falsa o while termina

ctrl+c >>> server para parar um execucao do terminal

o que o seguinte codigo está a fazer é incrementar sempre mais, até chegar ao 10, 
chegando a 10 a execucao termina


11 é maior que 10,  por esse motivo saimos do loop

'''

number = 0
while number  <= 10:
    print(number)
    number = number + 1
else:
    print('while loop ended and value of number ' + str(number))
