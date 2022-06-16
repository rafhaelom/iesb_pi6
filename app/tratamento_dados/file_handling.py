
class TratamentoArquivo:
    def __init__(self) -> None:
        self.path_raw = 'C:/Users/Usuario/Documents/Projetos_git/iesb_pi6/dados/raw_data/'
        self.path_base = 'C:/Users/Usuario/Documents/Projetos_git/iesb_pi6/dados/base_data/'

        # Dicionário com a chave (nome do mês) e valor (mês em número).
        self.meses = {'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4, 'Mai': 5, 'Jun': 6, \
            'Jul': 7, 'Ago': 8, 'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12}
