# https://click.palletsprojects.com/en/8.1.x/

import click


@click.command()
@click.option("--count", default=1, help="Número de olas que devemos fazer.")
@click.option("--nome", prompt="Seu nome", help="Nome da pessoa")
def hello(count: int, nome: str):
    for i in range(count):
        click.echo(f"Olá {nome}!")


if __name__ == "__main__":
    hello()