/*Monta base final*/
data saude_base_final;
	set work.saude_base_final;
	attrib ano_mes length=
run;

/*Junta bases.*/
proc append base=saude_base_final data=SIH_BASE.saude_reformatado_2018;
	sysecho "apenda saude_reformatado_2018.";
run;

proc append base=saude_base_final data=SIH_BASE.saude_reformatado_2019;
	sysecho "apenda saude_reformatado_2019.";
run;

proc append base=saude_base_final data=SIH_BASE.saude_reformatado_2020;
	sysecho "apenda saude_reformatado_2020.";
run;

proc append base=saude_base_final data=SIH_BASE.saude_reformatado_2021;
	sysecho "apenda saude_reformatado_2021.";
run;

proc append base=saude_base_final data=SIH_BASE.saude_reformatado_2022;
	sysecho "apenda saude_reformatado_2022.";
run;

/*Sort = Ordenando valores.*/
proc sort data=work.saude_base_final out=SIH_BASE.saude_base_final;
   by ano_mes ano mes cod_municipio_sem_dv servico total;
run;