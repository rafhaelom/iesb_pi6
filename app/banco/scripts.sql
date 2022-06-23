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