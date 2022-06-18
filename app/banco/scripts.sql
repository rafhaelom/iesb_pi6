--- Criação do banco de dados ---
CREATE DATABASE saude_sus
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

--- Criação de schema ---
CREATE SCHEMA "sih-sus"
    AUTHORIZATION postgres;

--------------------------------------------------
-- Table: sih-sus.tb_sus_sih_qt

-- DROP TABLE IF EXISTS "sih-sus".tb_sus_sih_qt;

CREATE TABLE IF NOT EXISTS "sih-sus".tb_sus_sih_qt
(
    index bigint,
    "Ano" bigint,
    "Mes" bigint,
    "CodMunicipio" bigint,
    "V_105001_105" double precision,
    "V_105002_105" double precision,
    "V_105003_105" double precision,
    "V_105004_105" double precision,
    "V_105005_105" double precision,
    "V_105006_105" double precision,
    "V_105007_105" double precision,
    "V_105008_105" double precision,
    "V_105009_105" double precision,
    "V_107008_107" double precision,
    "V_113001_113" double precision,
    "V_113002_113" double precision,
    "V_113003_113" double precision,
    "V_113004_113" double precision,
    "V_115001_115" double precision,
    "V_115002_115" double precision,
    "V_115003_115" double precision,
    "V_115004_115" double precision,
    "V_116002_116" double precision,
    "V_116003_116" double precision,
    "V_116004_116" double precision,
    "V_116005_116" double precision,
    "V_117001_117" double precision,
    "V_117002_117" double precision,
    "V_120001_120" double precision,
    "V_120002_120" double precision,
    "V_121000_121" double precision,
    "V_121001_121" double precision,
    "V_121002_121" double precision,
    "V_121003_121" double precision,
    "V_121004_121" double precision,
    "V_121006_121" double precision,
    "V_121007_121" double precision,
    "V_121008_121" double precision,
    "V_121009_121" double precision,
    "V_121010_121" double precision,
    "V_122000_122" double precision,
    "V_122003_122" double precision,
    "V_122004_122" double precision,
    "V_122007_122" double precision,
    "V_122008_122" double precision,
    "V_125004_125" double precision,
    "V_125006_125" double precision,
    "V_125007_125" double precision,
    "V_126001_126" double precision,
    "V_126002_126" double precision,
    "V_126003_126" double precision,
    "V_126004_126" double precision,
    "V_126005_126" double precision,
    "V_126006_126" double precision,
    "V_126007_126" double precision,
    "V_126008_126" double precision,
    "V_127001_127" double precision,
    "V_128000_128" double precision,
    "V_128001_128" double precision,
    "V_128002_128" double precision,
    "V_128003_128" double precision,
    "V_128004_128" double precision,
    "V_131000_131" double precision,
    "V_131001_131" double precision,
    "V_131002_131" double precision,
    "V_131003_131" double precision,
    "V_131007_131" double precision,
    "V_132001_132" double precision,
    "V_132002_132" double precision,
    "V_132003_132" double precision,
    "V_132004_132" double precision,
    "V_132005_132" double precision,
    "V_135001_135" double precision,
    "V_135002_135" double precision,
    "V_135003_135" double precision,
    "V_135004_135" double precision,
    "V_135011_135" double precision,
    "V_140000_140" double precision,
    "V_140001_140" double precision,
    "V_140002_140" double precision,
    "V_140003_140" double precision,
    "V_140005_140" double precision,
    "V_140006_140" double precision,
    "V_140012_140" double precision,
    "V_140019_140" double precision,
    "V_142001_142" double precision,
    "V_142002_142" double precision,
    "V_142003_142" double precision,
    "V_142004_142" double precision,
    "V_145000_145" double precision,
    "V_145001_145" double precision,
    "V_145002_145" double precision,
    "V_145003_145" double precision,
    "V_145006_145" double precision,
    "V_145008_145" double precision,
    "V_145011_145" double precision,
    "V_149015_149" double precision,
    "V_151001_151" double precision,
    "V_151003_151" double precision,
    "V_154001_154" double precision,
    "V_154002_154" double precision,
    "V_155001_155" double precision,
    "V_155002_155" double precision,
    "V_155003_155" double precision,
    "V_169002_169 double precision)
" text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "sih-sus".tb_sus_sih_qt
    OWNER to postgres;
-- Index: ix_sih-sus_tb_sus_sih_qt_index

-- DROP INDEX IF EXISTS "sih-sus"."ix_sih-sus_tb_sus_sih_qt_index";

CREATE INDEX IF NOT EXISTS "ix_sih-sus_tb_sus_sih_qt_index"
    ON "sih-sus".tb_sus_sih_qt USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;