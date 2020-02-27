import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


# int is the same as INTEGER in most of the cases
# but when you want to create auto increment primary key
# you should use INTEGER, not int
create_query = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(create_query)

# float type in sqlite is - real
create_query = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)'
cursor.execute(create_query)

cursor.execute("INSERT INTO items VALUES (3,'test_item', 0.99)")

connection.commit()

connection.close()
