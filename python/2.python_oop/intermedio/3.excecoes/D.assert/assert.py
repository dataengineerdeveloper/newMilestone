import pandas as pd

df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=["a", "b", "c"])

# assert = garanta
assert "d" in df, "O dataframe não possuí a coluna 'd'"
# AssertionError

# if "d" not in df:
#     raise KeyError("O dataframe não possuí a coluna 'd'")

print("Cheguei aqui")

