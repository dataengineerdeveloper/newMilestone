class Cachorro:
    """
    Objeto que define as características e ações que um
    cachorro (animal mamífero de 4 patas) pode realizar
    dentro do programa

    :param nome: nome do cachorro
    :param cor: cor do cachorro
    """
    reino: str = "Animalia"

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
        self.latir_generico()

    @staticmethod
    def latir_generico():
        print("Au au au au!")

    def latir(self) -> None:
        print(f"{self.nome}: Au au au au!")

    def corre(self, vel: int) -> None:
        """
        Faz o cachorro correr

        :param vel: velocidade em km/h de corrida
        """
        print(f"{self.nome}, do reino {self.reino}, está correndo a {vel} km/h")
        self.latir()
        Cachorro.latir_generico()


rex = Cachorro("Rex", "marrom")
scooby = Cachorro("Scooby", "preta")

rex.latir()
scooby.latir()

Cachorro.latir_generico()
rex.latir_generico()

print(Cachorro.reino)
print(rex.reino)

rex.corre(40)

rex.reino = "Plantae"
print(Cachorro.reino)
rex.corre(40)

Cachorro.reino = "Plantae"
print(Cachorro.reino)
scooby.corre(40)
