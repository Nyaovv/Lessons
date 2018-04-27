import os.path as Path
import sqlite3

SQL_INSERT_URL = '''
INSERT INTO shortener (original_url) VALUES (?)
'''
SQL_UPDATE_SHORT_URL = '''
	UPDATE shortener SET short_url=? WHERE id=?
'''
SQL_SELECT_ALL = '''
	SELECT
		id, original_url, short_url, created
	FROM
		shortener
'''

SQL_SELECT_URL_BY_ORIGINAL = SQL_SELECT_ALL +'WHERE=original_url=?'
SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'

# def connect(db_name=':memory:'):
def connect(db_name=None):
	"""Выполняет подключение к БД"""
	if db_name is None:
		db_name = ':memory:'
		
	conn = sqlite3.connect(db_name)
	# Магия !!!!
	
	return conn


def initialize(conn):
	"""Инициализирует структуру БД."""
	script_path = Path.join(Path.dirname(__file__), 'shema.sql')
	""" вместо /home/1/2.txt /\
	возращает /home/1
	если ещё /home и т.д."""
	
	with conn, open(script_path) as f: #старать сразу отдавать
		conn.executescript(f.read())# рез фун-ции другой 

def add_url(conn, url, domain=''):
	"""Добавляет URL-адрес в БД и возвращает короткий"""
	url = url.rstrip('/') """чтоб не хранить одинаковые юрл мы убираем слэши """
	
	if not url:
		raise RuntimeError("URL can't be empty. ")
	
	with conn: # что за with???
		found = find_url_by_origin(conn, url)
		
		if found:
			return found[2]
		
		cursor = conn.execute(SQL_INSERT_URL, (url,))
		
		pk = cursor.lastrowid
		# Магия по сокращению. \/ УЗНАТЬ
		short_url = '{}/{}'.format(domain.rstrip('/'), pk)
		
		conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))
		
		returh short_url
		
		
def find_url_by_origin(conn, origin_url):
	"""Возвращает URL-адрес по оригинальному URL."""
	origin_url = origin_url.rstrip('/')
	
	with conn:
		cursor = conn.execute(SQL_SELECT_URL_BY_ORIGINAL, (origin_url,))
		return cursor.fetchone()
		
		
