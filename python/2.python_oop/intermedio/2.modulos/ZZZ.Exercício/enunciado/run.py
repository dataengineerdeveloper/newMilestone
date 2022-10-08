"""
Dada o notebook de processamento de dados contido em 03.Manipulação de Dados/Projeto Final.ipynb
preencha as funções abaixo que permitam realizar o processamento da base de dados de forma completa
e exportar os resultados para a pasta do disco
"""

import typing
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

PATH_ENTRADA = Path(
    "G:/My Drive/Projetos/IZ/Cursos/Ciência de Dados/Compartilhar/dados/amostra"
)
PATH_SAIDA = Path(
    "G:/My Drive/Projetos/IZ/Cursos/Ciência de Dados/Compartilhar/aulas/04.Python Intermediário"
)


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


def processa_base_escola(
    esc_2017: pd.DataFrame, esc_2019: pd.DataFrame
) -> pd.DataFrame:
    """
    Consolida as bases do censo em uma base única, otimiza os tipos dos campos
    de dado e gera novas métricas para a base consolidada

    :param esc_2017: base de escolas do censo escolar de 2017
    :param esc_2019: base de escolas do censo escolar de 2019
    :return: base consolidada do censo
    """
    # concatena as bases para os dois anos
    escolas = esc_2017.append(esc_2019).reset_index(drop=True)

    # seleciona apenas escolas ativas
    escolas = escolas.loc[lambda f: f["TP_SITUACAO_FUNCIONAMENTO"] == 1]

    # remove a coluna de situação de funcionamento
    escolas.drop(columns=["TP_SITUACAO_FUNCIONAMENTO"], inplace=True)

    # converte as datas para datetime
    escolas = escolas.assign(
        DT_ANO_LETIVO_INICIO=lambda f: pd.to_datetime(
            f["DT_ANO_LETIVO_INICIO"], format="%d/%m/%Y"
        ),
        DT_ANO_LETIVO_TERMINO=lambda f: pd.to_datetime(
            f["DT_ANO_LETIVO_TERMINO"], format="%d/%m/%Y"
        ),
    )

    # calcula a quantidade de dias do ano letivo
    escolas = escolas.assign(
        QT_DIAS_LETIVOS=lambda f: (
            f["DT_ANO_LETIVO_TERMINO"] - f["DT_ANO_LETIVO_INICIO"]
        ).dt.days
    )

    # converte o campo de TP DEPENDENCIA em texto
    escolas = escolas.assign(
        TP_DEPENDENCIA=lambda f: f["TP_DEPENDENCIA"].replace(
            {
                1: "Federal",
                2: "Estadual",
                3: "Municipal",
                4: "Privada",
            }
        )
    )

    # converte o TP_DEPENDENCIA para categoria
    escolas = escolas.assign(
        TP_DEPENDENCIA=lambda f: f["TP_DEPENDENCIA"].astype(
            pd.CategoricalDtype(
                categories=["Federal", "Estadual", "Municipal", "Privada"]
            )
        ),
    )

    # ajusta as colunas IN_ para inteiros
    cols_in = [c for c in esc_2019 if c.startswith("IN_")]
    for c in cols_in:
        escolas[c] = escolas[c].astype("uint8")

    return escolas


