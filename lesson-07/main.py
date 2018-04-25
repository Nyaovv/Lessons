# Базы данных - SQLite3

import sqlite3

# 1. Подключение к БД
conn = sqlite3.connect('db.sqlite')

# 2. Создание объекта курсора
cursor = conn.cursor()

# 3. Выполнить SQL-запрос к БД
sql = '''
    CREATE TABLE IF NOT EXISTS shortener (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_url TEXT NOT NULL DEFAULT '',
        created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
'''
cursor.execute(sql)

# 3.2. Если запрос на изменение данных или структуры БД,
#то фиксируем с помощью commit
conn.commit()

sql = '''
	INSERT INTO shortener (	original_url) VALUES (?)
'''
# Колонки перечисляют через запятую

cursor.execute(sql, ('http://profi.itmo.ru',))
#Если хочу указать кортеж, то надо ставить в конце запятую
conn.commit()

sql = '''
	SELECT
		id, original_url, short_url, created
	FROM
		shortener
'''

cursor.execute(sql)

# 3.2. Если запрос на выборку данных (SELECT), то:

result = cursor.fetchall()
print(result)

# 4. Закрываем соединение с БД
conn.close()





# Контекстный менеджер!!!!
"""
try:
	....
finally:
	.....
"""

with sqlite3.connect('db.sqlite')
	sql = 'SELECT * FROM shortener'
	cursor = conn.execute(sql)
	print(cursor.fetchall())
