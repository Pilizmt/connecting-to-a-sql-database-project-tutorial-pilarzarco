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


# con.execute("""
#     CREATE TABLE publishers (
#         publisher_id INT NOT NULL,
#         name VARCHAR(255) NOT NULL,
#         PRIMARY KEY (publisher_id);""")


# except sq.OperationalError:
#     pass

# con.execute("""
#         CREATE TABLE authors(
#         author_id INT NOT NULL,
#         first_name VARCHAR(100) NOT NULL,
#         middle_name VARCHAR(50) NULL,
#         last_name VARCHAR(100) NULL,
#         PRIMARY KEY(author_id)
#     )            
# """)

# con.execute("""CREATE TABLE books(
#     book_id INT NOT NULL,
#     title VARCHAR(255) NOT NULL,
#     total_pages INT NULL,
#     rating DECIMAL(4, 2) NULL,
#     isbn VARCHAR(13) NULL,
#     published_date DATE,
#     publisher_id INT NULL,
#     PRIMARY KEY(book_id),
#     CONSTRAINT fk_publisher FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id))""")

# con.execute("""CREATE TABLE book_authors (
#     book_id INT NOT NULL,
#     author_id INT NOT NULL,
#     PRIMARY KEY (book_id, author_id),
#     CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES books(book_id) ON DELETE CASCADE,
#     CONSTRAINT fk_author FOREIGN KEY(author_id) REFERENCES authors(author_id)) ON DELETE CASCADE""")

# con.execute("""CREATE TABLE book_authors (
#     book_id INT NOT NULL,
#     author_id INT NOT NULL,
#     PRIMARY KEY (book_id, author_id),
#     FOREIGN KEY (book_id) REFERENCES books (book_id),
#     FOREIGN KEY (author_id) REFERENCES authors (author_id)
#     )
# """)

# con.commit()

# # We add the file insert.sql with the data to be integrated in the tables
# with open("./src/sql/insert.sql", "r") as sql_file:
#     sql_script = sql_file.read()
# cursor.executescript(sql_script)

# print one of the tables as dataframes using read_sql function
consult = "SELECT * FROM books"
consult_book = pd.read_sql_query(consult, con)
print(consult_book)

# Close the database connection
con.close()



