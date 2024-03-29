from functools import reduce

def sum_it(a, b, c = 10):
    # c = 10 - here is a sample of keyword argument (именнованного  аргумента)
    return a + b + c
print(sum_it(1,3))

# print(sum_it(c = 12, 1, 3)) Error : SyntaxError: positional argument follows keyword argument

def hello(fname, lname, age):
    return f'My name is {fname} {lname}. My age is {age}'

print(hello(41, 'Sergey', 'Kazakov')) #My name is 41 Sergey. My age is Kazakov


def pattern(length, char1 = '/', char2 = '*'):
    return (char1 + char2) * length + char1

print(pattern(10))
print(pattern(10, char1='&&&'))

min_value = min(5,435,6,13,6,-10)
print(min_value)

# Пространство имен (Namespace)
# В Python пространство имен — это место, где хранится переменная.
# Пространства имен реализованы в виде словарей, где ключи — это имена объектов, а значения — это сами объекты.
# 1. ВСТРОЕННОЕ ПРОСТРАНСТВО (BUILT-IN) ИМЕН СОДЕРЖИТ ИМЕНА ВСЕХ ВСТРОЕННЫХ ОБЪЕКТОВ PYTHON.
# 2. ГЛОБАЛЬНЫЕ (Global) ПРОСТРАНСТВА ИМЕН СОДЕРЖАТ ИМЕНА НА УРОВНЕ ОСНОВНОЙ ПРОГРАММЫ, ,
#    ПОЭТОМУ ПЕРЕМЕННЫЕ, НАХОДЯЩИЕСЯ В НЕМ, ЯВЛЯЮТСЯ ГЛОБАЛЬНЫМИ.
# 3. ЗАМКНУТОЕ  (ENCLOSED) ПРОСТРАНСТВО ИМЕН ВКЛЮЧАЕТ ИМЕНА, ОПРЕДЕЛЕННЫЕ ВНУТРИ ВНЕШНЕЙ ФУНКЦИИ.
# 4. Локальное (Local) пространство имен включает в себя локальные имена внутри функции.
#     ПЕРЕМЕННЫЕ, КОТОРЫЕ НАХОДЯТСЯ ВНУТРИ ФУНКЦИЙ, НАЗЫВАЮТСЯ ЛОКАЛЬНЫМИ


name = 'Alice'
def outer_function():
    name = 'Alex'
    def inner_function():
        # name = 'Andrew'
        return name
    return inner_function
enclosure = outer_function()
result = enclosure()
print(result)

# result : 1. if nothing is commented -> Andrew
#          2 if name = 'Andrew' is commented -> Alex
#          3. if name = 'Alex' is commented => Alice


# Decorator
# Декораторы в Python представляют функцию, которая в качестве параметра получает функцию и в качестве
# результата также возвращает функцию. Декораторы позволяют модифицировать выполняемую функцию, значения
# ее параметров и ее результат без изменения исходного кода этой функции.

def decorator_function(func):
    def wrapper(*arg):   # *arg - означает, что функция имеет произвольное значение параметров
        print(f'Wrapper function!') # в этот момент будет работать функция wrapper
        print(f'Wrapped function: {func.__name__}') # здесь мы вызываем оборачиваемую функцию
        print(f'Execute wrapper function') # выполняем функцию wrapper
        print(func(*arg))
        print('Exit from wrapper function')
    return wrapper

@decorator_function # аннотация для обращения к декоратору decorator_function
def candy_wrapper(item):
    return f'{item} is wrapped'

print(candy_wrapper('Candy'))

@decorator_function
def hello_all(name):
    return f'Hello! My name is {name}'

hello_all('Sergey')


x = 5
y = 10
def sum_it2(x,y):
    print(f'Locals: {locals()}')
    return x + y
print(f'Inside the function:{sum_it2(3,4)} ')
print(f'Outside the function: {x + y}')
print(f'Globals: {globals()}') # так мы увидим все переменные на global уровне


