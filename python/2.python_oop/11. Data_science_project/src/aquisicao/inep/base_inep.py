import abc
from pathlib import Path
import typing
from src.Aquisicao.base_etl import BaseETL
from src.utils.web import download_dados_web

import pandas as pd


import urllib
import requests
import re
from pathlib import Path
from bs4 import BeautifulSoup
import os



class BaseINEPETL(BaseETL, abc.ABC):
    """
    classe que estrutura como qualquer objecto de ETL deve funcionar para baixar dados do INEP
    
    """

    URL: str = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/"

    
    def __init__(self, entrada: str,  saida: str, base: str, criar_caminho: bool =  True)-> None:
        """
        > como qualquer Etl é preciso ter um caminho de entrada e saida:
        
        instancia o objecto de ETL INEP
        :param entrada:  string com caminho para pasta de entrada
        :param saida:  string com caminho para pasta de saida
        :param base: nome da base que vai na URL do INEP
        :param criar_caminho: flag indicando se devemos criar os caminhos
        
        """
     
        super().__init__(entrada,  saida, criar_caminho)
        
        self._url=f"{self.URL}/{base}"
        
    
    def ler_pagina_inep(self)-> typing.Dict[str, str]:
        
        """
        realiza o web scraping da pagina de dados dos inep

        return:  nome do arquivo e link para a pagina
        """
        
        html = urllib.request.urlopen(self._url).read()
        soup = BeautifulSoup(html,  features="html.parser")
        return {tag["href"].split("_")[-1]: tag["href"] for tag in soup.find_all("a", {"class":"external-limk"})}
        
    def dicionario_para_baixar(self) -> typing.Dict[str, str]:
        """
        le os conteudos da pasta de dados e seleciona apenas os arquivos a serem baixados como complementares
        :return :  dicionario com o nome do arquivo e link para a pagina
        """
        para_baixar =  self.ler_pagina_inep()
        baixados = os.listdir(str(self.caminho_entrada))
        return {arq:  link for arq,  link in para_baixar.items() if arq not in baixados}
    

    def donwload_conteudo(self) -> None:
        """
        realiza o donwload dos dados INEP para uma pasta local
        
        
        """
        
        for arq, link in self.dicionario_para_baixar().items():
            caminho_arq =  self.caminho_saida /arq
            download_dados_web(caminho_arq, link)
            
        

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