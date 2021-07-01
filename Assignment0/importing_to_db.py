#writes the random email's id's and passwords generated from csv to sqlite3 db
import sqlite3
import csv
conn=sqlite3.connect(":memory:")

c=conn.cursor()

c.execute("""CREATE TABLE users (email text, password text)""")

with open(r'C:\Users\Sowmith Kunapaneni\Documents\DS\GUVI-FDS\Sqlite_Python\random_users.csv','r',encoding="utf-16") as fin:
    reader=csv.DictReader(fin)
    to_db = [(i['email'], i['password']) for i in reader]

c.executemany("INSERT INTO users (email,password) VALUES (?,?);",to_db)
    
conn.commit()
c.execute("SELECT password FROM users WHERE password=?",("9Bo!$vWR",))
print(c.fetchone())
conn.close()