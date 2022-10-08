# faça um program que leia a ficheiro anterior e devolva quantas linhas,  palavras,  vogais e consoantes coném esse ficheiro
# solicite uma palavra ai utilizador e informae-0 quantas vezes essas palavra 
fnome = "pensamentos.txt"


try: 
    fp = open(fnome, 'r', encoding="UTF-8")
    conteudo=fp.readlines()# le linhas para uma lista
    fp.close()
    
    qtlinhas = len(conteudo)
    string = ''.join(conteudo)
    string = string.replace('\n',' ')
    
    novalista = string.split(' ')
    qtpals = len(novalista) # cont apalavta qq coisa
    #qtpals = 0
    #for pal in novalista:
     #   if pal.isalpha():
      #      qtpals +=1
    vogais = 'aáàâãeéèêiíìoóòôõuúù'
    qtvog, qtcons =0, 0
    
    for i in string:            
        if i.isalpha(): #garante que é uma letra
            if i.lower() in vogais: #
              qtvog= qtvog +1
            else:
                qtcons=qtcons +1
    print(f"o ficheiro contem {qtlinhas} linhas de textos")
    print(f"o ficheiro contem {qtpals} palavras")
    print(f"o ficheiro contem {qtvog} vogais")
    print(f"o ficheiro contem {qtcons} consoantes")
    
    
    #B
    
    pal = input("qual a palavra a procurar?")
    qtpal = string.count(pal)
    print(f"a palavras{pal} ocorrer {qtpal} de vezes no ficheiro")
    
    posiçoes = [] # guardar o numero da linha onde ocorre o pal
    
    for i, frase in enumerate(conteudo):
      if pal in frase:
        posiçoes.append(i+1)    
      
      print(f"palavra {pal} ocorre {qtpal} de vezes no ficheiro nas linhas {posiçoes}")
            
except FileExistsError:
    print("nao foi encontrado o ficheiro referido")
