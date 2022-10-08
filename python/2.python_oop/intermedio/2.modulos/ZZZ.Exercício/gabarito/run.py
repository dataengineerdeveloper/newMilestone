"""
Dada o notebook de processamento de dados contido em 03.Manipulação de Dados/Projeto Final.ipynb
preencha as funções abaixo que permitam realizar o processamento da base de dados de forma completa
e exportar os resultados para a pasta do disco
"""

from src import *


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


if __name__ == "__main__":
    main()
