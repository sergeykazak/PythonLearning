# Списки (lists)
# Кортежи (tuples)
# Словари (dictionaries)
# Множества (sets)

# List представляют тип данных, которые хранят набор или последовательность элементов. Например:
# Модели автомобилей;
# Имена студентов;
# Посещенные страны;
# Посетители магазина и так далее;
# Могут хранить разные типы данных
# Создаются при помощи:
# Квадратных скобок        my_list = []
# Функции List()                my_list = list()
# Изменяемая структура данных

my_list = [1,2,3]
print(type(my_list))

# sentence = 'What a wonderful life'
# my_list_new = sentence.split(' ')
# print(my_list_new)
# my_list_new2 = list(sentence)
# print(my_list_new2)
#
numbers = [1, 2, 3, 4, 5, 6]
# for i in numbers:
#     print(i**2)
#
# print(numbers[0])
# print(numbers[5])
# print(numbers[-1])
# выше пример с отрицательной индексацией, которая удобна, когда неизвестна длина листа

# .append()	метод для добавления элементов в список
# .insert()	для добавления элементов в конкретное место в списке
# .index()	для получения индекса элемента
# .clear()	для очистки списка
# .remove()	для удаления элемента списка
# .reverse()	чтобы развернуть список в обратном порядке
# .count()	для подсчета количества элементов в списке
# sum()  для сложения элементов списка
# min()	 показывает элемент с самым низким значением в списке
# max()	 элемент с самым высоким значением в списке

print(id(numbers))

numbers[0] = 10
print(numbers)
print(id(numbers)) # мы прроверяем не происходит ли мутация in place. результат: адрес памяти (id) остается прежним
                   # после замены первого элемента списка

numbers2 = [213, 123, 534]
print(numbers.append(numbers2)) # результат будет None - спросить chatgpt
print(numbers)
print(id(numbers)) # мы прроверяем не происходит ли мутация in place. результат: адрес памяти (id) остается прежним
                  # после замены первого элемента списка

numbers.extend((numbers2)) # в этом случае по элементно добавятся элементы листа numbers2 в лист numbers
                           # результат будет [10, 2, 3, 4, 5, 6, 213, 123, 534]
print(numbers)


# сортировка листов

numbers = [324, 3, 1, 42, 53, 0]
print(id(numbers))
numbers.sort() # метод sort() мутирует исходны лист на месте (in place), т.е. лист отсортировали и он не меняется
print(numbers.sort()) # и sort() ничего не возвращает

print(numbers)
print(id(numbers))

# print(numbers.reverse()) # тоже вернет None
# print(numbers) # результат будет [324, 53, 42, 32, 1, 0]

print(sorted(numbers))  # результат будет [0, 1, 32, 42, 53, 324]
print(id(sorted(numbers))) #id будет уже другой, т.е. метод sorted() возвращает новый список/ при этом первоначальный
                           # список не изменится

print(numbers[0:3]) #вернет первые три элемента списка [0, 1, 32]
# print(numbers[::-1]) # так тоже можно развернуть список и результат будет [324, 53, 42, 32, 1, 0]

print(sum(numbers))
print(max(numbers))
print(min(numbers))


#Генерация списков (List Comprehension)
# позволяет использовать сокращенный синтаксис при создании нового списка на основе значений
# из уже существующего списка
# newlist = [expression for item in iterable if condition == True]

# Option  A c For loop
# l = [1, 2, 3, 4, 5]
# new_l = []
# for x in l:
#    if x%2:
#       new_l.append(x*x)
# print(new_l)

# !!!!!!
# # К FALSE ПРИРАВНИВАЮТСЯ СЛЕДУЮЩИЕ ЗНАЧЕНИЯ:
# # БУЛЕВА ПЕРЕМЕННАЯ FALSE
# # ЗНАЧЕНИЕ NONE;
# # ЦЕЛОЕ ЧИСЛО 0;
# # ЧИСЛО С ПЛАВАЮЩЕЙ ТОЧКОЙ 0.0;
# # ПУСТАЯ СТРОКА (' ');
# # ПУСТОЙ СПИСОК ([]);
# # ПУСТОЙ СЛОВАРЬ ({});
# # ПУСТОЕ МНОЖЕСТВО (SET())

