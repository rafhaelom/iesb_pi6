----------------------------------------------------------------------------
--- 		Criação da estrutura do database, schema e tabelas			 ---
----------------------------------------------------------------------------

--- Criação do banco de dados ---
CREATE DATABASE saude_sus
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

--- Criação de schema ---
CREATE SCHEMA "sih_sus"
    AUTHORIZATION postgres;


-- Criação tabela quantida de internações por município e serviço/classificação --- 
--- sih_sus.tb_sus_sih_qt ---

CREATE TABLE IF NOT EXISTS "sih_sus".tb_sus_sih_qt
(
    "ID_SIH_QT" serial not null primary key,
    "ANO" SMALLINT not null,
    "MES" SMALLINT not null,
    "COD_MUNICIPIO" INTEGER not null,
    "V_105001" INTEGER,
    "V_105002" INTEGER,
    "V_105003" INTEGER,
    "V_105004" INTEGER,
    "V_105005" INTEGER,
    "V_105006" INTEGER,
    "V_105007" INTEGER,
    "V_105008" INTEGER,
    "V_105009" INTEGER,
    "V_107008" INTEGER,
    "V_112001" INTEGER,
    "V_112003" INTEGER,
    "V_113001" INTEGER,
    "V_113002" INTEGER,
    "V_113003" INTEGER,
    "V_113004" INTEGER,
    "V_114006" INTEGER,
    "V_114007" INTEGER,
    "V_115001" INTEGER,
    "V_115002" INTEGER,
    "V_115003" INTEGER,
    "V_115004" INTEGER,
    "V_115005" INTEGER,
    "V_115007" INTEGER,
    "V_116002" INTEGER,
    "V_116003" INTEGER,
    "V_116004" INTEGER,
    "V_116005" INTEGER,
    "V_117001" INTEGER,
    "V_117002" INTEGER,
    "V_120001" INTEGER,
    "V_120002" INTEGER,
    "V_120003" INTEGER,
    "V_121000" INTEGER,
    "V_121001" INTEGER,
    "V_121002" INTEGER,
    "V_121003" INTEGER,
    "V_121004" INTEGER,
    "V_121006" INTEGER,
    "V_121007" INTEGER,
    "V_121008" INTEGER,
    "V_121009" INTEGER,
    "V_121010" INTEGER,
    "V_121011" INTEGER,
    "V_121012" INTEGER,
    "V_122000" INTEGER,
    "V_122001" INTEGER,
    "V_122003" INTEGER,
    "V_122004" INTEGER,
    "V_122005" INTEGER,
    "V_122007" INTEGER,
    "V_122008" INTEGER,
    "V_123002" INTEGER,
    "V_123006" INTEGER,
    "V_125001" INTEGER,
    "V_125002" INTEGER,
    "V_125004" INTEGER,
    "V_125006" INTEGER,
    "V_125007" INTEGER,
    "V_126001" INTEGER,
    "V_126002" INTEGER,
    "V_126003" INTEGER,
    "V_126004" INTEGER,
    "V_126005" INTEGER,
    "V_126006" INTEGER,
    "V_126007" INTEGER,
    "V_126008" INTEGER,
    "V_127001" INTEGER,
    "V_128000" INTEGER,
    "V_128001" INTEGER,
    "V_128002" INTEGER,
    "V_128003" INTEGER,
    "V_128004" INTEGER,
    "V_131000" INTEGER,
    "V_131001" INTEGER,
    "V_131002" INTEGER,
    "V_131003" INTEGER,
    "V_131005" INTEGER,
    "V_131006" INTEGER,
    "V_131007" INTEGER,
    "V_132001" INTEGER,
    "V_132002" INTEGER,
    "V_132003" INTEGER,
    "V_132004" INTEGER,
    "V_132005" INTEGER,
    "V_133001" INTEGER,
    "V_133002" INTEGER,
    "V_133003" INTEGER,
    "V_134003" INTEGER,
    "V_134011" INTEGER,
    "V_135001" INTEGER,
    "V_135002" INTEGER,
    "V_135003" INTEGER,
    "V_135004" INTEGER,
    "V_135005" INTEGER,
    "V_135007" INTEGER,
    "V_135008" INTEGER,
    "V_135010" INTEGER,
    "V_135011" INTEGER,
    "V_135013" INTEGER,
    "V_140000" INTEGER,
    "V_140001" INTEGER,
    "V_140002" INTEGER,
    "V_140003" INTEGER,
    "V_140004" INTEGER,
    "V_140005" INTEGER,
    "V_140006" INTEGER,
    "V_140012" INTEGER,
    "V_140019" INTEGER,
    "V_142001" INTEGER,
    "V_142002" INTEGER,
    "V_142003" INTEGER,
    "V_142004" INTEGER,
    "V_145000" INTEGER,
    "V_145001" INTEGER,
    "V_145002" INTEGER,
    "V_145003" INTEGER,
    "V_145005" INTEGER,
    "V_145006" INTEGER,
    "V_145008" INTEGER,
    "V_145009" INTEGER,
    "V_145011" INTEGER,
    "V_149001" INTEGER,
    "V_149005" INTEGER,
    "V_149006" INTEGER,
    "V_149008" INTEGER,
    "V_149014" INTEGER,
    "V_149015" INTEGER,
    "V_149016" INTEGER,
    "V_151001" INTEGER,
    "V_151003" INTEGER,
    "V_153002" INTEGER,
    "V_154001" INTEGER,
    "V_154002" INTEGER,
    "V_155001" INTEGER,
    "V_155002" INTEGER,
    "V_155003" INTEGER,
    "V_169002" INTEGER
)

