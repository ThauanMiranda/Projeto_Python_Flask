import sqlite3 as sql

con = sql.connect ('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE "users" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NOME" TEXT,
    "MARCA" TEXT,
    "NUMERO" TEXT
    )'''

#cur.execute("INSERT INTO users VALUES('1','jordar','nike','41')")

cur.execute(sql)
con.commit()    
con.close()

#cur.execute("SELECT * FROM users")
#print(cur.fetchall())

