import typing
import zipfile
from pathlib import Path

import pandas as pd

from .base import _BaseDeDados


class Escolas(_BaseDeDados):
    colunas: typing.List[str] = [
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

    ano: int

    def __init__(
        self, entrada: typing.Union[str, Path], saida: typing.Union[str, Path], ano: int
    ) -> None:
        super().__init__(entrada, saida)
        self.ano = ano

    def _carregar(self) -> None:
        """
        Carrega as bases de escola dos censos escolares de 2017 e 2019
        e retorna uma tupla com dataframes para os anos separados

        :return: base de escolas de 2017 e 2019
        """
        if self.ano == 2017:
            with zipfile.ZipFile(
                self._pasta_entrada / "externo/censo_escolar/2017.zip"
            ) as z:
                with zipfile.ZipFile(
                    z.open("Microdados_Censo_Escolar_2017/DADOS/ESCOLAS.zip")
                ) as z2:
                    self._dados_entrada["escolas"] = pd.read_csv(
                        z2.open("ESCOLAS.CSV"),
                        sep="|",
                        encoding="latin-1",
                        usecols=self.colunas,
                    )
        elif self.ano == 2019:
            with zipfile.ZipFile(
                self._pasta_entrada / "externo/censo_escolar/2019.zip"
            ) as z:
                self._dados_entrada["escolas"] = pd.read_csv(
                    z.open("microdados_educacao_basica_2019/DADOS/ESCOLAS.CSV"),
                    sep="|",
                    encoding="latin-1",
                    usecols=self.colunas,
                )
        else:
            raise NotImplementedError(
                f"Nós não implementamos o processamento do ano {self.ano}"
            )

    def _processar(self) -> None:
        """
        Consolida as bases do censo em uma base única, otimiza os tipos dos campos
        de dado e gera novas métricas para a base consolidada
        """
        # seleciona apenas escolas ativas
        escolas = self._dados_entrada["escolas"].loc[
            lambda f: f["TP_SITUACAO_FUNCIONAMENTO"] == 1
        ]

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
        cols_in = [c for c in self.dados_entrada if c.startswith("IN_")]
        for c in cols_in:
            escolas[c] = escolas[c].astype("uint8")

        self._dados_saida["escolas"] = escolas

    def _exportar(self) -> None:
        """
        Exporta os dados da propriedade dados_saida para o disco
        """
        self.dados_saida["escolas"].to_parquet(
            self._pasta_saida / "escolas.parquet", partition_cols=["NU_ANO_CENSO"]
        )