numbers1 = [3, 4, 2, 3, 4, 5, 6]
numbers3 = []
for x in numbers1:
    if x % 2:  # значение это выражания будет True если будет остаток от деления, т.к. в Python целое число (0) приравннивается к нулю
        numbers3.append((x**2))
print(numbers3)
#  результат будет [1, 2809] , т.к. в листе numbers только 1 и 53 нечетные и только для них будет работать цикл

# тоже самое, но с применением List Comprehensions:

new_numbers = [x**2 for x in numbers if x % 2]
print(new_numbers)


print(len(numbers))  #len считает количество элементов в листе или длину списка

l2  = ['a', 2, 5, 'sdfa', 35, 0, None]
print(len(l2))

print(id(new_numbers))
numbers2 = new_numbers.copy()
print(id(numbers2)) # метод copy() позволяет получить новые список (у него id будет уже отличный от id листа numbers_new

# Кортежи (tuples)
# Кортежи создаются с помощью:
# 1. круглых скобок: ();     my_tuple = ()
# 2. Функции tuple()         my_tuple = tuple()
# 3. При перечислении нескольких значений через запятую:  my_tuple = 1, 2, 3
#
# Элементы внутри кортежей разделяются запятыми;
# Могут хранить разные типы данных
# Важно соблюдать особенности синтаксиса, характерные для каждого отдельного типа данных в кортеже — кавычки для
# строк, числа и булевые значения без кавычек и так далее.

#     my_tuple = (1, True, ‘name’, None)
# Кортежи – неизменяемая структура данных

# Кортежи используются в случаях, когда важно соблюдать целостность данных, например,
# координаты, названия штатов, название месяцев года и дней недели

my_tuple = (213, 'apple', None, 234, 0)
print(id(my_tuple))
print(my_tuple)

my_tuple1 = 32, 'dfgdg', None, 5423
print(my_tuple1)

print(tuple(numbers)) # метод tuple можно использовать для перевода листов в tuple
my_tuple2 = list(my_tuple1)
my_tuple2.append(12)
print(my_tuple2)

# С помощью кортежей можно передавать в функцию произвольное количество аргументов – def func(*args).
# Символ * означает, что кортеж нужно распаковать (раскрыть)
#    def func(*args):
#       for item in args:
#          return item*item
# print(func(2, 5, 6, 8, 10))

def func(*args):
    for item in args:
         return item*item # если использовать return, то функция func вернет только первое значение и это будет 4

print(func(2, 5, 6, 8, 10))

def func(*args):
    for item in args:
         yield item*item # yield работает по-другому в отличие от return и создает объект генератор?????



for i in func(1,2,3,4,2354,2352,235252):
    print(i)

print(numbers) # результат будет [0, 1, 3, 42, 53, 324]
print(*numbers) # печатаем лист с распаковкой (каждый элемент печатается отдельно). результат будет: 0 1 3 42 53 324


# Словарь (dictionary)
# Словарь в Python хранит коллекцию элементов, где каждый элемент имеет уникальный ключ и связанное с ним
# некоторое значение
# Создается при помощи:
# 1. фигурных скобок           my_dict = {}
# 2. Функции dict()            my_dict = dict()
# Имеет следующий синтаксис:
# dictionary = { ключ1:значение1, ключ2:значение2, ....}
# Ключи в словаре могут быть только строками, целыми числами или числами с плавающей точкой. А вот значения могут быть любого типа
# Важно не забывать использовать кавычки для ключа типа str
# Изменяемая структура данных


# .keys() — используется для вывода ключей словаря.
# .items() — используется для создания кортежей с ключами и значениями.
# .get() — метод для получения значения по ключу.
# .clear() — очистить словарь.
# .copy() — скопировать весь словарь.
# len() — получить длину словаря.
# type() — узнать тип.
# min() — получить ключ с минимальным значением.
# max() — получить ключ с максимальным значением.

