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
    pass


def carrega_base_ideb() -> typing.Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Carrega as bases de ideb com os dados históricos consolidados
    no censo de 2019 para anos iniciais, anos finais e ensino médio

    :return: bases de ideb ai, af e em
    """
    pass


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
    pass


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
    pass


def junta_bases(escolas: pd.DataFrame, ideb: pd.DataFrame) -> pd.DataFrame:
    """
    Junta as bases de escola e IDEB em uma base que contenha apenas as
    métricas de nota de IDEB e meta projetada por ano

    :param escolas: base consolidada de escolas tratada
    :param ideb: base consolidada de IDEB tratado
    :return: base de dados cruzados
    """
    pass


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
    pass


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
