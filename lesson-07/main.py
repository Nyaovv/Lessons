# Базы данных - SQLite3

import sqlite3

# 1. Подключение к БД
conn = sqlite3.connect('db.sqlite')

# 2. Создание объекта курсора
cursor = conn.cursor()

# 3. Выполнить SQL-запрос к БД
sql = '''
    CREATE TABLE IF NOT EXISTS shortener (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        origin_url TEXT NOT NULL,
        short_url TEXT NOT NULL DEFAULT '',
        created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
'''

# Закрываем соединение с БД
conn.close()
