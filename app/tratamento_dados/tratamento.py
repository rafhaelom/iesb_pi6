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

    def criaNomeColuna(self):
        """Função para criar padrão no nome das colunas de serviço/classificação.
        
        Ex: Nome coluna Original = '105001 105 SERVICO DE ATENCAO EM NEUROLOGIA / NEUROCIRURGIA / 001 NEUROCIRURGIA DO TRAUMA E ANOMALIAS DO DE'
            Nome coluna Nova = 'V_105001_105'
        """
        logger.info('Criando padronização no nome das colunas.')
        colunas_origem = list(self.df.columns)
        nomes_coluna = []
        print(colunas_origem)
        if len(colunas_origem) == 109:
            #print(len(colunas_origem))
            for col in colunas_origem:
                if len(col) > 12 and col != 'CodMunicipio':
                    #print(f"V_{col[:6]}_{col[7:10]}")
                    nomes_coluna.append(f"V_{col[:6]}_{col[7:10]}")
                else:
                    nomes_coluna.append(col)
                    #print("A coluna {0}\n não é a coluna de serviço\n".format(col))

            
            #return self.colunas_novas
        else:
            print('Não possuem as colunas corretas.')
            pass
        colunas_novas = ["Ano", "Mes", "CodMunicipio"] + nomes_coluna
        print(type(colunas_novas))
        self.df1 = self.df.copy()
        self.df1.columns = colunas_novas

    def criarColunas(self):
        """Função para criar colunas de ano e mes em uma posição específica do DataFrame."""
        logger.info('Criando coluna de Ano e Mes.')
        self.df.insert(0, "Ano", self.ano_arq, allow_duplicates=False)
        self.df.insert(1, "Mes", self.mes_arq, allow_duplicates=False)

    def extraiCodMunicipio(self):
        """Função para extrair código do município."""
        logger.info('Extraindo CodMunicipio.')
        self.df.insert(2, "CodMunicipio", self.df.Município.apply(lambda x: x[:7]), allow_duplicates=False)
        #self.df["CodMunicipio"] = self.df["Município"].apply(lambda x: x[:7])

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

    def renomearColunas(self):
        """Função para renomear as colunas de acordo com o padrão definido no projeto, conforme o que se extrai da funcao 'criaNomeColuna'.
        
        Ex: Nome coluna Original = '105001 105 SERVICO DE ATENCAO EM NEUROLOGIA / NEUROCIRURGIA / 001 NEUROCIRURGIA DO TRAUMA E ANOMALIAS DO DE'
            Nome coluna Nova = 'V_105001_105'
        """
        #print(colunas_novas)
        logger.info('Renomeando colunas.')
        #colunas_antigas = list(self.df.columns)
        #print(colunas_antigas)
        print()
        #print(self.colunas_novas)
        #colunas_nomes = {}
        #for _col_antiga, _col_nova in 
        #colunas_nomes = dict(zip(colunas_antigas, self.colunas_novas))
        #print(colunas_nomes)
            #print("Coluna antiga: ", _col_antiga)
            #print("Coluna nova: ", _col_nova)
        #_colunas_nomes[_col_antiga] = (_col_nova)
        #pass

        #print(_colunas_nomes)
        self.df1 = self.df_remove_line.copy()
        self.df1.columns = self.colunas_novas
        #self.df1.rename(columns=colunas_nomes, inplace=True)
        #pass
        print('fim renomear')

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
        if len(colunas_df) == 109:
            for col in colunas_df:
                if len(col) == 12 and col != 'CodMunicipio':
                    self.df_remove_line[col].replace(to_replace={'-': None}, inplace=True)
                else:
                    pass
            
        else:
            pass

        return self.df_remove_line

    def salvarArquivo(self):
        """Função para salvar o arquivo final após o tratamento."""
        logger.info('Salvando o arquivo em ".csv".')
        self.df_remove_line.to_csv(self.path_base+'SIH_SUS_'+str(self.ano_arq)+'_'+str(self.mes_arq)+'.csv', sep=';', index=False, encoding='latin1')

    def main(self):
        #self.criaNomeColuna()
        #self.extraiCodMunicipio()
        self.criarColunas()
        self.extraiCodMunicipio()
        self.removerColunas()
        self.removerLinhas()
        #self.criaNomeColuna()
        #self.renomearColunas()
        #self.df2 = 
        self.df_remove_line = self.trataNulos()
        self.salvarArquivo()
        #print(len(self.df.columns))
        logger.info(f'Fim do tratamento do arquivo.')
        return self.df_remove_line