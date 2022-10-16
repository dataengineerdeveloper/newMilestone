nome_fich = input("qual o noe do ficheiro: ")

pos = nome_fich.rfind('.')
nome = nome_fich[ :pos]
ext = nome_fich[pos +1: ]

print("nome=",nome,"ext=",ext)

for ind in range(1,11):
    nome_fich =  nome + str(ind)+'.'+ ext
    #print(nome_fich)
    fp = open(nome_fich, 'w')
    fp.close()
    