--- Homologação da estrutura da tabela criada ---
select * from sih_sus.tb_sus_sih_qt;

-- Criação tabela quantida de internações por município e serviço/classificação --- 
--- sih_sus.tb_sus_sih_dicionario ---

CREATE TABLE IF NOT EXISTS "sih_sus".tb_sus_sih_dicionario
(
    "ID_SIH_DIC" serial not null primary key,
    "COD_SERVICO_CLASSIFICACAO" VARCHAR(10) not null, 
	"DESC_SERVICO_CLASSIFICACAO" VARCHAR(120) not null,
	"COD_SERVICO" VARCHAR(10) not null, 
	"DESC_SERVICO" VARCHAR(100) not null, 
	"COD_CLASSIFICACAO" VARCHAR(10) not null,
	"DESC_CLASSIFICACAO" VARCHAR(100) not null, 
	"QUANTIDADE_APROVADA" INTEGER not null
)

--- Homologação da estrutura da tabela criada ---
select * from sih_sus.tb_sus_sih_dicionario;

-- Criação tabela quantida de internações por município e serviço/classificação --- 
--- sih_sus.tb_dtb_municipios_ibge ---

CREATE TABLE IF NOT EXISTS sih_sus.tb_dtb_municipios_ibge
(
	"COD_UF" smallint not null, 
	"DESC_UF" VARCHAR(30) not null, 
	"COD_REGIAO_GEOGRAFICA_INTERMEDIARIA" smallint not null,
	"DESC_REGIAO_GEOGRAFICA_INTERMEDIARIA" VARCHAR(50) not null,
	"COD_REGIAO_GEOGRAFICA_IMEDIATA" INTEGER not null, 
	"DESC_REGIAO_GEOGRAFICA_IMEDIATA" VARCHAR(80) not null,
	"COD_MESORREGIAO" VARCHAR(10) not null, 
	"DESC_MESORREGIAO" VARCHAR(50) not null, 
	"COD_MICRORREGIAO" VARCHAR(10) not null,
	"DESC_MICRORREGIAO" VARCHAR(50) not null, 
	"COD_ABREVIADO_MUNICIPIO" VARCHAR(10) not null,
	"COD_COMPLETO_MUNICIPIO" INTEGER not null, 
	"DESC_MUNICIPIO" VARCHAR(50) not null
)

--- Homologação da estrutura da tabela criada ---
select * from sih_sus.tb_dtb_municipios_ibge;

----------------------------------------------------------------------------
--- 			Análise Quantidade de Internações/Registros				 ---
----------------------------------------------------------------------------

--- Quantidade de registros totais. ---
select count(*) from sih_sus.tb_sus_sih_qt;

--- Quantidade de registros por ano. ---
select 
	a."ANO", 
	count(*) 
from sih_sus.tb_sus_sih_qt a
	group by a."ANO"
		order by a."ANO";

--- Quantidade de registros por ano e mes. ----
select 
	a."ANO", 
	a."MES", 
	count(*) 
