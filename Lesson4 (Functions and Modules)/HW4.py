from Lesson4 import *
from functools import reduce

import Lesson4 as l
import math
import time
import datetime


result = l.current_date


# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа):  периметр квадрата, площадь квадрата и диагональ квадрата.



# @decorator_run
def square(side):
    perimetr = 4 * side
    square = side * side
    diagonal = math.sqrt(2 * side * side)
    return (perimetr, square, diagonal)

a = 10
print(square(a))


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer


def function(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} - {value}')
    # return args

a = {'name': 'John', 'last_name':'Smith', 'age': 35, 'position': 'web developer'}
# function(**a)

# print(function(**a))


# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

my_list = [20, -3, 15, 2, -1, -21]

my_list_positives = list(filter(lambda i: i > 0, my_list))
print(my_list_positives)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)

res1 = reduce(lambda x, y: x + y, list1) # reduce - тоже функция высшего порядка, как и filter()
# how it works: list1 = [324, 12, 53, 765, 578] - for iteration 1: x = 324, y = 12, they are summed - 336
#  for iteration 2 - x = 336, y = 53 and so on
# difference between filter() and reduce() - reduce returns only 1 value  and it's needed to wrap it with list
print(res1)


my_list_multiple = reduce(lambda a, b: a * b, my_list)
print(my_list_multiple)

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

def decorator_run(func):
    def wrapper(*args):
        start_timestamp = time.time()
        print(start_timestamp)
        run = func(*args)
        end_timestamp = time.time()
        print(end_timestamp)
        unixtime = end_timestamp - start_timestamp
        print(f'Result of the {func.__name__} runtime is {unixtime}') #__name__ is a special built-in variable that
                                      # contains the name of the current module. When you use func.__name__, you're
                                      #accessing the __name__ attribute of the function func.
        return run
    return wrapper

@decorator_run
def calculatenew(x,y):
    return x + y

calculatenew(543, 543535)


# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.