mydict = {
    'name': 'Sergey',
    'surname': 'Kazakov',
    'age': 42,
    'city': 'Tallinn',
    'weight': 80.1
}

print(mydict) #{'name': 'Sergey', 'surname': 'Kazakov', 'age': 42, 'city': 'Tallinn', 'weight': 80.1}
print(list(mydict)) # ['name', 'surname', 'age', 'city', 'weight']
print(mydict['city']) # для получения значения определенного ключа

mydict['height'] = 182.1 # добавляем новый ключ со значением
print(type(mydict))

print(mydict.keys()) # keys() выводит только ключи словаря: dict_keys(['name', 'surname', 'age', 'city', 'weight', 'height'])

print(mydict.items()) #используется для создания кортежей с ключами и значениями:
# dict_items([('name', 'Sergey'), ('surname', 'Kazakov'), ('age', 42), ('city', 'Tallinn'), ('weight', 80.1), ('height', 182.1)])


print(len(mydict)) # узнать длину словаря

print(min(mydict))

newdict = mydict.copy()
mydict.clear()
print(mydict)
print(newdict)

print(newdict.keys())
print(newdict.values())
print(newdict.items())

print(newdict.pop('name'))
print(newdict)
print(newdict.get('name','Not found!!!')) #метод get пытается найти ключ 'name' и если не найдет то
                  # распечатает Not Found!!! т.к. пара с ключом name была ранее удалена через pop


for i in newdict.items():
    print(*i)

# получили распакованный cловарь:
# surname Kazakov
# age 42
# city Tallinn
# weight 80.1
# height 182.1


for i in newdict: # так можно распечатать все ключи в словаре
    print(i)

dictnumbers ={
    'first': 1,
    'hundred': 100,
    'fifty comma 7': 50
}
result = 0
for i in dictnumbers:
    result += dictnumbers[i]
print(result)


# Множества (sets)
# Множество похоже на словарь, в котором значения отброшены, а оставлены только ключи.
# Как и в словаре, ключи должны быть уникальными. То есть значения во множестве не должны повторяться
# Создается при помощи:
# 1. Перечисления элементов в фигурных скобках:   my_set = {‘a’,’B’,’c’}
# 2. Функции set{}                                my_set = set{}
#
# Множества используют для математических операций.
# Также множества удобно использовать для удаления повторяющихся элементов.
# К примеру, при выполнении set([1, 8, 2, 1, 5, 8, 9]) все дубликаты исчезнут.
# к элементу множества нельзя применить метод index(), т.к. положение элементов в нем постоянно меняется


# len(s) - число элементов в множестве (размер множества).
# x in s - принадлежит ли x множеству s.
# set.add() - добавляет элемент в множество.
# set.remove() - удаляет элемент из множества. KeyError, если такого элемента не существует.
# set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать,
# какой элемент будет первым.
# set.clear() - очистка множества
# set.issubset(other) или set <= other - все элементы set принадлежат other.
# set.issuperset(other) или set >= other - все элементы other принадлежат set


set1 = {23, 32, None, 'test', -233}
set2 ={64, 1,2, 23,5,6345, 0, 'abc'}
set3 = {1,2,5}

print(set2.issubset(set3)) #False
print(set3.issubset(set2)) #True

print(set2.issuperset(set3)) #True
print(set1.issuperset(set3)) #False

print(set1.intersection(set2)) #result: {23}
print(set2.intersection(set3)) #result: {1, 2, 5}

print(set2.difference(set1)) #result: {64, 1, 2, 0, 5, 6345, 'abc'}
print(set2.symmetric_difference(set1)) #result: {64, 1, 2, 0, 5, 6345, 'abc'} #возвращает все уникальные значения
                                       # из обоих множеств

print(set1.add(123)) #result None
print(set1)
