import os
import sys
from app.logs import logger

class TratamentoArquivo:
    def __init__(self, df, ano, mes) -> None:
        logger.debug('Classe "TratamentoArquivo" iniciada.')
        self.df = df  # dataframe completo com os dados.
        self.ano_arq = ano  # ano do arquivo.
        self.mes_arq = mes  # mes do arquivo.

    def criaNomeColuna(self):
        """Função para criar padrão no nome das colunas de serviço/classificação.
        
        Ex: Nome coluna Original = '105001 105 SERVICO DE ATENCAO EM NEUROLOGIA / NEUROCIRURGIA / 001 NEUROCIRURGIA DO TRAUMA E ANOMALIAS DO DE'
            Nome coluna Nova = 'V_105001_105'
        """
        logger.info('Criando padronização no nome das colunas.')
        colunas_origem = list(self.df.columns)
        nomes_coluna = []

        if len(colunas_origem) == 108:
            #print(len(colunas_origem))
            for col in colunas_origem:
                if len(col) >= 10:
                    #print(f"V_{col[:6]}_{col[7:10]}")
                    nomes_coluna.append(f"V_{col[:6]}_{col[7:10]}")
                else:
                    #print("A coluna {0}\n não é a coluna de serviço\n".format(col))
                    pass

            self.colunas_novas = ["Ano", "Mes", "CodMunicipio"] + nomes_coluna
            return self.colunas_novas
        else:
            pass

    def extraiCodMunicipio(self):
        """Função para extrair código do município."""
        logger.info('Extraindo CodMunicipio.')
        self.df.insert(0, "CodMunicipio", self.df.Município.apply(lambda x: x[:7]), allow_duplicates=False)
        #self.df["CodMunicipio"] = self.df["Município"].apply(lambda x: x[:7])

    def criarColunas(self):
        """Função para criar colunas de ano e mes em uma posição específica do DataFrame."""
        logger.info('Criando coluna de Ano e Mes.')
        self.df.insert(0, "Ano", self.ano_arq, allow_duplicates=False)
        self.df.insert(1, "Mes", self.mes_arq, allow_duplicates=False)
    
    def removerColunas(self):
        """Função para remover coluna não utilizada."""
        logger.info('Removendo coluna não utilizada.')
        self.df.drop(['Município'], axis=1, inplace=True)
        self.df.drop(['Total\r'], axis=1, inplace=True)

    def removerLinhas(self):
        """Função para remover linhas desnecessárias do DataFrame.
        
        Ex: Em um arquivo, serão removidas as linhas 1260 até 1264, por padrão do '.csv' gerado, as 'últimas 5' são informativas, portanto, serão excluídas.
            linha 1258 =    522140 Trindade
            linha 1259 =    530010 Brasília
            linha 1260 =    Total
            linha 1261 =    Fonte: Ministério da Saúde - Sistema de Informações Hospitalares do SUS (SIH/SUS)
            linha 1262 =    Notas:
            linha 1263 =     
            linha 1264 =    Dados referentes aos últimos seis meses, sujeitos a atualização.
        """
        logger.info('Removendo linhas desnecessárias.')
        self.df = self.df[:-6]

    def renomearColunas(self):
        """Função para renomear as colunas de acordo com o padrão definido no projeto, conforme o que se extrai da funcao 'criaNomeColuna'.
        
        Ex: Nome coluna Original = '105001 105 SERVICO DE ATENCAO EM NEUROLOGIA / NEUROCIRURGIA / 001 NEUROCIRURGIA DO TRAUMA E ANOMALIAS DO DE'
            Nome coluna Nova = 'V_105001_105'
        """
        logger.info('Renomeando colunas.')
        colunas_antigas = list(self.df.columns)
        colunas_nomes = {}
        for i, j in zip(colunas_antigas, self.colunas_novas):
            #print("Col2: ", i)
            #print("Colunas: ", j)
            colunas_nomes[i] = (j)

        self.df.rename(columns=colunas_nomes, inplace=True)

    def main(self):
        _colunas_novas = self.criaNomeColuna()
        self.extraiCodMunicipio()
        self.criarColunas()
        self.removerColunas()
        self.removerLinhas()
        self.renomearColunas()
        print(self.df.columns)