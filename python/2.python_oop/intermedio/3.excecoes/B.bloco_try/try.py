import traceback

print("Cheguei Aqui")

# print(int("Olá Mundo"))
# print(1 / 0)
d = dict(a=1, b=2)

# try = tentar
try:
    try:
        d["d"] = 1 / 0
    except ZeroDivisionError:
        d["d"] = 4
    print(d["c"])
    d["e"] = 5
except ZeroDivisionError:
    d["d"] = 4
except KeyError:
    # print(traceback.format_exc())
    d["c"] = 3
except Exception:
    print("Exceção geral")
else:
    d["f"] = 6
finally:
    print(d)


print("Não Cheguei Aqui")
