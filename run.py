from app.logs import logger
from app.extracao_dados.extracao import ExtracaoDados
from app.tratamento_dados.tratamento import TratamentoArquivo

if __name__ == '__main__':
    logger.debug('Extração de dados do arquivo iniciado.')
    extracao = ExtracaoDados()
    df, ano, mes = extracao.main()
    #print(df)
    #print()
    #print(ano)
    #print(mes)
    #logger.debug('Tratamento do arquivo iniciado.')
    tratamento = TratamentoArquivo(df, ano, mes)
    tratamento.main()