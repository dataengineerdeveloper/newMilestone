print("Cheguei Aqui")

# print(int("Olá Mundo"))
# print(1 / 0)
d = dict(a=1, b=2)

# try = tentar
try:
    d["d"] = 1 / 0
    print(d["c"])
    d["e"] = 5
except:
    d["c"] = 3
    print(d)

print("Não Cheguei Aqui")
