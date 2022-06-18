from msilib import schema
from sqlalchemy import create_engine
import pandas as pd

#from app.logs import logger

file_name = "C:/Users/Usuario/Documents/Projetos_git/iesb_pi6/app/dados/base_data/SIH_SUS_2018_1.csv"
df = pd.read_csv(file_name, sep=';', encoding='latin-1', header=0, usecols=None, nrows=None, lineterminator='\n', on_bad_lines='skip')
print(df.columns)
# create sqlalchemy engine
engine = create_engine('postgresql+psycopg2://{user}:{pw}@{servidor}/{db}'
                        .format(user="postgres",
                                pw="",
                                servidor="localhost",
                                db="saude_sus"))

# Insert whole DataFrame into MySQL
#df.to_sql('tb_sus_sih_qt', schema="sih-sus", con = engine, if_exists = 'append', chunksize = 1000)