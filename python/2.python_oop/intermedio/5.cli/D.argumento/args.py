import typing
import click


@click.command()
@click.argument("count", type=click.INT)
@click.argument("nome", nargs=-1)
def hello(count: int, nome: typing.List[str]):
    """
    Diz olá para uma pessoa um certo número de vezes

    :param count: Número de vezes para repetir a mensagem
    :param nome: Nome da pessoa a comprimentar
    """
    for i in range(count):
        for n in nome:
            click.echo(f"Olá {n}!")


if __name__ == "__main__":
    hello()
