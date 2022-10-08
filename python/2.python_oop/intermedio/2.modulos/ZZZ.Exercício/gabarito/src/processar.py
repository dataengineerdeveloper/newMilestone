import numpy as np
import pandas as pd


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
