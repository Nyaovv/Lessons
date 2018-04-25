# Exception - исключение

try:
	i = int(input())
	# print(i[0])
except VelueError:
	print('Не корректно число!')
except:
	print('Любое исключение было отловлено')
finally:
	print('Выполняется всегда!')
	
	
raise KeyError('Моё сообщение об ошибке')
