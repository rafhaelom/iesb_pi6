import pandas as pd

df_dic = pd.read_csv("app/dados/dicionario/A115354189_28_143_208.csv", sep=';', encoding='latin-1', header=3, lineterminator='\n', on_bad_lines='skip')

df_dic = df_dic[:-6]

df_dic.insert(0, "SERVICO", df_dic["Serviço/Classificação"].apply(lambda x: x[:3]), allow_duplicates=False)
df_dic.insert(1, "CLASSIFICACAO", df_dic["Serviço/Classificação"].apply(lambda x: f'V_{x[:7]}'), allow_duplicates=False)

#print(df_dic)

descricao = list(df_dic["Serviço/Classificação"])
print(descricao.split('/'))