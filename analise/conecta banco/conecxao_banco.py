# Importando Bilbiotecas.
import os
from dotenv import load_dotenv
# Carrega variáveis de ambiente.
load_dotenv()

import psycopg2
import pandas as pd

class ConectaBanco:
    def __init__(self) -> None:
        self.host = os.getenv('BD_HOST')
        self.port = os.getenv('BD_PORT')
        self.dbname = os.getenv('BD_DBNAME')
        self.user = os.getenv('BD_USER')
        self.password = os.getenv('BD_PASSWORD')

# Função para criar tabela no banco
def conecta_banco(self):
    # Conexão ao banco de dados.
    self.conn = psycopg2.connect(host=self.host, port=self.port, dbname=self.dbname, user=self.user, password=self.password)
    return self.conn

# Função para realizar consultas no banco de dados.
def consultar_banco(self, sql, colunas):
    registros = []
    # Conecta ao banco de dados.
    conn = self.conecta_banco()
    cur = conn.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    
    for rec in recset:
        registros.append(rec)
    
    conn.close()
    
    # Tranformando os dados da consulta no PostegreSQL em DataFrame
    self.df = pd.DataFrame(registros, columns=colunas)
    return self.df

colunas_dic = ["ID_SIH_DIC", "COD_SERVICO_CLASSIFICACAO", "DESC_SERVICO_CLASSIFICACAO", "COD_SERVICO", \
                "DESC_SERVICO", "COD_CLASSIFICACAO", "DESC_CLASSIFICACAO", "QUANTIDADE_APROVADA"]
banco = ConectaBanco()
df = banco.consulta_banco(sql='select * from sih_sus.tb_sus_sih_dicionario', colunas=colunas_dic)
print(df)