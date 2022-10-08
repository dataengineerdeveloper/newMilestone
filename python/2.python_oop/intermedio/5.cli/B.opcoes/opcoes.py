import typing
import click


# @click.command()
# @click.option("--n", default=1)
# def pontos(n: int) -> None:
#     click.echo("." * n)


# @click.command()
# @click.option("--n", required=True, type=int)
# def pontos(n: int) -> None:
#     click.echo("." * n)

# @click.command()
# @click.option("--from", "from_")
# @click.option("--to")
# def reservado(from_: str, to: str) -> None:
#     click.echo(f"de {from_} para {to}")

# @click.command()
# @click.option("--cidade-de-origem", "-co", "co")
# @click.option("--cidade-de-destino", "-cd", "cd")
# def reservado(co: str, cd: str) -> None:
#     click.echo(f"de {co} para {cd}")


# @click.command()
# @click.option(
#     "--n", default=1, show_default=True, help="Número de vezes para aparecer o ponto"
# )
# def pontos(n: int) -> None:
#     click.echo("." * n)

# @click.command()
# @click.option("--pos", nargs=2, type=float)
# def multipla(pos: typing.Tuple[float, float]) -> None:
#     x, y = pos
#     click.echo(f"x={x} | y={y}")

# @click.command()
# @click.option("--item", type=(str, float))
# def multipla(item: typing.Tuple[str, float]) -> None:
#     nome, preco = item
#     click.echo(f"O produto {nome} tem preço R$ {preco}")


# @click.command()
# @click.option("--mensagem", "-m", multiple=True)
# def multipla(mensagem: typing.List[str]) -> None:
#     click.echo("\n".join(mensagem))

@click.command()
@click.option("--usuario", prompt=True)
@click.option("--senha", prompt=True, hide_input=True, confirmation_prompt=True)
def hello(usuario: str, senha: str):
    click.echo(f"Olá {usuario}")
    click.echo(senha)


if __name__ == "__main__":
    hello()
