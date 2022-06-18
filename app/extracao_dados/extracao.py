from msilib.schema import Error
import pandas as pd

from app.logs import logger

class ExtracaoDados:
    def __init__(self, arquivo) -> None:
        logger.debug('Classe "ExtracaoDados" iniciada!!!')
        self.path_raw = 'C:/Users/Usuario/Documents/Projetos_git/iesb_pi6/app/dados/raw_data/'
        self.arquivo = arquivo
        # Dicionário com a chave (nome do mês) e valor (mês em número).
        self.meses = {'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4, 'Mai': 5, 'Jun': 6, \
            'Jul': 7, 'Ago': 8, 'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12}

    def lerArquivo(self, sep=';', encoding='latin-1', header='infer', usecols=None, nrows=None):
        """Função para leitura de arquivos '.csv'."""
        file_name = self.path_raw+self.arquivo
        try:
            logger.info(f'Lendo arquivo "{file_name}"')
            return pd.read_csv(file_name, sep=sep, encoding=encoding, header=header, usecols=usecols, nrows=nrows, lineterminator='\n', on_bad_lines='skip')
        except:
            logger.error(f'Arquivo não encontrado {file_name}')

    def extraiAnoMes(self):
        """Função para extrair o Ano e Mês do arquivo."""
        logger.info(f'Extraindo ano e mês do arquivo.')
        _ano_mes = str(self.df1[0][2])
        self.ano = int(_ano_mes.split('/')[1][:4])    # Extrai o "ano" do arquivo.        
        nome_mes = str(_ano_mes.split('/')[0].split(':')[1])     # Extrai o "mes" do arquivo. 
        self.mes = self.meses.get(f'{nome_mes}')  # Verifica o nome do Mês e retornar o número respectivo ao Mês.
        logger.info(f'Extraido ano {self.ano} e mes {self.mes} do arquivo {self.arquivo}.')
        return self.ano, self.mes

    def main(self):
        """Função main que controla ordem de execução das funções."""
        #self.arquivo = self.listarDiretorio()
        logger.info('Leitura das primeiras linhas para extrair ano e mes.')
        self.df1 = self.lerArquivo(header=None, usecols=[0], nrows=10)  # Leitura das primeiras linhas para extrair ano e mes.
        self.ano_arq, self.mes_arq = self.extraiAnoMes()
        logger.info('Leitura do arquivo completo.')
        self.df2 = self.lerArquivo(header=3)     # Leitura do arquivo completo.
        logger.info(f'Fim da extração dos dados contidos no arquivo.')
        
        return self.df2, self.ano_arq, self.mes_arq     # Retorna dataframe, ano e mes do arquivo.