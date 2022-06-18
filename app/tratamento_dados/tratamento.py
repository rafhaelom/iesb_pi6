import os
import sys
from app.logs import logger

class TratamentoArquivo:
    def __init__(self, df, ano, mes) -> None:
        logger.debug('Classe "TratamentoArquivo" iniciada!!!')
        self.df = df  # dataframe completo com os dados.
        self.ano_arq = ano  # ano do arquivo.
        self.mes_arq = mes  # mes do arquivo.
        self.path_base = 'C:/Users/Usuario/Documents/Projetos_git/iesb_pi6/app/dados/base_data/'

    def criarColunas(self):
        """Função para criar colunas de ano e mes em uma posição específica do DataFrame."""
        logger.info('Criando coluna de Ano e Mes.')
        self.df.insert(0, "Ano", self.ano_arq, allow_duplicates=False)
        self.df.insert(1, "Mes", self.mes_arq, allow_duplicates=False)

    def extraiCodMunicipio(self):
        """Função para extrair código do município."""
        logger.info('Extraindo CodMunicipio.')
        self.df.insert(2, "CodMunicipio", self.df.Município.apply(lambda x: x[:7]), allow_duplicates=False)

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
        self.df_remove_line = self.df.copy() 
        self.df_remove_line = self.df_remove_line[:-6]

    def trataNulos(self):
        """Função para trata valores nulos.

        Ex: 
        Valores entrada. 
        index   | V_105001_105
        linha 1 |     2
        linha 2 |     5
        linha 3 |     -
        
        Valores saída. 
        index   | V_105001_105
        linha 1 |     2
        linha 2 |     5
        linha 3 |    None

        """
        logger.info("Tratando Nulos.")
        colunas_df = list(self.df_remove_line.columns)
        #print(colunas_df)
        for col in colunas_df:
            if len(col) >= 12 and col != 'CodMunicipio':
                self.df_remove_line[col].replace(to_replace={'-': None}, inplace=True)
            else:
                pass

    def salvarArquivo(self):
        """Função para salvar o arquivo final após o tratamento."""
        logger.info('Salvando o arquivo em ".csv".')
        self.df_remove_line.to_csv(self.path_base+'SIH_SUS_'+str(self.ano_arq)+'_'+str(self.mes_arq)+'.csv', sep=';', index=False, encoding='latin1')

    def main(self):
        self.criarColunas()
        self.extraiCodMunicipio()
        self.removerColunas()
        self.removerLinhas() 
        self.trataNulos()
        self.salvarArquivo()
        logger.info(f'Fim do tratamento do arquivo.')
        return self.df_remove_line