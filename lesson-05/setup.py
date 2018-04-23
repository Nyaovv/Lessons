"""
name         - название пакета
verstion     - версия пакета
description  - описание пакета 
url          - URL-адрес сайта
license      - Лицензия
author       - имя автора
author_email - эмейл автора

packages     - пакеты, которые нужно скопировать
            (без рекурсии, необходимо указать вложенные пакеты)
py_modules   - модули, которые нужно скопировать

scripts      - запускаемые из командной строки скрипты

install_requires - зависимости пакета от других пакетов
"""
from setuptools import setup

setup(
    name='mega-math',
    verstion='0.0.1',
    description='Collection of methematical formulas.',
    url='https://github.com/nyaovv/mega-math',
    license='Apache 2.0',
    author='Vladimir Kandrin',
    author_email='plusfak@gmail.com',
    packages=[
        'mega_math',
        ]
)
