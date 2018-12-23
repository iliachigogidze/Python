import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('CREATE TABLE users (id int, username text, password text)')

user = (1, 'ilia', 'qwerty')

cursor.execute('INSERT INTO users VALUES(?,?,?)', user)

users = [
    (2, 'nika', 'sdf'),
    (3, 'temo', 'davassdf')
]

cursor.executemany('INSERT INTO users VALUES(?,?,?)', users)

selected = cursor.execute('SELECT * FROM users')
for row in selected:
    print(row)

connection.commit()

connection.close()