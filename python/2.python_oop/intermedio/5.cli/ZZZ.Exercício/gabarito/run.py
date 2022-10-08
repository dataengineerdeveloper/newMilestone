from pathlib import Path

import click
import pandas as pd

from src.bases import Escolas, Ideb
from src.configs import PATH_ENTRADA, PATH_SAIDA
from src.processar import junta_bases


@click.group()
def cli():
    pass


@cli.command()
@click.argument("base", type=click.Choice(["escola", "ideb"]))
@click.argument("ano", type=click.STRING)
@click.option(
    "--entrada",
    default=str(PATH_ENTRADA),
    type=click.Path(file_okay=False, resolve_path=True, path_type=Path),
    help="Pasta de entrada dos dados",
)
@click.option(
    "--saida",
    default=str(PATH_SAIDA),
    type=click.Path(file_okay=False, resolve_path=True, path_type=Path),
    help="Pasta de saída dos dados",
)
def processa_base(base: str, ano: str, entrada: Path, saida: Path) -> None:
    """
    Executa o pipeline do objeto de processamento de dados adequado

    :param base: Base de dados a ser processada (escola ou ideb)
    :param ano: Ano de processamento (deve ser um inteiro ou N/A)
    :param entrada: Pasta de entrada dos dados
    :param saida: Pasta de saída dos dados
    """
    assert ano.isnumeric() or ano == "N/A"

    if base == "escola":
        ano = int(ano) if ano.isnumeric() else None
        processar = Escolas(entrada, saida, ano)
    else:
        processar = Ideb(entrada, saida)

    processar.pipeline()


@cli.command()
@click.option(
    "--entrada",
    default=str(PATH_ENTRADA),
    type=click.Path(file_okay=False, resolve_path=True, path_type=Path),
    help="Pasta de entrada dos dados",
)
@click.option(
    "--saida",
    default=str(PATH_SAIDA),
    type=click.Path(file_okay=False, resolve_path=True, path_type=Path),
    help="Pasta de saída dos dados",
)
def gera_datamart(entrada: Path, saida: Path) -> None:
    """
    Executa o pipeline do objeto de processamento de dados adequado

    :param entrada: Pasta de entrada dos dados
    :param saida: Pasta de saída dos dados
    """
    escolas = pd.read_parquet(entrada / "escolas.parquet")
    ideb = pd.read_csv(
        entrada / "ideb.csv",
        sep=";",
        decimal=",",
        encoding="latin-1",
    )

    # junta as bases numa base única
    print("CONSOLIDANDO DADOS EM BASE ÚNICA", end="...")
    cruzada = junta_bases(escolas, ideb)
    cruzada.to_pickle(saida / "cruzada.pkl")
    print("OK!")


if __name__ == "__main__":
    cli()
