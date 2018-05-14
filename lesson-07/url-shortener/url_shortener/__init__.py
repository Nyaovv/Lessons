from collections import namedtuple, OrderedDict
import sys

from url_shortener import storage

get_connection = lambda: storage.connect('shortener.sqlite')
#Анонимная функция.


Action = namedtuple('Action', ('func', 'name'))
actions = OrderedDict()


def menu_action(cmd, name=None):
	def decorator(func):
		nonlocal name
		name = name or func.__doc__
		actions[cmd] = Action(func, name)
		return func
	return decorator


@menu_action('1')
def action_add():
	"""Добавить URL-адрес"""
	url = input('\nВведите URL-адрес: ')

	with get_connection() as conn:
		short_url = storage.add_url(conn, url)


@menu_action('2', 'Найти оригинальный URL-адрес')
def action_find():
	"""Найти оригинальный URL-адрес"""


@menu_action('3', 'Вывести все URL-адреса')
def action_find_all():
	"""Вывести все URL-адреса"""
	with get_connection() as conn:
		urls = storage.find_all(conn)

		template = '{url[short_url]} - {url[original_url]} - {url[created]}'

		for url in urls:
			template.format(url['short_url'], url['original_url'])


@menu_action('m', 'Показать меню')
def action_show_menu():
    """Показать меню"""
    menu = []

    for cmd, action in actions.items():
    	menu.append('{}. {}'.format(cmd, action.name))

    print('\n'.join(menu))

@menu_action('q', 'Выйти')
def action_exit():
	"""Выйти"""
	sys.exit(0)
	


def main():
	with get_connection() as conn:
		storage.initialize(conn)
	
	action_show_menu()
	

	while 1:
		cmd = input('\nВведите команду: ')
		action = actions.get(cmd)
		
		if action:
			action()
		else:
			print('Неизвестная команда')
			
