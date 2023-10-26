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

