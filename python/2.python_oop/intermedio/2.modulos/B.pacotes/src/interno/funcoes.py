import typing


def imprime_com_espacos(palavra: typing.Union[str, typing.List[str]]) -> None:
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaço entre suas letras ou strings

    :param palavra: palavra secreta do jogo
    """
    for letra in palavra:
        print(letra, end=" ")
    print()