from sih_sus.tb_sus_sih_qt a
	group by a."ANO", a."MES"
		order by a."ANO", a."MES";




colunas_qt = ["ID_SIH_QT", "ANO", "MES", "COD_MUNICIPIO", "V_105001", "V_105002", "V_105003", "V_105004", \
                "V_105005", "V_105006", "V_105007", "V_105008", "V_105009", "V_107008", "V_112001", "V_112003", \
                "V_113001", "V_113002", "V_113003", "V_113004", "V_114006", "V_114007", "V_115001", "V_115002", \
                "V_115003", "V_115004", "V_115005", "V_115007", "V_116002", "V_116003", "V_116004", "V_116005", \
                "V_117001", "V_117002", "V_120001", "V_120002", "V_120003", "V_121000", "V_121001", "V_121002", \
                "V_121003", "V_121004", "V_121006", "V_121007", "V_121008", "V_121009", "V_121010", "V_121011", \
                "V_121012", "V_122000", "V_122001", "V_122003", "V_122004", "V_122005", "V_122007", "V_122008", \
                "V_123002", "V_123006", "V_125001", "V_125002", "V_125004", "V_125006", "V_125007", "V_126001", \
                "V_126002", "V_126003", "V_126004", "V_126005", "V_126006", "V_126007", "V_126008", "V_127001", \
                "V_128000", "V_128001", "V_128002", "V_128003", "V_128004", "V_131000", "V_131001", "V_131002", \
                "V_131003", "V_131005", "V_131006", "V_131007", "V_132001", "V_132002", "V_132003", "V_132004", \
                "V_132005", "V_133001", "V_133002", "V_133003", "V_134003", "V_134011", "V_135001", "V_135002", \
                "V_135003", "V_135004", "V_135005", "V_135007", "V_135008", "V_135010", "V_135011", "V_135013", \
                "V_140000", "V_140001", "V_140002", "V_140003", "V_140004", "V_140005", "V_140006", "V_140012", \
                "V_140019", "V_142001", "V_142002", "V_142003", "V_142004", "V_145000", "V_145001", "V_145002", \
                "V_145003", "V_145005", "V_145006", "V_145008", "V_145009", "V_145011", "V_149001", "V_149005", \
                "V_149006", "V_149008", "V_149014", "V_149015", "V_149016", "V_151001", "V_151003", "V_153002", \
                "V_154001", "V_154002", "V_155001", "V_155002", "V_155003" , "V_16900"]  


colunas_dic = ["ID_SIH_DIC", "COD_SERVICO_CLASSIFICACAO", "DESC_SERVICO_CLASSIFICACAO", "COD_SERVICO", \
                "DESC_SERVICO", "COD_CLASSIFICACAO", "DESC_CLASSIFICACAO", "QUANTIDADE_APROVADA"]


colunas_municipios = ["COD_UF", "DESC_UF", "COD_REGIAO_GEOGRAFICA_INTERMEDIARIA", "DESC_REGIAO_GEOGRAFICA_INTERMEDIARIA", \
                        "COD_REGIAO_GEOGRAFICA_IMEDIATA", "DESC_REGIAO_GEOGRAFICA_IMEDIATA", "COD_MESORREGIAO", \
                        "DESC_MESORREGIAO", "COD_MICRORREGIAO", "DESC_MICRORREGIAO", "COD_ABREVIADO_MUNICIPIO", \
                        "COD_COMPLETO_MUNICIPIO", "DESC_MUNICIPIO"]


servico_105 = ["V_105001", "V_105002", "V_105003", "V_105004", "V_105005", "V_105006", "V_105007", "V_105008", "V_105009"]

servico_107 = ["V_107008"]

servico_112 = [ "V_112001", "V_112003"]

servico_113 = ["V_113001", "V_113002", "V_113003", "V_113004"]

servico_114 = ["V_114006", "V_114007"]

servico_115 = ["V_115001", "V_115002", "V_115003", "V_115004", "V_115005", "V_115007"]

servico_116 = ["V_116002", "V_116003", "V_116004", "V_116005"]

servico_117 = ["V_117001", "V_117002"]

servico_120 = ["V_120001", "V_120002", "V_120003"]

servico_121 = ["V_121000", "V_121001", "V_121002", "V_121003", "V_121004", "V_121006", "V_121007", \
                        "V_121008", "V_121009", "V_121010", "V_121011", "V_121012"]

