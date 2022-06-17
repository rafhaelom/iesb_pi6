import os
import sys
from app.logs import logger

class TratamentoArquivo:
    def __init__(self, df, ano, mes) -> None:
        logger.debug('Classe "TratamentoArquivo" iniciada.')
        self.df = df
        self.ano_arq = ano
        self.mes_arq = mes

    def extraiCodMunicipio(self):
        """Função para extrair código do município."""
        logger.info('Extraindo CodMunicipio.')
        self.df["CodMunicipio"] = self.df["Município"].apply(lambda x: x[:7])

    def criaNomeColuna(self):
        """Função para criar padrão no nome das colunas de serviço/classificação."""
        logger.info('Criando padronização no nome das colunas.')
        colunas_origem = list(self.df.columns)
        nomes_coluna = []
        try:
            if len(colunas_origem) == 109:
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
        
        except ValueError as V:
            print(V)
            print(V)
            print("Valor digitado incorreto apenas numeros inteiros:")
            pass
        except Exception as E:
            print(E)
            print(E)
        

    def main(self):
        self.criaNomeColuna()
        self.extraiCodMunicipio()
