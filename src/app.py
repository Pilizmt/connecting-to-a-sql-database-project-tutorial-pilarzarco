import pandas as pd
from dotenv import load_dotenv
import sqlite3 as sq

# 1) Connect to the database here using the SQLAlchemy's create_engine function
# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
# 4) Use pandas to print one of the tables as dataframes using read_sql function

# load the .env file variables
load_dotenv()

# Open the connection to the database
con = sq.connect("prueba.db")
cursor = con.cursor()

# print one of the tables as dataframes using read_sql function
consult = "SELECT * FROM books"
consult_book = pd.read_sql_query(consult, con)
print(consult_book)

# Close the database connection
con.close()


# from dotenv import load_dotenv

# # Carga las variables de entorno desde el archivo .env
# load_dotenv()
# import os

# Accede a las variables de entorno cargadas desde el archivo .env
# db_host = os.getenv("DB_HOST")
# db_user = os.getenv("DB_USER")
# db_password = os.getenv("DB_PASSWORD")
# db_name = os.getenv("DB_NAME")
# db_port = os.getenv("DB_PORT")

# (127.0.0.1).