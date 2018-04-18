# Как объявить функцию?
# Функция - это блок кода,
# которой можно вызывать многократно

def hello():
    print('Hello!')

print(type(hello))
hello() # Вызов функции
hello()

say_hello = hello
say_hello()

# Зачем функции аргументы?

def hello_username(name):
    print('Hello, ', name)
    
hello_username('Python')
hello_username('JavaScript')
heelo_username('Вася')

def summa(a, b):
    print(a + b)
    
summa(1, 3)

# Передача значений аргументов по ссылке
def parse(src, output)
    src = src.strip('.')
    
    for i in src.split():
        output.append(i)

src = 'Python is programming language.'
output = []

print(src, output)
parse(src, output)
print(src, output)

def poww(x, p=2):
    print(x ** p)
    
poww(5)
poww(2, 3)

# По умолчанию всегда должен ставиться неизменяемые тип данных.

def f(i, l=None):
    l = l or []

# Переданный аргумент передается истине

# Как вернуть значение из функции?

def minus(a, b):
    return a - b
    a = a * b # Никогда выполняться не будет 
    
r = minus(1, 2)
print(r)

# return - поподробнее.

# Функция всегда возвращает какое-то полезное значение
# если она не возвращает, то это процедура. 

def f2():
    return 1, 2, 3

a, b, c = f2()

# Переменное количество аргументов в описании функции
def demo_func(i, j=0, *args, **kwargs):
    """
    args - кортеж
    kwargs - словарь
    """
    print(i, args, type(args))
    print(kwatgs, type(kwargs))

demo_func(1, 2, 3, j=4)
demo_func('10', '20', k=True, e=456)

def f3(i=1, *args, j=1, **kwargs): # для примера. Это зоопарк. 
    print(i, j, args)
    
f3(2, 2, 5, 5, j=2)

# Переменное количество аргументов при вызове функции
def f4(*i, j, k, a=None, b=None, c=None):
    print(i, j, k)
    print(a, b, c)

args = [1, 2, 3]
kwargs = {
    'a' : 10,
    'b' : 20,
    'c' : 30,
}
f4(*args, **kwargs)

# Анонимная функция

sqrt = lambda x: x ** 0,5
# lambda: pass
# lambda x, y: pass
print(sqrt(9))

def f5(x, cb):
    return cb(x)

print(f5(25, lambda x: x ** 0,5))
print(f5(25, lambda x: x ** x))

# Глобальная область видимости
# Локальные переменные - это область видимости функции

# Замыкания

# Функция каррирования
def trim(chars=None):
    # Оласть видимости (локальная) функции trim
    # Замкнутая область
    def f(s):
        # Область видимости (локальная) функции f
        return s.strip(chars)
    return f

spaces_trim=trim()
print(spaces_trim)
slashes_trim=trim('/\\')

print(spaces_trim('     Hello    '))
print(slashes_trim('//////url///\\\//'))

# Рекурсивная функция
# 5! = 1 * 2 * 3 * 4 * 5
def factorial(x): # вот это прям **** ваще повторить. 
    # Прямая рекурсия (когда вызывает сама же себя)
    return 1 if x == 0 else x * factorial(x - 1)

print(factorial(5))

# Косвенная рекурсия
#def a():
    #b()

#def b():
    #a()
    

g = 666

def wrapper():
    external = 777
    
    def func():
        global g
        nonlocal external
        
        g += 1
        external += 1
        
    func()
    
    print(g, external)
    
wrapper()
