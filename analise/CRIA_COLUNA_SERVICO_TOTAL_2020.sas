/*Sort = Ordenando valores.*/
proc sort data=work.SIH_SUS_SERVICOS_2020; /*out=work.saude_reformatado_2020;*/
   by ano_mes ano mes cod_municipio_sem_dv;
run;

/*Criando coluna 'SERVICO' e coluna 'TOTAL'.*/
data SIH_BASE.saude_reformatado_2020 (keep= ano_mes ano mes cod_municipio_sem_dv servico total);
	set work.SIH_SUS_SERVICOS_2020;

	by ano_mes ano mes cod_municipio_sem_dv;
	retain ano_mes ano mes cod_municipio_sem_dv;

	attrib servico length=$3.;
	attrib total length=8.;

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

run;