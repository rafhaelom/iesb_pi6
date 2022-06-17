import os
import sys
from app.logs import logger

class TratamentoArquivo:
    def __init__(self) -> None:
        logger.debug('Classe "TratamentoArquivo" iniciada.')

    def main(self, df, ano_arq, mes_arq):
        print(df)
        print(ano_arq)
        print(mes_arq)

