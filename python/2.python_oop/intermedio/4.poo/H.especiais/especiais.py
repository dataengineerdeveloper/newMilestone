# https://docs.python.org/3/reference/datamodel.html

from __future__ import annotations

import typing


class Mamifero:
    especie: str

    def __init__(self, especie: str):
        self.especie = especie

    def alimenta(self):
        print("HMM! eu gosto de leite!")


class Cachorro(Mamifero):
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
        super().__init__("Cachorro")

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

    def __str__(self) -> str:
        return f"Cachorro {self.nome} de cor {self.cor}"

    # __repr__

    def __len__(self) -> int:
        return int(self._peso)

    # __getitem__, __setitem__, __contains__, __iter__, __next__

    def __eq__(self, other: Cachorro) -> bool:
        return (
            self.nome == other.nome
            and self.cor == other.cor
            and self.peso == other.peso
            and self.porte == other.porte
        )

    # __lt__, __le__, __ne__, __gt__, __ge__

    def __add__(self, other: typing.Union[float, Cachorro]) -> float:
        if isinstance(other, float):
            return self.peso + other
        elif isinstance(other, Cachorro):
            return self.peso + other.peso
        else:
            raise ValueError("O objeto deve ser um float ou Cachorro")

    # __sub__, __mul__, __truediv__, __pow__

    def __hash__(self) -> int:
        return hash(
            (
                self.nome,
                self.cor,
                self._peso,
                self.porte
            )
        )

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
        self.latir_generico()

    def alimenta(self):
        print(f"Eu {self.nome} estou com fome")
        super().alimenta()


class Labrador(Cachorro):
    personalidade: str

    def __init__(self, nome: str, cor: str, peso: float) -> None:
        """
        Construtor da classe cachorro

        :param nome: nome do cachorro
        :param cor: cor do cachorro
        :param peso: peso do cachorro em kg
        """
        super().__init__(nome, cor, peso, "grande")

        self.personalidade = "brincalhão"

    def corre(self, vel: int) -> None:
        """
        Faz o cachorro correr

        :param vel: velocidade em km/h de corrida
        """
        print(f"De forma {self.personalidade}")
        super().corre(vel)

    def alimenta(self):
        print(f"Eu {self.nome} um labrador parrudo, estou com muita fome")
        Mamifero.alimenta(self)


rex = Cachorro("Rex", "marrom", 30, "grande")
rex2 = Cachorro("Rex", "marrom", 30, "grande")
scooby = Cachorro("Scooby", "preta", 10, "grande")
marley = Labrador("Marley", "loira", 30)

print(rex)
print(scooby)
print(marley)
print(len(rex))
print(rex == rex2)
print(rex + 10.)
print(rex + marley)

d = dict()
d[rex] = 1

print(d[rex])