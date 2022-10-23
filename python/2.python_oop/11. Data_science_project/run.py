'''
comandos que vou ter para correr na linha de comandos

'''

import click
from src.Aquisicao.opcoes import EnumETL
from src.Aquisicao.opcoes import ETL_DICT
import src.configs as conf_geral


@click.group()
def cli():
    pass

@cli.group()
def aquisicao():
    """
    grupo de comandos que executam as funcoes de aquisicao
    """
    pass


@aquisicao.command()
@click.option("--etl",type = click.Choice([s.value for s in EnumETL]) ,  help='nome do Etl a ser executado')
@click.option('--entrada', default=conf_geral.PASTA_DADOS,  help='string com caminho para pasta de entrada')
@click.option('--saida', default=conf_geral.PASTA_SAIDA_AQUISICAO,  help='string com caminho para pasta de saida')
@click.option('--criar_caminho', default=True,  help='flag indicando se devemos criar os caminhos')

#metodo que vai correr o meu ETL
def processa_dados(etl: str, entrada: str,  saida: str,  criar_caminho: bool )->None:
    ''' instanciar um classe de objecto etl e chamar o pipeline da Class
    
    :param etl: nome do etl a ser executado
    :param entrada:  string com caminho para pasta de entrada
    :param saida:  string com caminho para pasta de saida
    :param criar_caminho: flag indicando se devemos criar os caminhos
    '''
    objecto = ETL_DICT[EnumETL(etl)](entrada, saida, criar_caminho)
    objecto.pipeline()
        
if __name__ == '__main__':
    cli()