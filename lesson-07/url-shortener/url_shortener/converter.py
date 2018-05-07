from string import ascii_letters, digits

valid_values = list(digits + ascii_letters)
radix = len(valid_values)


def convert(number):
	"""Конвертирует из 10 СС в нашу"""
	result = []
	
	while number:
		result.insert(0, valid_values[number % radix])
		number //= radix
		
	return '' .join(result)


def inverse(number):
	"""Переводит из нашей СС в 10"""
	result = 0
	
	for p, i in enumerate(reversed(number)):
		n = valid_values.index(i)
		result += n * radix ** p
	return result
