''' 
Estrutura das opçoes

este ficheiro consiste em definir quais os etl existentes e qua

'''

from enum import Enum

class EnumETL(Enum):
    censo_escolar="CENSO_ESCOLAR"

# chave =  Enum
# Valor = Classe de objecto ETL
ETL_DICT = {}