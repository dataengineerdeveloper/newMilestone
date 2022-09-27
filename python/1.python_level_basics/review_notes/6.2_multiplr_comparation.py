
'''
podesmos fzer mias do que uma compraçao contudo, basta uma das comparaçoes ser false, ele apresenta como falso

x=1<2<3
print(x) >> true


x=(3==3)<5
print(x) >> true

'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if ((nota1+nota2)/2) == 10:
    print("Aprovado com Distinção")
elif ((nota1+nota2)/2) < 7:
    print("Reprovado")
else:
    print("Aprovado")
    
