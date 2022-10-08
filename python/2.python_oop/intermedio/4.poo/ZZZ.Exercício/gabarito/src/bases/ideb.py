import zipfile

import numpy as np
import pandas as pd

from .base import _BaseDeDados


class Ideb(_BaseDeDados):
    def _carregar(self) -> None:
        """
        Carrega as bases de escola dos censos escolares de 2017 e 2019
        e retorna uma tupla com dataframes para os anos separados

        :return: base de escolas de 2017 e 2019
        """
        with zipfile.ZipFile(
            self._pasta_entrada / "externo/ideb/divulgacao_anos_finais_escolas_2019.zip"
        ) as z:
            self._dados_entrada["ideb_af"] = pd.read_excel(
                z.open(
                    "divulgacao_anos_finais_escolas_2019/divulgacao_anos_finais_escolas_2019.xlsx"
                ),
                skiprows=9,
            )

        with zipfile.ZipFile(
            self._pasta_entrada
            / "externo/ideb/divulgacao_anos_iniciais_escolas_2019.zip"
        ) as z:
            self._dados_entrada["ideb_ai"] = pd.read_excel(
                z.open(
                    "divulgacao_anos_iniciais_escolas_2019/divulgacao_anos_iniciais_escolas_2019.xlsx"
                ),
                skiprows=9,
            )

        with zipfile.ZipFile(
            self._pasta_entrada
            / "externo/ideb/divulgacao_ensino_medio_escolas_2019.zip"
        ) as z:
            self._dados_entrada["ideb_em"] = pd.read_excel(
                z.open(
                    "divulgacao_ensino_medio_escolas_2019/divulgacao_ensino_medio_escolas_2019.xlsx"
                ),
                skiprows=9,
            )

    def _processar(self) -> None:
        """
        Consolida as bases do censo em uma base única, otimiza os tipos dos campos
        de dado e gera novas métricas para a base consolidada
        """
        # remove as linhas com dados sobre a coleta
        ideb_ai = self.dados_entrada["ideb_ai"].dropna(
            subset=list(self.dados_entrada["ideb_ai"].loc[:, "CO_MUNICIPIO":].columns),
            how="all",
        )
        ideb_af = self.dados_entrada["ideb_af"].dropna(
            subset=list(self.dados_entrada["ideb_af"].loc[:, "CO_MUNICIPIO":].columns),
            how="all",
        )
        ideb_em = self.dados_entrada["ideb_em"].dropna(
            subset=list(self.dados_entrada["ideb_em"].loc[:, "CO_MUNICIPIO":].columns),
            how="all",
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

        self._dados_saida["ideb"] = ideb

    def _exportar(self) -> None:
        """
        Exporta os dados da propriedade dados_saida para o disco
        """
        self._dados_saida["ideb"].to_csv(
            self._pasta_saida / "ideb.csv",
            sep=";",
            decimal=",",
            encoding="latin-1",
            index=False,
        )
