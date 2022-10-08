"""
Crie  2  ficheiros  de  texto  com  algo  escrito  em  ambos.  Desenvolva  um  programa  que solicite o 
nome dos 2 ficheiros ao utilizador.

 Crie a função junta_fich() que recebe os 2 nomes como argumentos.
A função deverá criar o ficheiro de saída com a concatenação dos 2 ficheiros. O nome do ficheiro de 
saída deverá ser o nome do primeiro ficheiro, concatenado com “_”, seguido do nome do segundo ficheiro
e com a extensão “.txt”Exemplo: Fich1  python.txt   Fich2  Linux.txt   Fich_saida  python_linux.txt

"""

def junta_fich(f1,f2):
    # file pointer > abertura de um ficheiro
    try:
        fp1 = open(f1,'r',  encoding='UTF-8')
        cont1 = fp1.read()#ler como string
        fp1.close()#liberta o processo
        
        # verficar se termina em \n
        
        if cont1[-1] != '\n': # temos de acrescentar o caracter \n
            cont1 = cont1 + '\n'
        
        fp2 = open(f2,'r',  encoding='UTF-8')
        cont2 = fp2.read()#ler como string
        fp2.close()#liberta o processo
        
        res = cont1 + cont2 
        
        ## construit o nome do fichiero final
        pos = f1.rfind('.')
        nf1 = f1[:pos]
        pos = f2.rfind('.')
        nf2 = f2[:pos]
        
        nfinal = nf1 + '_' + nf2 + '.txt'
        
        fp3 = open(nfinal, 'w', encoding='UTF-8')
        fp3.write(res)
        fp3.close()
        
        
        print("resultado final\n",  nfinal)
        
    except FileNotFoundError:
        print("não foi possivel encontrar o ficheiros referidos")
        
        



nome1 = str(input("insirir o neom do ficheoro 1: ")) 
nome2 = str(input("insirir o neom do ficheoro 2: ")) 
junta_fich(nome1,nome2)

