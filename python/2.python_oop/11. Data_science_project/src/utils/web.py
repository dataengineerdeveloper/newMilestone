import urllib
import requests
import re
from pathlib import Path
from bs4 import BeautifulSoup
import typing

def download_dados_web (caminho: typing.Union[str, Path],url: str)-> None:
    """
    realiza o download dos dados em um link da web
    
    :param caminho: caminho para extraºçao dos daos
    :param url : endereço do site a ser baixo
    
    """
    r = requests.get(url,stream=True)
    with open(caminho, "wb") as arq:
        arq.write(r.content)