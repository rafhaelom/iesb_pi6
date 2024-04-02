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




# Cria coluna com soma de servicos hospitalares.
df_qt["105"] = df_qt["V_105001"] + df_qt["V_105002"] + df_qt["V_105003"] + df_qt["V_105004"] + df_qt["V_105005"] + df_qt["V_105006"] + df_qt["V_105007"] + df_qt["V_105008"] + df_qt["V_105009"]
df_qt["107"] = df_qt["V_107008"]
df_qt["112"] = df_qt["V_112001"] + df_qt["V_112003"]
df_qt["113"] = df_qt["V_113001"] + df_qt["V_113002"] + df_qt["V_113003"] + df_qt["V_113004"]
df_qt["114"] = df_qt["V_114006"] + df_qt["V_114007"]
df_qt["115"] = df_qt["V_115001"] + df_qt["V_115002"] + df_qt["V_115003"] + df_qt["V_115004"] + df_qt["V_115005"] + df_qt["V_115007"]
df_qt["116"] = df_qt["V_116002"] + df_qt["V_116003"] + df_qt["V_116004"] + df_qt["V_116005"]
df_qt["117"] = df_qt["V_117001"] + df_qt["V_117002"]
df_qt["120"] = df_qt["V_120001"] + df_qt["V_120002"] + df_qt["V_120003"]
df_qt["121"] = df_qt["V_121000"] + df_qt["V_121001"] + df_qt["V_121002"] + df_qt["V_121003"] + df_qt["V_121004"] + df_qt["V_121006"] + df_qt["V_121007"] + df_qt["V_121008"] + df_qt["V_121009"] + df_qt["V_121010"] + df_qt["V_121011"] + df_qt["V_121012"]
df_qt["122"] = df_qt["V_122000"] + df_qt["V_122001"] + df_qt["V_122003"] + df_qt["V_122004"] + df_qt["V_122005"] + df_qt["V_122007"] + df_qt["V_122008"]
df_qt["123"] = df_qt["V_123002"] + df_qt["V_123006"]
df_qt["125"] = df_qt["V_125001"] + df_qt["V_125002"] + df_qt["V_125004"] + df_qt["V_125006"] + df_qt["V_125007"]
df_qt["126"] = df_qt["V_126001"] + df_qt["V_126002"] + df_qt["V_126003"] + df_qt["V_126004"] + df_qt["V_126005"] + df_qt["V_126006"] + df_qt["V_126007"] + df_qt["V_126008"]
df_qt["127"] = df_qt["V_127001"]
df_qt["128"] = df_qt["V_128000"] + df_qt["V_128001"] + df_qt["V_128002"] + df_qt["V_128003"] + df_qt["V_128004"]
df_qt["131"] = df_qt["V_131000"] + df_qt["V_131001"] + df_qt["V_131002"] + df_qt["V_131003"] + df_qt["V_131005"] + df_qt["V_131006"] + df_qt["V_131007"]
df_qt["132"] = df_qt["V_132001"] + df_qt["V_132002"] + df_qt["V_132003"] + df_qt["V_132004"] + df_qt["V_132005"]
df_qt["133"] = df_qt["V_133001"] + df_qt["V_133002"] + df_qt["V_133003"]
df_qt["134"] = df_qt["V_134003"] + df_qt["V_134011"]
df_qt["135"] = df_qt["V_135001"] + df_qt["V_135002"] + df_qt["V_135003"] + df_qt["V_135004"] + df_qt["V_135005"] + df_qt["V_135007"] + df_qt["V_135008"] + df_qt["V_135010"] + df_qt["V_135011"] + df_qt["V_135013"]
df_qt["140"] = df_qt["V_140000"] + df_qt["V_140001"] + df_qt["V_140002"] + df_qt["V_140003"] + df_qt["V_140004"] + df_qt["V_140005"] + df_qt["V_140006"] + df_qt["V_140012"] + df_qt["V_140019"]
df_qt["142"] = df_qt["V_142001"] + df_qt["V_142002"] + df_qt["V_142003"] + df_qt["V_142004"]
df_qt["145"] = df_qt["V_145000"] + df_qt["V_145001"] + df_qt["V_145002"] + df_qt["V_145003"] + df_qt["V_145005"] + df_qt["V_145006"] + df_qt["V_145008"] + df_qt["V_145009"] + df_qt["V_145011"]
df_qt["149"] = df_qt["V_149001"] + df_qt["V_149005"] + df_qt["V_149006"] + df_qt["V_149008"] + df_qt["V_149014"] + df_qt["V_149015"] + df_qt["V_149016"]
df_qt["151"] = df_qt["V_151001"] + df_qt["V_151003"]
df_qt["153"] = df_qt["V_153002"]
df_qt["154"] = df_qt["V_154001"] + df_qt["V_154002"]
df_qt["155"] = df_qt["V_155001"] + df_qt["V_155002"] + df_qt["V_155003"]
df_qt["169"] = df_qt["V_16900"]



sns.set_theme(style="dark")
plt.figure(figsize=(16, 5))

sns.barplot(data=df_qt, x="ANO", y="105")
sns.barplot(data=df_qt, x="ANO", y="107")
sns.barplot(data=df_qt, x="ANO", y="112")
sns.barplot(data=df_qt, x="ANO", y="113")
sns.barplot(data=df_qt, x="ANO", y="114")
sns.barplot(data=df_qt, x="ANO", y="115")
sns.barplot(data=df_qt, x="ANO", y="116")
sns.barplot(data=df_qt, x="ANO", y="117")
sns.barplot(data=df_qt, x="ANO", y="120")
sns.barplot(data=df_qt, x="ANO", y="121")
sns.barplot(data=df_qt, x="ANO", y="122")
sns.barplot(data=df_qt, x="ANO", y="123")
sns.barplot(data=df_qt, x="ANO", y="125")
sns.barplot(data=df_qt, x="ANO", y="126")
sns.barplot(data=df_qt, x="ANO", y="127")
sns.barplot(data=df_qt, x="ANO", y="128")
sns.barplot(data=df_qt, x="ANO", y="131")
sns.barplot(data=df_qt, x="ANO", y="132")
sns.barplot(data=df_qt, x="ANO", y="133")
sns.barplot(data=df_qt, x="ANO", y="134")
sns.barplot(data=df_qt, x="ANO", y="135")
sns.barplot(data=df_qt, x="ANO", y="140")
sns.barplot(data=df_qt, x="ANO", y="142")
sns.barplot(data=df_qt, x="ANO", y="145")
sns.barplot(data=df_qt, x="ANO", y="149")
sns.barplot(data=df_qt, x="ANO", y="151")
sns.barplot(data=df_qt, x="ANO", y="153")
sns.barplot(data=df_qt, x="ANO", y="154")
sns.barplot(data=df_qt, x="ANO", y="155")
sns.barplot(data=df_qt, x="ANO", y="169")

plt.title("Quantidade de Internação Hospitalar por Serviço e Ano")
plt.show()