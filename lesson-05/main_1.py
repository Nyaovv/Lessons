# Модули и пакеты

# 1. Импорт модуля "целиком"
import os.path as Path # Добавил псевдоним с помочью 'as'
import square_shapes   # Псведоним используется для скоращения,
# удобства написания, и равзрешения конфликтов.



# 2. Частичный импорт
from square_shapes import (
    calculate_rectangle_area,
    calculate_circle_area as calc_circle_area
) # Если импорт не влезает в одну строчку, то можно перенести
  # с помощью скобок
# from os import path

# 3. Импорт * (все имена из модуля)
from square_shapes import *

print(square_shapes.calculate_square_area(5))
print(square_shapes.calculate_rectangle_area(4, 3))

# os.path.basename('/home/itmo/1.txt')

print(calculate_rectangle_area(7, 8))


if __name__ == '__main__':
    print('Будет работать только если модуль используется как исполняемый - главный')