def processa_base_ideb(
    ideb_ai: pd.DataFrame, ideb_af: pd.DataFrame, ideb_em: pd.DataFrame
) -> pd.DataFrame:
    """
    Consolida as bases de IDEB e gera uma base final por escola e ano
    que contenha as diferentes métricas por série que o IDEB gera

    :param ideb_ai: base de métricas do IDEB dos anos iniciais
    :param ideb_af: base de métricas do IDEB dos anos finais
    :param ideb_em: base de métricas do IDEB do ensino médio
    :return: base de métricas do IDEB por escola e ano
    """
    # remove as linhas com dados sobre a coleta
    ideb_ai.dropna(
        subset=list(ideb_ai.loc[:, "CO_MUNICIPIO":].columns), how="all", inplace=True
    )
    ideb_af.dropna(
        subset=list(ideb_af.loc[:, "CO_MUNICIPIO":].columns), how="all", inplace=True
    )
    ideb_em.dropna(
        subset=list(ideb_em.loc[:, "CO_MUNICIPIO":].columns), how="all", inplace=True
    )

    # realiza o melt das bases selecionando apenas as métricas de interesse
    metricas = [
        "VL_APROVACAO",
        "VL_INDICADOR_REND",
        "VL_NOTA_MATEMATICA",
        "VL_NOTA_PORTUGUES",
        "VL_NOTA_MEDIA",
        "VL_OBSERVADO",
        "VL_PROJECAO",
    ]
    ideb_ai = ideb_ai.melt(
        id_vars=["ID_ESCOLA"],
        value_vars=[c for c in ideb_ai if any([c.startswith(m) for m in metricas])],
        var_name="METRICA",
        value_name="VALOR",
    )
    ideb_af = ideb_af.melt(
        id_vars=["ID_ESCOLA"],
        value_vars=[c for c in ideb_af if any([c.startswith(m) for m in metricas])],
        var_name="METRICA",
        value_name="VALOR",
    )
    ideb_em = ideb_em.melt(
        id_vars=["ID_ESCOLA"],
        value_vars=[c for c in ideb_em if any([c.startswith(m) for m in metricas])],
        var_name="METRICA",
        value_name="VALOR",
    )

    # consolida os dados numa base única
    ideb = (
        ideb_ai.assign(SERIE="AI")
        .append(ideb_af.assign(SERIE="AF"))
        .append(ideb_em.assign(SERIE="EM"))
    )

    # ajusta os campos de valores do IDEB
    ideb = (
        ideb.assign(VALOR=lambda f: f["VALOR"].astype(str))
        .assign(VALOR=lambda f: f["VALOR"].str.replace(",", "."))
        .assign(VALOR=lambda f: f["VALOR"].str.replace("[*]", ""))
        .assign(
            VALOR=lambda f: np.where(
                f["VALOR"].str.contains("ND"),
                np.nan,
                np.where(f["VALOR"] == "-", np.nan, f["VALOR"]),
            )
        )
        .assign(VALOR=lambda f: f["VALOR"].astype("float64"))
    )

    # cria o campo de ano do censo
    ideb = ideb.assign(
        ANO=lambda f: f["METRICA"]
        .str.split("_")
        .map(lambda x: [c for c in x if c.isnumeric()][0])
    ).assign(ANO=lambda f: f["ANO"].astype("uint16"))

    # gera uma coluna de métricas
    ideb = ideb.assign(
        METRICA2=lambda f: f.apply(
            lambda x: x["METRICA"].replace(f"_{x['ANO']}", ""), axis=1
        )
    )
    ideb = ideb.assign(METRICA2=lambda f: f["METRICA2"] + "_" + f["SERIE"])

    # faz o pivot da base para obter métricas por ano
    ideb = ideb.pivot_table(
        index=["ID_ESCOLA", "ANO"], columns="METRICA2", values="VALOR"
    ).reset_index()

    # converte o campo de ID de escola para inteiro
    ideb["ID_ESCOLA"] = ideb["ID_ESCOLA"].astype("int")

    return ideb


def junta_bases(escolas: pd.DataFrame, ideb: pd.DataFrame) -> pd.DataFrame:
    """
    Junta as bases de escola e IDEB em uma base que contenha apenas as
    métricas de nota de IDEB e meta projetada por ano

    :param escolas: base consolidada de escolas tratada
    :param ideb: base consolidada de IDEB tratado
    :return: base de dados cruzados
    """
    cruzada = escolas.merge(
        ideb.reindex(
            columns=["ID_ESCOLA", "ANO"]
            + [c for c in ideb if c.startswith("VL_OBS") or c.startswith("VL_PROJ")]
        ),
        left_on=["CO_ENTIDADE", "NU_ANO_CENSO"],
        right_on=["ID_ESCOLA", "ANO"],
        how="left",
    ).drop(columns=["ID_ESCOLA", "ANO"])

    cruzada.rename(
        columns={
            "VL_OBSERVADO_AF": "IDEB_AF",
            "VL_OBSERVADO_AI": "IDEB_AI",
            "VL_OBSERVADO_EM": "IDEB_EM",
            "VL_PROJECAO_AF": "IDEB_META_AF",
            "VL_PROJECAO_AI": "IDEB_META_AI",
            "VL_PROJECAO_EM": "IDEB_META_EM",
        },
        inplace=True,
    )

    return cruzada


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


def main():
    # carrega as bases de entrada
    print("-" * 100)
    print("CARREGANDO DADOS DE ESCOLA", end="...")
    esc_2017, esc_2019 = carrega_base_escola()

    print("CARREGANDO DADOS DE IDEB", end="...")
    ideb_ai, ideb_af, ideb_em = carrega_base_ideb()
    print("OK!")

    # consolida as bases de dados
    print("PROCESSANDO DADOS DE ESCOLA", end="...")
    escolas = processa_base_escola(esc_2017, esc_2019)
    print("OK!")

    print("PROCESSANDO DADOS DE IDEB", end="...")
    ideb = processa_base_ideb(ideb_ai, ideb_af, ideb_em)
    print("OK!")

    # junta as bases numa base única
    print("CONSOLIDANDO DADOS EM BASE ÚNICA", end="...")
    cruzada = junta_bases(escolas, ideb)
    print("OK!")

    # exporta os resultados
    print("EXPORTANDO RESULTADOS", end="...")
    exporta_bases(escolas, ideb, cruzada)
    print("OK!")

    print("-" * 100)


main()