servico_122 = ["V_122000", "V_122001", "V_122003", "V_122004", "V_122005", "V_122007", "V_122008"]

servico_123 = ["V_123002", "V_123006"]

servico_125 = ["V_125001", "V_125002", "V_125004", "V_125006", "V_125007"]

servico_126 = ["V_126001", "V_126002", "V_126003", "V_126004", "V_126005", "V_126006", "V_126007", "V_126008"]

servico_127 = ["V_127001"]

servico_128 = ["V_128000", "V_128001", "V_128002", "V_128003", "V_128004"]

servico_131 = ["V_131000", "V_131001", "V_131002", "V_131003", "V_131005", "V_131006", "V_131007"]

servico_132 = ["V_132001", "V_132002", "V_132003", "V_132004", "V_132005"]

servico_133 = ["V_133001", "V_133002", "V_133003"]

servico_134 = ["V_134003", "V_134011"]

servico_135 = ["V_135001", "V_135002", "V_135003", "V_135004", "V_135005", "V_135007", "V_135008", "V_135010", "V_135011", "V_135013"]

servico_140 = ["V_140000", "V_140001", "V_140002", "V_140003", "V_140004", "V_140005", "V_140006", "V_140012", "V_140019"]

servico_142 = ["V_142001", "V_142002", "V_142003", "V_142004"]

servico_145 = ["V_145000", "V_145001", "V_145002", "V_145003", "V_145005", "V_145006", "V_145008", "V_145009", "V_145011"]

servico_149 = ["V_149001", "V_149005", "V_149006", "V_149008", "V_149014", "V_149015", "V_149016"]

servico_151 = ["V_151001", "V_151003"]

servico_153 = ["V_153002"]

servico_154 = ["V_154001", "V_154002"]

servico_155 = ["V_155001", "V_155002", "V_155003"]

servico_169 = ["V_16900"]

----------------------------------------------------
--- criando coluna servico | total ----

servico = '105';
total = '105'n;
output;

servico = '107';
total = '107'n;
output;

servico = '112';
total = '112'n;
output;

servico = '113';
total = '113'n;
output;

servico = '114';
total = '114'n;
output;

servico = '115';
total = '115'n;
output;

servico = '116';
total = '116'n;
output;

servico = '117';
total = '117'n;
output;

servico = '120';
total = '120'n;
output;

servico = '121';
total = '121'n;
output;

servico = '122';
total = '122'n;
output;

servico = '123';
total = '123'n;
output;

servico = '125';
total = '125'n;
output;

servico = '126';
total = '126'n;
output;

servico = '127';
total = '127'n;
output;

servico = '128';
total = '128'n;
output;

servico = '131';
total = '131'n;
output;

servico = '132';
total = '132'n;
output;

servico = '133';
total = '133'n;
output;

servico = '134';
total = '134'n;
output;

servico = '135';
total = '135'n;
output;

servico = '140';
total = '140'n;
output;

servico = '142';
total = '142'n;
output;

servico = '145';
total = '145'n;
output;

servico = '149';
total = '149'n;
output;

servico = '151';
total = '151'n;
output;

servico = '153';
total = '153'n;
output;

servico = '154';
total = '154'n;
output;

servico = '155';
total = '155'n;
output;

servico = '169';
total = '169'n;
output;


where in ('530010','520010','520017','520025','520030','520400','520549','520551','520580','520620','520800','521250','521305','521523','521560','521730','521760','521975','522185','522220','522230');

# # Quantidade por Servicos Hospitalares.
df['105'] = df[["V_105001", "V_105002", "V_105003", "V_105004", "V_105005", "V_105006", "V_105007", "V_105008", "V_105009"]].sum(axis=1)
df['107'] = df[["V_107008"]].sum(axis=1)
df['112'] = df[ "V_112001", "V_112003"]].sum(axis=1)
df['113'] = df[["V_113001", "V_113002", "V_113003", "V_113004"]].sum(axis=1)
df['114'] = df[["V_114006", "V_114007"]].sum(axis=1)
df['115'] = df[["V_115001", "V_115002", "V_115003", "V_115004", "V_115005", "V_115007"]].sum(axis=1)
df['116'] = df[["V_116002", "V_116003", "V_116004", "V_116005"]].sum(axis=1)
df['117'] = df[["V_117001", "V_117002"]].sum(axis=1)
df['120'] = df[["V_120001", "V_120002", "V_120003"]].sum(axis=1)
df['121'] = df[["V_121000", "V_121001", "V_121002", "V_121003", "V_121004", "V_121006", "V_121007", \
                            "V_121008", "V_121009", "V_121010", "V_121011", "V_121012"]].sum(axis=1)
