# creates the db and tables
import sqlite3
DATABASE = 'app.db'

def create_user_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alias TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()


def create_uploads_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            receiver TEXT,
            cost REAL,
            account_details TEXT,
            file_name TEXT,
            file_part1 TEXT,
            file_part2 TEXT,
            payment_status TEXT,
            token TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_user_table()
create_uploads_table()