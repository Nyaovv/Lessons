# Пакеты
import mega_math.square_shapes
mega_math.square_shapes.calculate_square_area(2)

from mega_math import square_shapes
square_shapes.calculate_circle_area(10)

from mega_math.square_shapes import calculate_triangle_area
calculate_triangle_area(1, 2, 3)

# Относительный импорт
# Не работает в исполняемом (главном) модуле!
# from . import module_name
# from .module_name import func_name
# from ..parent_module import klass_name

from mega_math import calculate_rectangle_area
