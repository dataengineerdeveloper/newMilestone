import typing
import zipfile

import pandas as pd
from .configs import PATH_ENTRADA


def carrega_base_escola() -> typing.Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Carrega as bases de escola dos censos escolares de 2017 e 2019
    e retorna uma tupla com dataframes para os anos separados

    :return: base de escolas de 2017 e 2019
    """
    colunas = [
        "NU_ANO_CENSO",
        "CO_ENTIDADE",
        "NO_ENTIDADE",
        "TP_SITUACAO_FUNCIONAMENTO",
        "DT_ANO_LETIVO_INICIO",
        "DT_ANO_LETIVO_TERMINO",
        "CO_MUNICIPIO",
        "TP_DEPENDENCIA",
        "IN_LOCAL_FUNC_PREDIO_ESCOLAR",
        "IN_AGUA_INEXISTENTE",
        "IN_ENERGIA_INEXISTENTE",
        "IN_ESGOTO_INEXISTENTE",
        "IN_ALMOXARIFADO",
        "IN_AUDITORIO",
        "IN_BIBLIOTECA",
        "IN_SALA_LEITURA",
        "IN_COZINHA",
        "IN_REFEITORIO",
        "IN_LABORATORIO_CIENCIAS",
        "IN_LABORATORIO_INFORMATICA",
        "IN_QUADRA_ESPORTES",
        "IN_EQUIP_PARABOLICA",
        "IN_COMPUTADOR",
        "IN_EQUIP_COPIADORA",
        "IN_EQUIP_IMPRESSORA",
        "IN_EQUIP_DVD",
        "IN_EQUIP_SOM",
        "IN_EQUIP_TV",
        "IN_EQUIP_MULTIMIDIA",
        "IN_INTERNET",
        "IN_ALIMENTACAO",
    ]

    with zipfile.ZipFile(PATH_ENTRADA / "externo/censo_escolar/2017.zip") as z:
        with zipfile.ZipFile(
            z.open("Microdados_Censo_Escolar_2017/DADOS/ESCOLAS.zip")
        ) as z2:
            esc_2017 = pd.read_csv(
                z2.open("ESCOLAS.CSV"), sep="|", encoding="latin-1", usecols=colunas
            )

    with zipfile.ZipFile(PATH_ENTRADA / "externo/censo_escolar/2019.zip") as z:
        esc_2019 = pd.read_csv(
            z.open("microdados_educacao_basica_2019/DADOS/ESCOLAS.CSV"),
            sep="|",
            encoding="latin-1",
            usecols=colunas,
        )

    return esc_2017, esc_2019


def carrega_base_ideb() -> typing.Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Carrega as bases de ideb com os dados históricos consolidados
    no censo de 2019 para anos iniciais, anos finais e ensino médio

    :return: bases de ideb ai, af e em
    """
    with zipfile.ZipFile(
        PATH_ENTRADA / "externo/ideb/divulgacao_anos_finais_escolas_2019.zip"
    ) as z:
        ideb_af = pd.read_excel(
            z.open(
                "divulgacao_anos_finais_escolas_2019/divulgacao_anos_finais_escolas_2019.xlsx"
            ),
            skiprows=9,
        )

    with zipfile.ZipFile(
        PATH_ENTRADA / "externo/ideb/divulgacao_anos_iniciais_escolas_2019.zip"
    ) as z:
        ideb_ai = pd.read_excel(
            z.open(
                "divulgacao_anos_iniciais_escolas_2019/divulgacao_anos_iniciais_escolas_2019.xlsx"
            ),
            skiprows=9,
        )

    with zipfile.ZipFile(
        PATH_ENTRADA / "externo/ideb/divulgacao_ensino_medio_escolas_2019.zip"
    ) as z:
        ideb_em = pd.read_excel(
            z.open(
                "divulgacao_ensino_medio_escolas_2019/divulgacao_ensino_medio_escolas_2019.xlsx"
            ),
            skiprows=9,
        )

    return ideb_ai, ideb_af, ideb_em