df['122'] = df[["V_122000", "V_122001", "V_122003", "V_122004", "V_122005", "V_122007", "V_122008"]].sum(axis=1)
df['123'] = df[["V_123002", "V_123006"]].sum(axis=1)
df['125'] = df[["V_125001", "V_125002", "V_125004", "V_125006", "V_125007"]].sum(axis=1)
df['126'] = df[["V_126001", "V_126002", "V_126003", "V_126004", "V_126005", "V_126006", "V_126007", "V_126008"]].sum(axis=1)
df['127'] = df[["V_127001"]].sum(axis=1)
df['128'] = df[["V_128000", "V_128001", "V_128002", "V_128003", "V_128004"]].sum(axis=1)
df['131'] = df[["V_131000", "V_131001", "V_131002", "V_131003", "V_131005", "V_131006", "V_131007"]].sum(axis=1)
df['132'] = df[["V_132001", "V_132002", "V_132003", "V_132004", "V_132005"]].sum(axis=1)
df['133'] = df[["V_133001", "V_133002", "V_133003"]].sum(axis=1)
df['134'] = df[["V_134003", "V_134011"]].sum(axis=1)
df['135'] = df[["V_135001", "V_135002", "V_135003", "V_135004", "V_135005", "V_135007", "V_135008", "V_135010", "V_135011", "V_135013"]].sum(axis=1)
df['140'] = df[["V_140000", "V_140001", "V_140002", "V_140003", "V_140004", "V_140005", "V_140006", "V_140012", "V_140019"]].sum(axis=1)
df['142'] = df[["V_142001", "V_142002", "V_142003", "V_142004"]].sum(axis=1)
df['145'] = df[["V_145000", "V_145001", "V_145002", "V_145003", "V_145005", "V_145006", "V_145008", "V_145009", "V_145011"]].sum(axis=1)
df['149'] = df[["V_149001", "V_149005", "V_149006", "V_149008", "V_149014", "V_149015", "V_149016"]].sum(axis=1)
df['151'] = df[["V_151001", "V_151003"]].sum(axis=1)
df['153'] = df[["V_153002"]].sum(axis=1)
df['154'] = df[["V_154001", "V_154002"]].sum(axis=1)
df['155'] = df[["V_155001", "V_155002", "V_155003"]].sum(axis=1)
df['169'] = df[["V_169002"]].sum(axis=1)

def modificaDtypeColunas(df):
# Modifica dtype de colunas.
df['105'] = df['105'].astype('Int64')
df['107'] = df['107'].astype('Int64')
df['112'] = df['112'].astype('Int64')
df['113'] = df['113'].astype('Int64')
df['114'] = df['114'].astype('Int64')
df['115'] = df['115'].astype('Int64')
df['116'] = df['116'].astype('Int64')
df['117'] = df['117'].astype('Int64')
df['120'] = df['120'].astype('Int64')
df['121'] = df['121'].astype('Int64')
df['122'] = df['122'].astype('Int64')
df['123'] = df['123'].astype('Int64')
df['125'] = df['125'].astype('Int64')
df['126'] = df['126'].astype('Int64')
df['127'] = df['127'].astype('Int64')
df['128'] = df['128'].astype('Int64')
df['131'] = df['131'].astype('Int64')
df['132'] = df['132'].astype('Int64')
df['133'] = df['133'].astype('Int64')
df['134'] = df['134'].astype('Int64')
df['135'] = df['135'].astype('Int64')
df['140'] = df['140'].astype('Int64')
df['142'] = df['142'].astype('Int64')
df['145'] = df['145'].astype('Int64')
df['149'] = df['149'].astype('Int64')
df['151'] = df['151'].astype('Int64')
df['153'] = df['153'].astype('Int64')
df['154'] = df['154'].astype('Int64')
df['155'] = df['155'].astype('Int64')
df['169'] = df['169'].astype('Int64')