import pandas as pd

from .configs import PATH_SAIDA


def exporta_bases(
    escolas: pd.DataFrame, ideb: pd.DataFrame, cruzada: pd.DataFrame
) -> None:
    """
    Exporta as bases de dados para o disco
    - escola como parquet particionada por NU_ANO_CENSO
    - ideb como csv no padrão brasileiro
    - cruzada como pickle

    :param escolas: base consolidada de escolas tratada
    :param ideb: base consolidada de IDEB tratado
    :param cruzada:base de dados cruzados
    """
    escolas.to_parquet(PATH_SAIDA / "escolas.parquet", partition_cols=["NU_ANO_CENSO"])
    ideb.to_csv(
        PATH_SAIDA / "ideb.csv", sep=";", decimal=",", encoding="latin-1", index=False
    )
    cruzada.to_pickle(PATH_SAIDA / "cruzada.pkl")
