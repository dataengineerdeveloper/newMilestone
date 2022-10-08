import typing
import click
from pathlib import Path
from datetime import datetime


@click.command()
@click.option("--n", default=1, type=click.IntRange(min=1, max=100))
@click.option("--p", default=4.10, type=click.FloatRange(min=4, max=12))
@click.option("--i", default="Feijão", type=click.STRING)
@click.option("--d", default="2022-04-06", type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option(
    "--c",
    default=".",
    type=click.Path(file_okay=False, resolve_path=True, path_type=Path),
)
@click.option(
    "--f",
    default="./teste.txt",
    type=click.File(mode="w", encoding="latin-1"),
)
@click.option("--mostra/--nao-mostra", is_flag=True)
@click.option("--m", default="-A-", type=click.Choice(["-A-", "-B-", "-C-"]))
def pontos(n: int, p: float, i: str, d: datetime, c: Path, f, mostra: bool, m: str) -> None:
    # exists (false) se True e caminho/arquivo não existe ele pula os checks
    # file_okay = você pode passar um arquivo
    # dir_okay = você pode passar um diretório
    # readable = se você consegue ler um arquivo
    # writeble = se você consegue escrever um arquivo
    # executable = se o arquivo é executável
    # resolve_path = criar o caminho absoluto
    # path_type = converter o tipo do dado
    click.echo(type(n))
    click.echo(type(p))
    click.echo(type(i))
    click.echo(type(d))
    click.echo(type(c))
    click.echo(type(f))
    click.echo(type(mostra))
    click.echo(type(m))
    f.write("Olá mundo!")
    if mostra:
        click.echo(f"Eu quero {n} unidades de {i} da marca {m} por R$ {p} para a data {d} - {c}")
    else:
        click.echo(f"Eu quero {n} unidades de {i} da marca {m} por R$ {p} para a data {d}")


if __name__ == "__main__":
    pontos()
