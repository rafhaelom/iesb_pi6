/*Definição de opções.*/
options mprint mlogic symbolgen;

/*Lib's utilizadas.*/
libname raw_sih "C:\Users\Usuario\Documents\Projetos_git\iesb_pi6\analise\dados_sih\rawdata";
libname base_sih "C:\Users\Usuario\Documents\Projetos_git\iesb_pi6\analise\dados_sih\basedata";

/*--- Armazenando dados na lib rawdata. ---*/
/*TB_SUS_SIH_QT*/
/*Retira ',' da coluna ANO.*/
data raw_sih.sus_sih (drop=ANO_CHAR);
	set work.tb_sus_sih_qt (rename=(ANO = ANO_CHAR));
	ANO = compress(ANO_CHAR, ',', '');
run;

/*TB_SUS_SIH_DICIONARIO*/
data raw_sih.sus_sih_dic;
	set work.tb_sus_sih_dicionario;
run;

/*TB_DTB_MUNICIPIOS_IBGE*/
data raw_sih.municipios_brasil_ibge;
	set work.tb_dtb_municipios_ibge;
run;
