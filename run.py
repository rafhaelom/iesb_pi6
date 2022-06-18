import os
import sys
from sqlalchemy import create_engine

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
        Nome coluna Nova = 'V_105001_105'
    """
    logger.info('Criando padronização no nome das colunas.')
    colunas_origem = list(df.columns)
    nomes_coluna = []
    for col in colunas_origem:
        if len(col) > 15:
            #print(f"V_{col[:6]}_{col[7:10]}")
            nomes_coluna.append(f"V_{col[:6]}_{col[7:10]}")
        else:
            nomes_coluna.append(col)

    df1 = df.copy()
    df1.columns = nomes_coluna
    return df1

if __name__ == '__main__':
    arquivos = listarDiretorio(path_raw)
    logger.debug('Loop pipeline para os arquivos iniciado!!!')
    #for arquivo in arquivos:
    logger.debug('Extração de dados do arquivo iniciado!!!')
    extracao = ExtracaoDados(arquivos[0])
    df1, ano, mes = extracao.main()
    df2 = criaNomeColuna(df1)
    logger.debug(f'Tratamento do arquivo {arquivos[0]} iniciado!!!')
    tratamento = TratamentoArquivo(df2, ano, mes)
    df3 = tratamento.main()
    print(arquivos[0])
    logger.debug(f'Todos os arquivos foram extraidos!!!')

    # create sqlalchemy engine
    engine = create_engine('postgresql+psycopg2://{user}:{pw}@{servidor}/{db}'
                            .format(user="postgres",
                                    pw="",
                                    servidor="localhost",
                                    db="saude_sus"))

    # Insert whole DataFrame into MySQL
    df3.to_sql('tb_teste_sus_sih_qt', schema="sih-sus", con = engine, if_exists = 'append', chunksize = 1000)
    engine.commit()