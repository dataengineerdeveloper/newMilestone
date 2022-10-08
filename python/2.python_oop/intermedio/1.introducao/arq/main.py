import os

import pandas as pd


def main():
    ideb = pd.read_parquet("dados/ideb.parquet")
    print(os.getcwd())


main()

