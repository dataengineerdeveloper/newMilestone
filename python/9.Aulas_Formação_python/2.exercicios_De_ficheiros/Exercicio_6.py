# exercicio 6


f1 =  'ficheiro_1.txt'
f2 =  'ficheiro_1.txt'

fp1 = open(f1, 'r',  encoding='UTF-8')
fp2 = open(f2, 'r',  encoding='UTF-8')




#carregar em menoria como string cont1 / lista cont2
cont1 = fp1.read() # carrega com string

if cont1[-1] != '\n':
    cont1 = cont1+ '\n'
cont2 = fp2.readlines() #carrega como lista

ultimafrase = cont2[-1]
if ultimafrase != '\n':
    ultimafrase = ultimafrase + '\n'
#print(f"ultima frase = {ultimafrase}")

cont2[-1] = ultimafrase # sunstituir a ultima frase se o \n,  pela ultima frase com de \n

print(f"ultima frase = {ultimafrase}")
print("Ficheiro_2:\n",cont2)

fp1.close()
fp2.close()

#count_final = cont1 +  cont2
# inverter a order das linhas
# linha1,  linha 2,  linha 3 > linha 3, linha 2, linhas 1
#print("ficheiro_2:\n", cont2) #print par validar se o ficheiro inverte
Cont2 =  cont2[::-1]
#print("ficheiro_2 invertido:\n", cont2) #print par validar se o ficheiro inverte

fp3 = open('final.txt', 'w', encoding='UTF-8')
fp3.write(cont1) # escreve conteudo do 1 ficheiro
fp3.writelines(cont2)
fp3.close()

