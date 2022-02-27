import pandas as pd
import os
import sqlalchemy  

# Como aqui é um ambiente público o IP, Senha e Porta  foram omitidos:
str_connection = 'postgresql+psycopg2://database:senha@"localhost",:porta/Olist'

connection = sqlalchemy.create_engine(str_connection)

path = r'data'
files_names = []
for file in os.listdir(path):
    if file.endswith(".csv"):
        #print(os.path.join(path, file))
        files_names.append((os.path.join(path, file)))
print(files_names)

for i in files_names:
    df_tmp = pd.read_csv(i)
    table_name = "tb_"+i.strip(".csv").replace("olist_","").replace("_dataset","")
    df_tmp.to_sql(table_name,con = connection,if_exists='replace')