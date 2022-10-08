import typing


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

    __faixa_peso = {"pequeno": (2, 10), "medio": (10, 20), "grande": (20, 40)}

    nome: str
    cor: str
    _peso: float
    porte: str
    saude: str

    def __init__(self, nome: str, cor: str, peso: float, porte: str) -> None:
        """
        Construtor da classe cachorro

        :param nome: nome do cachorro
        :param cor: cor do cachorro
        :param peso: peso do cachorro em kg
        :param porte: porte do animal (pequeno, medio, grande)
        """
        assert porte in ("pequeno", "medio", "grande"), (
            "O porte do animal deve ser pequeno, medio ou grande -"
            f"{porte} não é válido"
        )

        self.nome = nome
        self.cor = cor
        self._peso = peso
        self.porte = porte
        self.saude = self.calcula_saude()

        print(f"{self.nome} for criado")
        self._latir()

    def calcula_saude(self) -> str:
        peso_min, peso_max = self.__faixa_peso[self.porte]
        if peso_min <= self._peso < peso_max:
            return "Saúdavel"
        elif self._peso < peso_min:
            return "Magro demais"
        else:
            return "Gordo demais"

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, value: float) -> None:
        self._peso = value
        self.saude = self.calcula_saude()

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


rex = Cachorro("Rex", "marrom", 30, "grande")
scooby = Cachorro("Scooby", "preta", 10, "grande")

print(rex.saude)
print(scooby.saude)

scooby.peso = 30
print(scooby.saude)
