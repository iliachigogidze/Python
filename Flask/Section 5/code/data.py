import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

# cursor.execute('CREATE TABLE users (id int, username text, password text)')

cursor.execute('INSERT INTO users VALUES(?,?,?)',(1,'ilia','qwerty'))

users = [(2,'nika','asdf'),(3,'nino','sdfg')]

cursor.executemany('INSERT INTO users VALUES(?,?,?)', users)

for row in cursor.execute('SELECT * FROM users'):
    print(row)

connection.commit()

connection.close()