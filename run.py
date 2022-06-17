from app.logs import logger
from app.extracao_dados import extracao
from app.tratamento_dados import tratamento

if __name__ == '__main__':
    logger.debug('Extração de dados do arquivo iniciado.')
    extracao.main()
    