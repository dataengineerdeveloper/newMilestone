class Cachorro:
    """
    Objeto que define as características e ações que um
    cachorro (animal mamífero de 4 patas) pode realizar
    dentro do programa

    :param nome: nome do cachorro
    :param cor: cor do cachorro
    """

    nome: str
    cor: str

    def __init__(self, nome: str, cor: str) -> None:
        """
        Construtor da classe cachorro

        :param nome: nome do cachorro
        :param cor: cor do cachorro
        """
        self.nome = nome
        self.cor = cor

    def latir(self) -> None:
        print(f"{self.nome}: Au au au au!")

    def corre(self, vel: int) -> None:
        """
        Faz o cachorro correr

        :param vel: velocidade em km/h de corrida
        """
        print(f"{self.nome} está correndo a {vel} km/h")


rex = Cachorro("Rex", "marrom")
scooby = Cachorro("Scooby", "preta")

rex.latir()
scooby.latir()

Cachorro.latir(rex)

rex.corre(40)
Cachorro.corre(scooby, 50)
