import logging

'''Formatação para definir como o log será mostrado.'''
# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

'''
Configurações do modulo.

filename = 'Nome do arquivo em que salva a mensagem do log.'
filemode = 'Forma em que o arquivo será gravado.'
level = 'Level(nivel) em que o log atuará.'
format = 'Formatação da mensagem do log.'
'''
logging.basicConfig(filename='app/logs/testes1.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format,
                    encoding='utf-8')

# Instancia do objeto getLogger()
logger = logging.getLogger('root')