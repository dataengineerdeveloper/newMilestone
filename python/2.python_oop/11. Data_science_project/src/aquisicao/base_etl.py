import abc
from pathlib import Path
import typing
import pandas as pd

class BaseETL(abc.ABC):
    """
    classe que estrutura como qualquer objecto de ETL deve funcionar
    
    """
    
    #descrição do objecto o type int destas variaveis
    caminho_entrada:Path
    caminho_saida: Path
    # vamos aguardar receber dados de vários anos
    _dados_entrada:typing.Dict[str,pd.DataFrame]
    _dados_saida:typing.Dict[str,pd.DataFrame]
    
    def __init__(self, entrada:str,  saida:str, criar_caminho: bool =  True)-> None:
        """
        > como qualquer Etl é preciso ter um caminho de entrada e saida:
        
        instancia o objecto de ETL Base
        :param entrada:  string com caminho para pasta de entrada
        :param saida:  string com caminho para pasta de saida
        :param criar_caminho: flag indicando se devemos criar os caminhos
        
        """
        # criação de parametros
        self.caminho_entrada = Path(entrada)
        self.caminho_saida = Path(saida)
        
        if criar_caminho:
            self.caminho_entrada.mkdir(parents=True,exist_ok=True)
            self.caminho_saida.mkdir(parents=True,exist_ok=True)
        
        
        '''
        1 _ protected
        2 __ private
        '''
        self._dados_entrada = None
        self._dados_saida = None
     
     
    '''
     se os dados de entrada nao tiverem sido definidos chama o metodos de extract,  depois dá o return nos dados de entrada
    '''   
    @property
    def dados_entrada(self)-> typing.Dict[str,pd.DataFrame]:
        '''
        acessa o dicionario de dados de entrada
        return:  dicionario como o nome do arquivo e umm dataframe com os dados
        '''
        if self._dados_entrada is None:
            self.extract()
        return self._dados_entrada
    
    @property
    def dados_saida(self)-> typing.Dict[str,pd.DataFrame]:
        '''
        acessa o dicionario de dados de saida
        return:  dicionario como o nome do arquivo e umm dataframe com os dados
        '''
        if self._dados_saida is None:
            self.extract()
        return self._dados_saida
    
    '''
    >num objecto de ETL é preciso ter um extratc,  trasnform e um load,  ou seja é preciso ter um metdo para cada um
    
    > vou ter de criar um decorator:
        > para cada tipo de extraçao que for fazer,  vou ter de definir com o é que é esse objecto,  como tal vamos ter de usar um decorador
        > qualquer class filha do objecto ETL tem de gerar uma definição desse method de extract,  então não posso importar da class pai.
        > por isso todas as class filhas tem defenir como vai ser feita a extração
    '''
    @abc.abstractclassmethod
    def extract(self) -> None:
        '''
        extrai os dados deo objecto
        '''
        pass
    
    @abc.abstractclassmethod
    def transform(self) -> None:
        '''
        transforma os dados e os adequa para os formatos de saída de interesse
        
        '''
        
        pass     
    @abc.abstractclassmethod
    def load(self) -> None:
        '''
        aqui podemos definir alguns tipos de estrutura que queremos receber
        
        exporta os dados transformandos
        '''
        for arq,  df in self.dados_saida.items():
            df.to_parquet(self.caminho_saida / arq,  index=False)
            
    
    def pipeline(self)->None:
        """
        executa o pipeline complete de tratamento de dados
        
        """
        self.extract()
        self.transform()
        self.load()