# Module
# Модуль в языке Python представляет отдельный файл с кодом, который можно повторно использовать в других программах.

import math
import modulefinder as m
from locale import delocalize as b
from keyword import *


arr = [68, 68, 35, 80, 476]
math.sin(90)
print(math.prod(arr))


import datetime
birthyear = 1981
current_date = datetime.date.today()
current_age = current_date.year - birthyear
print(current_date)
print(current_age)


def introduce(**kwargs):
    print(type(kwargs))
    print(kwargs)

introduce(name = 'Mike', lname = 'Smith', age = 54)


                          # **kwargs - common accepted notation
                          #** before a parameter in a function definition, it signifies that the function can accept
                          #any number of keyword arguments. These keyword arguments are captured as a dictionary
                          #within the function body, where the keys are the argument names and the values are
                          #the corresponding values passed to the function.
                          # *


def my_result(*args):
    print(type(args))
    print(*args)
my_result(342, 234, 234,12)

                     #*args notation is used to pass a variable number of positional arguments to a function.
                     # It collects these arguments into a tuple within the function.
                     # The asterisk (*) before args unpacks the arguments passed to the function into this tuple.


# Анонимные функции: лямбда-выражения
# Анонимные функции могут содержать лишь одно выражение, но и выполняются они быстрее.
# Анонимные функции создаются с помощью инструкции lambda. Кроме этого,
# В ОТЛИЧИЕ ОТ ОБЫЧНЫХ ФУНКЦИЙ, их не обязательно присваивать переменной,
# lambda функции не требуется инструкция return
#
# Синтаксис lambda функции
# 	lambda argument: manipulate(argument)
# 	lambda n: n*n


result1 = lambda x, y: x * y
print(result1(324, 234))

list1 = [324, 12, 53, 765, 578]
# new_list1 = filter()      # filter() - higher order function cause it takes another function as an argument
                          # and/or returns a function as its result.
# The filter() function in Python is used to filter elements from an iterable (like lists, tuples, etc.)
# based on a specified condition. It takes two arguments: a function and an iterable.
# The function passed as the first argument should return a boolean value (True or False).


#Option 1
def take_odd(num):
    if num % 2:
        return True
    else:
        return False

# Option 2
new_list1 = list(filter(lambda x: x % 2, list1))  # value will True if x%2 not equal to 0, cause True is 1
#                 for case: (lambda x: x % 2 == 0, list1) - for this case value will be True if x % 2 == 0
print(new_list1) # result will be : <filter object at 0x103234e20> until we wrap it with list

new_list2 = list(filter(take_odd, list1)) # here we applied custom function take_odd for argument instead of lambda
print(new_list2)

#result of 2 prints above will be the same : [53, 765]

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100,'5000', 4.23, -1000]
new_list_1 = list(filter(lambda i: isinstance(i, str) and 'a' in i, list_1))
print(new_list_1)

res1 = reduce(lambda x, y: x + y, list1) # reduce - тоже функция высшего порядка, как и filter()
# how it works: list1 = [324, 12, 53, 765, 578] - for iteration 1: x = 324, y = 12, they are summed - 336
#  for iteration 2 - x = 336, y = 53 and so on
# difference between filter() and reduce() - reduce returns only 1 value  and it's needed to wrap it with list
print(res1)


# task on DNA
def count_agtc(dna):
    a = dna.count("A")
    t = dna.count("")
    g = dna.count("G")
    c = dna.count("C")

    return a, g, t, c

print(count_agtc("AGTCGTCGACGTCGAGC"))


# Task on polyndrom

def is_polyndrom(text):
 #Option1 to solve this task
    text1 = text.lower()
    text2 = ''
    for char in text1:
        if char.isalpha(): #isalpha - returns True if all characters in the string are alphabetic
                            # (consist of only letters), otherwise it returns False.
            text2 += char
    return text2 == text2[::-1] #[::-1] - turns string from the end (-1) to start


