import json
import psycopg2


conn = psycopg2.connect('dbname=test user=postgres password=123')

cur = conn.cursor()



cur.execute('''
CREATE TABLE wishlist
(id serial PRIMARY KEY,
author varchar,
title varchar,
tags ARRAY,
cover varchar,
rating real,
desc text );''')



with open('list_of_books.txt', 'r') as f:
    data = json.load(f)
    data0 = data[0]

# print(data0[0])

cur.execute('''
DELETE FROM wishlist
WHERE id = 0;
''')

conn.commit()

# cur.execute('''
# INSERT INTO wishlist VALUES(0, 'Имя', 'Наименования', '[Жанры, и еще жанры]', 'Обложка', '5.5', 'Описание')''')



cur.execute('''
INSERT INTO wishlist VALUES(0, data0[0], data0[1], data0[2], data0[3], data0[4], data0[5])''')

conn.commit()

cur.close()
conn.close()