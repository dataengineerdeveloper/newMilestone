import random
import time
import typing

FORCAIMG = [
    """

      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========""",
]


def main():
    """
    Função Principal do programa
    """
    global FORCAIMG

    letras_erradas = list()
    letras_acertadas = list()

    # lista as palavras disponíveis para o jogo
    palavras = le_palavras()

    # seleciona uma palavra aleatória
    palavra_secreta = gera_palavra_aleatoria(palavras).upper()

    # cria o loop do jogo
    jogando = True
    while jogando:
        # imprime o estado do jogo atual
        time.sleep(0.3)
        imprime_jogo(letras_erradas, letras_acertadas, palavra_secreta)
        time.sleep(0.3)

        # recebe um palpite do jogador
        palpite = recebe_palpite(letras_erradas + letras_acertadas)

        # adiciona o palpite ao dicionário adequado
        if palpite in palavra_secreta:
            letras_acertadas.append(palpite)
        else:
            letras_erradas.append(palpite)

        # verifica se o usuário ganhou o jogo
        if verifica_se_ganhou(palavra_secreta, letras_acertadas):
            time.sleep(0.3)
            print("Exato! A palavra secreta é " + palavra_secreta + "! Você ganhou!!")
            jogando = False

        # verifica se o usuário perdeu o jogo
        elif len(letras_erradas) == len(FORCAIMG) - 1:
            time.sleep(0.3)
            print("Você excedeu o seu limite de palpites!")
            print(
                "Depois de "
                + str(len(letras_erradas))
                + " letras erradas e "
                + str(len(letras_acertadas)),
                end=" ",
            )
            print("palpites corretos, a palavra era " + palavra_secreta + ".")

            jogando = False

        # se o usuário terminar o jogo
        if not jogando:
            # pede para jogar novamente
            time.sleep(0.3)
            if jogar_novamente():
                letras_erradas = list()
                letras_acertadas = list()
                jogando = True
                palavra_secreta = gera_palavra_aleatoria(palavras).upper()


def le_palavras() -> typing.List[str]:
    """
    Le arquivo com palavras que podem ser utilizadas
    como parte do jogo
    """
    with open("palavras.txt") as f:
        return f.readlines()


def gera_palavra_aleatoria(palavras: str) -> typing.List[str]:
    """
    Função que retorna uma string a partir da
    lista de palavras

    :param palavras: lista com palavras que podem ser sorteadas
    :return: palavra secreta do jogo
    """
    return random.choice(palavras).replace("\n", "")


def imprime_com_espacos(palavra: typing.Union[str, typing.List[str]]) -> None:
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaço entre suas letras ou strings

    :param palavra: palavra secreta do jogo
    """
    for letra in palavra:
        print(letra, end=" ")
    print()


def imprime_jogo(
    letras_erradas: typing.List[str],
    letras_acertadas: typing.List[str],
    palavra_secreta: str,
) -> None:
    """
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta

    :param letras_erradas: lista de letras chutadas incorretamente
    :param letras_acertadas: lista de letras chutadas corretamente
    :param palavra_secreta: palavra secreta do jogo
    """
    global FORCAIMG
    print(FORCAIMG[len(letras_erradas)] + "\n")

    print("Letras Erradas:", end=" ")
    imprime_com_espacos(letras_erradas)

    vazio = "_" * len(palavra_secreta)
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] in letras_acertadas:
            vazio = vazio[:i] + palavra_secreta[i] + vazio[i + 1 :]

    imprime_com_espacos(vazio)


def recebe_palpite(palpites_feitos: typing.List[str]) -> str:
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado

    :param palpites_feitos: lista de letras chutadas anteriormente
    :return: nova letra chutada
    """
    while True:
        palpite = input("Advinhe uma letra.\n").upper()

        if len(palpite) != 1:
            print("Coloque uma única letra.")
        elif palpite in palpites_feitos:
            print("Você já chutou esta letra. Escolha novamente.")
        elif not "A" <= palpite <= "Z":
            print("Por favor escolha apenas letras.")
        else:
            return palpite


def jogar_novamente() -> bool:
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta

    :return: True se o jogador informou que deseja jogar novamente
    """
    return input("Você quer jogar novamente? (sim ou nao)\n").upper().startswith("S")


def verifica_se_ganhou(
    palavra_secreta: str, letras_acertadas: typing.List[str]
) -> bool:
    """
    Função que verifica se o usuário acertou todas as
    letras da palavra secreta

    :param palavra_secreta: palavra secreta do jogo
    :param letras_acertadas: lista de letras chutadas corretamente
    :return: booleano informando se o jogador ganhou o jogo
    """
    return set(list(palavra_secreta)) == set(letras_acertadas)


main()
