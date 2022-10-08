class Cachorro:
    """
    Objeto que define as características e ações que um
    cachorro (animal mamífero de 4 patas) pode realizar
    dentro do programa

    :param nome: nome do cachorro
    :param cor: cor do cachorro
    """
    reino: str = "Animalia"
    __reino: str = "Animalia"

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

        print(f"{self.nome} for criado")
        self._latir()

    @staticmethod
    def latir_generico():
        print("Au au au au!")

    def _latir(self) -> None:
        print(f"{self.nome}: Au au au au!")

    def corre(self, vel: int) -> None:
        """
        Faz o cachorro correr

        :param vel: velocidade em km/h de corrida
        """
        print(f"{self.nome}, do reino {self.__reino}, está correndo a {vel} km/h")
        self._latir()
        Cachorro.latir_generico()


rex = Cachorro("Rex", "marrom")
scooby = Cachorro("Scooby", "preta")

print(rex.reino)
rex.corre(40)
rex._latir()
print(rex.__reino)