#Option2 to solve this task via list
    # text1 = [i.upper() for i in text if i.isalpha()]
    # a = text1[:] #  is a form of slicing notation that creates a copy of the entire sequence text.
    # b = text1[::-1]
    # if a = b:
    #     return True
    # else:
    #     False


text = "А роза упала на лапу азора"
print(is_polyndrom(text))


starts_with = lambda x: x.startswith('W')
result = starts_with("Wsdfsf")
print(result)

#
# def newfunc(x: str) # при таком синтаксе у нас будут методы для строк


sq = lambda x, y: x**2  + y**2
print(sq(4, 5))

# написать функцию, которая принимает целые числа и возвращает True если числа делятся без остатка на 19 или 13

func = lambda x: True if x % 13 == 0 or x % 19 == 0 else False
# func = lambda x: x % 13 == 0 or x % 19 == 0 - то же, что и выше только в сокращенной форме

print(func(38))

data = {'мама', 'папа', 'автомобиль', 'дом', 'лом', 'гараж'}
sorted_data = sorted(data, key = lambda x: (-len(x), x)) # sorted принимает 3 параметра/
                                                        # третий параметр (len(x), x) - где len(x) - сортирует по длине
                                                        # x - сортирует по алфавиту/
                                                  # если есть оба len(x) и x - то сортирует и по алфавиту и по длине
                                          # -len(x) - сортирует в обратном порядке по длине, начиная с самых длинных

print(' '.join(sorted_data)) # результат: дом лом мама папа гараж автомобиль

a = [23, 3, 5, 2, 5, 76, 72]
sorted_data_numbers = sorted(a, key = lambda x: (x % 2)) # (x % 2, x) - при сортировке сначала будут четные
                                                    # а при (x % 2 ==0, x) - сначала будут нечетные
print(sorted_data_numbers)


# Task: to calculate number of positive ,negative and zero numbers
numbersAll = [-345, 54, -43, 0, 36, 4, -343, 43, -43343]

negative_numbers = list(filter(lambda x: x < 0, numbersAll))
zero = list(filter(lambda x: x == 0, numbersAll))
positive_numbers = list(filter(lambda x: x > 0, numbersAll))

print(f' Negative: {len(negative_numbers)}, Zero numbers: {len(zero)}, Positive numbers: {len(positive_numbers)}')


# map can be used to modify in bulk:
# map is used to apply a given function to each item of an iterable (like a list) and returns
# a map object (an iterator) which can then be converted into another data structure, usually a list or tuple.

#without map:

a = "543 43 41 424"
b = a.split()
print(b) # result will be list of strings: ['543,', '43,', '41,', '424']
# if we need digits use for loop

c = []
for i in b:
    c.append(int(i))
print(c) # result: [543, 43, 41, 424]

#with map:

d = list(map(int, a.split()))
print(d) # result : [543, 43, 41, 424]


#Task : from the list leave only items starting from 'S' OR  having 4 characters:

days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
b = list(filter(lambda x: len(x) == 4 or x[0] == 'S', days)) # instead of x[0] can use x.startswith('S')
print(b)
# result of print(b) with sorted: ['Five', 'Four', 'Nine', 'Seven', 'Six']
# result of print(b) without sorted: ['Four', 'Five', 'Six', 'Seven', 'Nine']



#Task: increase each item from the origitnal list in 3 times  and save it to the new list
numbers = [432, 546,88, 132, 756, 253, -24, -35, -54 , 43]
increase_3 = list(map(lambda x: x * 3,numbers))
print(increase_3 )


#Task: write decorator that wraps function with phrases Hello and Goodbye. Hello is printed before call of the function.
#  Goodbye is printed after call.


def text_decor(func):
    def dec(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs) # for this line of code 'I am just a simple python func' is printed from simple_func
        print('Goodbye')
    return dec

@text_decor
def simple_func():
    print('I am just a simple python func')

simple_func()
