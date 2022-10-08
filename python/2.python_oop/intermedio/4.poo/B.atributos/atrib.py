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


rex = Cachorro("Rex", "marrom")
scooby = Cachorro("Scooby", "preta")

print(rex.nome)
print(rex.cor)
print(scooby.nome)
print(scooby.cor)

rex.nome = "Buddy"
print(rex.nome)

rex.peso = 40
print(rex.peso)
print(scooby.peso)
