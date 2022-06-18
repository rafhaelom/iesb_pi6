import os
import sys

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
    print(colunas_origem)
    #print(len(colunas_origem))
    for col in colunas_origem:
        if len(col) > 15:
            #print(f"V_{col[:6]}_{col[7:10]}")
            nomes_coluna.append(f"V_{col[:6]}_{col[7:10]}")
        else:
            nomes_coluna.append(col)
            #print("A coluna {0}\n não é a coluna de serviço\n".format(col))

    #colunas_novas = ["Ano", "Mes", "CodMunicipio"] + nomes_coluna
    #print(type(colunas_novas))
    df1 = df.copy()
    df1.columns = nomes_coluna
    return df1

if __name__ == '__main__':
    #for i in range(0,50):
    arquivo = listarDiretorio(path_raw)[0]
    logger.debug('Loop pipeline para os arquivos iniciado!!!')
    #for arquivo in arquivos:
    logger.debug('Extração de dados do arquivo iniciado!!!')
    extracao = ExtracaoDados(arquivo)
    df1, ano, mes = extracao.main()
    #print(df1.columns)
    df2 = criaNomeColuna(df1)
    print(df2)
    #print(ano)
    #print(mes)
    print()
    logger.debug(f'Tratamento do arquivo {arquivo} iniciado!!!')
    tratamento = TratamentoArquivo(df2, ano, mes)
    df3 = tratamento.main()
    print(df3)
    logger.debug(f'Todos os arquivos foram extraidos!!!')