import json
import psycopg2


conn = psycopg2.connect('dbname=tt user=postgres password=123')
cur = conn.cursor()

def livelib():
    cur.execute('''
    CREATE TABLE wishlist
    (id serial PRIMARY KEY,
    url text,
    author varchar,
    title varchar,
    tags text, 
    cover text,
    rating real,
    description text,
    key smallint );''')

    conn.commit()

    with open('list_of_books.txt', 'r') as f:
        data = json.load(f)
        for index, row in enumerate(data):
            cur.execute('''
            INSERT INTO wishlist VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (index, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    conn.commit()

def library():
    cur.execute('''
    CREATE TABLE nekrasovka
    (id serial PRIMARY KEY,
    author varchar,
    title varchar,
    notes text,
    key smallint);''')

    with open('actual_in_lib.txt', 'r') as f:
        data = json.load(f)
        for index, row in enumerate(data):
            cur.execute('''
            INSERT INTO nekrasovka VALUES(%s, %s, %s, %s, %s)
            ''', (index, row[0], row[1], row[2], row[3]))

    conn.commit()


livelib()
library()

cur.close()
conn.close()