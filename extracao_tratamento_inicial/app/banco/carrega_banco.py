from msilib import schema
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

#from app.logs import logger

file_name = "C:/Users/Usuario/Documents/Projetos_git/iesb_pi6/app/dados/base_data/SIH_SUS_2018_1.csv"
df = pd.read_csv(file_name, sep=';', encoding='latin-1', header=0, usecols=None, nrows=None, lineterminator='\n', on_bad_lines='skip')
#print(df.columns)
# create sqlalchemy engine
#engine = create_engine('postgresql+psycopg2://{user}:{pw}@{servidor}/{db}'
                        #.format(user="postgres",
                             #   pw="",
                             #   servidor="localhost",
                             #   db="saude_sus"))

# Insert whole DataFrame into MySQL
#df.to_sql('tb_sus_sih_qt', schema="sih-sus", con = engine, if_exists = 'append', chunksize = 1000)




# Connect to your postgres DB
#conn = psycopg2.connect(host="localhost", port="5432", dbname="saude_sus", options="-c search_path=sih-sus", user="postgres", password="973314")

# Open a cursor to perform database operations
#cur = conn.cursor()

# creating column list for insertion
colunas = df.columns.to_list()
#cols = "`,`".join([str(i) for i in colunas])
colunas[-1] = 'V_169002_169'

cols = ",".join([str(i) for i in colunas])
print(df.V_169002_169)
# Insert DataFrame recrds one by one.
#for i,row in df.iterrows():
#    sql = "INSERT INTO `tb_teste_sus_sih_qt` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
#    cur.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
#    conn.commit()