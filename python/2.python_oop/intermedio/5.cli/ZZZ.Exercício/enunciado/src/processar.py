import pandas as pd


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
