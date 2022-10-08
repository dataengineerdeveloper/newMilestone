import typing

import click


@click.group()
def cli():
    pass


@cli.group()
def grupo1():
    pass


@cli.group()
def grupo2():
    pass


@grupo1.command()
@click.option("--n", default=1)
def pontos(n: int) -> None:
    click.echo("." * n)


@grupo1.command()
@click.option("--from", "from_")
@click.option("--to")
def reservado(from_: str, to: str) -> None:
    click.echo(f"de {from_} para {to}")


@grupo2.command()
@click.option("--mensagem", "-m", multiple=True)
def multipla(mensagem: typing.List[str]) -> None:
    click.echo("\n".join(mensagem))


@grupo2.command()
@click.option("--usuario", prompt=True)
@click.option("--senha", prompt=True, hide_input=True, confirmation_prompt=True)
def hello(usuario: str, senha: str):
    click.echo(f"Olá {usuario}")
    click.echo(senha)


if __name__ == "__main__":
    cli()
