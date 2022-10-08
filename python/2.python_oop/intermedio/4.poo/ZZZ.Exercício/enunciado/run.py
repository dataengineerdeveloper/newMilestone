"""
Dada o notebook de processamento de dados contido em 03.Manipulação de Dados/Projeto Final.ipynb
preencha as funções abaixo que permitam realizar o processamento da base de dados de forma completa
e exportar os resultados para a pasta do disco
"""

from src.configs import PATH_ENTRADA, PATH_SAIDA
from src.bases import Escolas, Ideb
from src.processar import junta_bases


def main():
    # gerando objetos de carregamento
    esc_2017 = Escolas(PATH_ENTRADA, PATH_SAIDA, 2017)
    esc_2019 = Escolas(PATH_ENTRADA, PATH_SAIDA, 2019)
    ideb = Ideb(PATH_ENTRADA, PATH_SAIDA)

    # executa os objetos de processamento
    esc_2017.pipeline()
    esc_2019.pipeline()
    ideb.pipeline()

    # gera a base consolidada
    escolas = (
        esc_2017.dados_saida["escola"]
        .append(esc_2019.dados_saida["escola"])
        .reset_index(drop=True)
    )

    # junta as bases numa base única
    print("CONSOLIDANDO DADOS EM BASE ÚNICA", end="...")
    cruzada = junta_bases(escolas, ideb.dados_saida["ideb"])
    cruzada.to_pickle(PATH_SAIDA / "cruzada.pkl")
    print("OK!")


if __name__ == "__main__":
    main()
