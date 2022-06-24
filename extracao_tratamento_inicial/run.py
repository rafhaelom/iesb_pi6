import os
import sys

import psycopg2

from app.logs import logger
from app.extracao_dados.extracao import ExtracaoDados
from app.tratamento_dados.tratamento import TratamentoArquivo

path_raw = 'C:/Users/Usuario/Documents/Projetos_git/iesb_pi6/app/dados/raw_data/'

def listarDiretorio(path_raw) -> list:
    """Função para listar os arquivos de um diretório."""
    try:
        logger.info(f'Listando os arquivos do diretório "{path_raw}"')
        return os.listdir(path_raw)
    except OSError as ose:
        logger.error(f'Diretório Inválido ou Inexistente!!! {ose}')
        logger.error(f'{path_raw} type: {type(path_raw)}')
        print(f"Diretório Inválido ou Inexistente!!! {ose}")
        sys.exit()

def criaNomeColuna(df):
    """Função para criar padrão no nome das colunas de serviço/classificação.
    
    Ex: Nome coluna Original = '105001 105 SERVICO DE ATENCAO EM NEUROLOGIA / NEUROCIRURGIA / 001 NEUROCIRURGIA DO TRAUMA E ANOMALIAS DO DE'
        Nome coluna Nova = 'V_105001'
    """
    logger.info('Criando padronização no nome das colunas.')
    colunas_origem = list(df.columns)
    nomes_coluna = []
    for col in colunas_origem:
        if len(col) > 15:
            #print(f"V_{col[:6]}_{col[7:10]}")
            nomes_coluna.append(f"V_{col[:6]}")
        else:
            nomes_coluna.append(col)

    df1 = df.copy()
    df1.columns = nomes_coluna
    return df1

if __name__ == '__main__':
    arquivos = listarDiretorio(path_raw)
    #arquivo = arquivos[-1]
    logger.debug('Loop pipeline para os arquivos iniciado!!!')
    for arquivo in arquivos:
        logger.debug('Extração de dados do arquivo iniciado!!!')
        extracao = ExtracaoDados(arquivo)
        df1, ano, mes = extracao.main()
        df2 = criaNomeColuna(df1)
        logger.debug(f'Tratamento do arquivo {arquivo} iniciado!!!')
        tratamento = TratamentoArquivo(df2, ano, mes)
        df3 = tratamento.main()
        print(arquivo)
    logger.debug(f'Todos os arquivos foram extraidos!!!')
    #print(arquivos)
    #print()
    #print(arquivo)
    #print(ano, mes)
    #print()
    """
    # Connect to your postgres DB
    conn = psycopg2.connect(host="localhost", port="5432", dbname="saude_sus", user="postgres", password="")
    #conn = psycopg2.connect(host="", port="5432", dbname="sus_saude", user="", password="")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # creating column list for insertion
    colunas = df3.columns.to_list()
    cols = ",".join([str(i) for i in colunas])
    print(cols)

    # Insert DataFrame recrds one by one.
    for i,row in df3.iterrows():
        print(row)
        sql = str('INSERT INTO sih_sus.tb_sus_sih_qt (' + 'id_sih_qtd,' +cols + ') VALUES (' + 'default,' +'%s,'*(len(row)-1) + '%s)')
        #sql = f'INSERT INTO `"sih-sus".tb_teste_sus_sih_qt` (`" +{cols} + "`) VALUES ({i}, {*(len(row)-1) i})'
        cur.execute(sql, tuple(row))
        print(sql)
        exit()


    # the connection is not autocommitted by default, so we must commit to save our changes
    conn.commit()
    # Fecha conexão com o banco.
    conn.close()
    #print(sql)
    """