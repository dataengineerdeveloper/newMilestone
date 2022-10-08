import pandas as pd
import typing
from pathlib import Path


class _BaseDeDados:
    """
    Classe que representa uma base de dados a ser carregada
    na memória.

    A base deve conter uma pasta de entrada e saída, para que
    os dados possam ser carregados e, após o processamento,
    salvo nos caminhos especificados.

    Cada base carregada é colocada no dicionário de "_dados_entrada",
    na qual cada chave corresponde a um nome da base e cada valor ao
    data frame carregado.

    Cada base a ser exportada é colocada no dicionário "_dados_saida",
    na qual cada chave corresponde a um nome da base e cada valor ao
    data frame a ser salvo.

    O objeto é construído com 3 métodos pré definidos:
    - carregar: Carrega as bases em _pasta_entrada de dados no _dados_entrada
    - processar: Processa os dados e armazena o resultado em _dados_saida
    - exportar: Salva os dados em _dados_saida no caminho _pasta_saida

    Como o processamento, carregamento e exportação de cada base será diferente
    este objeto contém, também, os métodos de _carregar, _processar, _exportar
    que são protegidos (não espera-se que um usuário os acesse) e devem ser
    sobre-escritos pelas classe filha desse objeto.

    Além disso, este objeto vem com as propriedades dados_entrada e dados_saida
    que são criadas como meios de acessar os conteúdos de _dados_entrada e _dados_saida
    sempre garantindo que estes estejam devidamente preenchidos.

    CUIDADO!!! A propriedade dados_entrada chama o método carregar, portanto não se
    deve referenciar essa propriedade em carregar e _carregar.
    O mesmo vale para os dados_saida com os métodos processar e _processar.
    """

    _pasta_entrada: Path
    _pasta_saida: Path
    _dados_entrada: typing.Dict[str, pd.DataFrame]
    _dados_saida: typing.Dict[str, pd.DataFrame]

    def __init__(
        self, entrada: typing.Union[str, Path], saida: typing.Union[str, Path]
    ) -> None:
        """
        Inicializa o objeto de Base de Dados

        :param entrada: caminho da pasta de entrada
        :param saida: caminho da pasta de saida
        """
        self._pasta_entrada = Path(entrada)
        self._pasta_saida = Path(saida)
        self._dados_entrada = dict()
        self._dados_saida = dict()

    @property
    def dados_entrada(self) -> typing.Dict[str, pd.DataFrame]:
        """
        Propriedade que permite acessar o atributo _dados_entrada
        de forma que este sempre seja não vazio

        :return: dados carregados para processamento
        """
        if len(self._dados_entrada) == 0:
            self.carregar()
        return self._dados_entrada

    @property
    def dados_saida(self) -> typing.Dict[str, pd.DataFrame]:
        """
        Propriedade que permite acessar o atributo _dados_saida
        de forma que este sempre seja não vazio

        :return: dados processados para exportação
        """
        if len(self._dados_saida) == 0:
            self.processar()
        return self._dados_saida

    def _carregar(self) -> None:
        """
        Carrega os dados da base a ser processada no objeto
        dentro do atributo _dados_entrada
        """
        raise NotImplementedError

    def _processar(self) -> None:
        """
        Aplica alterações para a base de dados carregada na
        propriedade de dados_entrada e gera uma nova base
        em _dados_saida
        """
        raise NotImplementedError

    def _exportar(self) -> None:
        """
        Exporta os dados da propriedade dados_saida para o disco
        """
        raise NotImplementedError

    @property
    def __nome(self) -> str:
        return str(self.__class__).split(".")[-1].replace("'", "").replace(">", "")

    def carregar(self) -> None:
        """
        Carrega os dados da base a ser processada no objeto
        dentro do atributo _dados_entrada
        """
        print(f"Carregando bases para {self.__nome}", end="...")
        self._carregar()
        print("OK!")

    def processar(self) -> None:
        """
        Aplica alterações para a base de dados carregada na
        propriedade de dados_entrada e gera uma nova base
        em _dados_saida
        """
        print(f"Processando bases para {self.__nome}", end="...")
        self._processar()
        print("OK!")

    def exportar(self) -> None:
        """
        Exporta os dados da propriedade dados_saida para o disco
        """
        print(f"Exportando bases para {self.__nome}", end="...")
        self._exportar()
        print("OK!")

    def pipeline(self) -> None:
        """
        Executa o pipeline de processamento de dados
        """
        self.carregar()
        self.processar()
        self.exportar()
