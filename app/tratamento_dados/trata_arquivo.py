# Importação de Bibliotecas.
from asyncio.log import logger
import sys
import os
import pandas as pd
import logging

class TrataArquivo:
    def __init__(self) -> None:
        self.path_raw = 'C:/Users/Usuario/Documents/Projetos_git/iesb_pi6/dados/raw_data/'
        self.path_base = 'C:/Users/Usuario/Documents/Projetos_git/iesb_pi6/dados/base_data/'

        # Dicionário com a chave (nome do mês) e valor (mês em número).
        self.meses = {'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4, 'Mai': 5, 'Jun': 6, \
            'Jul': 7, 'Ago': 8, 'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12}

        '''
        A formatação abaixo permite personalizarmos
        a forma como o log será mostrado para nós.
        '''
        # DateTime:Level:Arquivo:Mensagem
        log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
        
        '''
        Aqui definimos as configurações do modulo.

        filename = 'nome do arquivo em que vamos salvar a mensagem do log.'
        filemode = 'É a forma em que o arquivo será gravado.'
        level = 'Level em que o log atuará'
        format = 'Formatação da mensagem do log'
        '''
        logging.basicConfig(filename='exemplo.log',
                            # w -> sobrescreve o arquivo a cada log
                            # a -> não sobrescreve o arquivo
                            filemode='w',
                            level=logging.DEBUG,
                            format=log_format)

        # Instancia do objeto getLogger()
        self.logger = logging.getLogger('root')

    def listarDiretorio(self) -> list:
        """Função para listar os arquivos de um diretório."""
        try:
            self.logger.info(f'{self.path_raw}')
            return os.listdir(self.path_raw)
        except OSError as ose:
            logger.error(f'Diretório Inválido ou Inexistente!!! {ose}')
            print(f'{self.path_raw} type: {type(self.path_raw)}')
            logger.error(f'{self.path_raw} type: {type(self.path_raw)}')
            print(f"Diretório Inválido ou Inexistente!!! {ose}")
            sys.exit()

    def lerArquivo(self, arquivo, sep=';', encoding='latin-1', header='infer', usecols=None, nrows=None):
        """Função para leitura de arquivos '.csv'."""

        return pd.read_csv(self.path_raw+arquivo, sep=sep, encoding=encoding, header=header, usecols=usecols, \
                        nrows=nrows, lineterminator='\n', on_bad_lines='skip')

    def extraiAnoMes(self, df):
        """Função para extrair o Ano e Mês do arquivo."""
        print("Entrou na função!!!")
        print(df)
        _ano_mes = str(df[0][2])
        print(_ano_mes)

        # Extrai o "ano" do arquivo.
        ano = int(_ano_mes.split('/')[1][:4])
        # Extrai o "mes" do arquivo.
        mes = self.meses.get(str(_ano_mes.split('/')[0].split(':')[1])) # Verifica o nome do Mês e retornar o número respectivo ao Mês.

        return ano, mes

if __name__ == '__main__':
    trata = TrataArquivo()
    arquivo = trata.listarDiretorio()[0]
    df = trata.lerArquivo(arquivo, header=None, usecols=[0], nrows=10)
    ano, mes = trata.extraiAnoMes(df)
    print(ano, mes)
