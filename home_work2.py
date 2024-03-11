"""
Взять любую задачу и настроить в ней запуск скрипта с параметрами.
(используем Пайчарм и модуль argparse)
"""

import argparse

parser = argparse.ArgumentParser(description='Введите 2 числа')
parser.add_argument('-a', type=int, default=1)
parser.add_argument('-b', type=int, default=2)
args = parser.parse_args()


def func_sum(a, b):
    return a+b


print(func_sum(args.a, args.b))
