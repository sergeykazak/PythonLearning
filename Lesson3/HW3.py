# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']
my_list_new = (my_list[-2])
tuple1 = tuple(my_list_new)
print(*tuple1)
print(my_list[2][2]) #prints last element (3') in the inner list [1,2,3]


# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100, '5000', 4.23]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100,'5000', 4.23, -1000]

# Option1
# result_list = sum([i for i in list_1 if isinstance(i, int)])
# print(result_list)

tuple2 = (list_1)
print(*tuple2)

# Option2 - is more correct cause it covers various cases like '5000', -1000, 4.23
sum = 0
for i in list_1:
    if type(i) in (int,float):
        sum += i
    # elif int(i): this results in ValueError: invalid literal for int() . so we need to use try catch
    #     sum += int(i)
    else:
        try:
            sum += int(i)
        except ValueError:
            continue
print(sum)

result_string = []
print(list)
for i in list_1:
     if isinstance(i, str) and 'a' in i:
         result_string.append(i)
print(','.join(result_string))

# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

listA = ['cat', 'dog', 'horse', 'cow']
tupleA = tuple(listA)
print(tupleA)


    # 3.4. Напишите программу, которая определяет, какая семья больше.
    #       1) Программа имеет два input() - например, family_1, family_2.
    #       2) Членов семьи нужно перечислить через запятую.
    #      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

family_1 = input("Please provide Family 1 members: ")
family_2 = input("Please provide Family 2 members: ")


if ',' in family_1:
    # Split the input string into a list of substrings using comma
    f1 = family_1.split(',')
    # Filter out empty strings resulting from consecutive commas
    f1_filtered = [i for i in f1 if i.strip()]
    print(f1)
    # break  # Break out of the loop since input is valid

    if ',' in family_2:
        # Split the input string into a list of substrings using comma
        f2 = family_2.split(',')
        # Filter out empty strings resulting from consecutive commas
        f2_filtered = [i for i in f2 if i.strip()]
        print(f2)
        # break  # Break out of the loop since input is valid

    if len(f1) > len(f2):
        print(f'Family 1 has more family members then Family 2')
    elif len(f1) < len(f2):
        print(f'Family 2 has more family members then Family 1')
    elif len(f1) == len(f2):
        print('Equal')
else: print("Input must contain commmas.")






# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

dict1 = {
    'title': 'Once upon a time in New York',
    'director': 'Sergio Leone',
    'year': 1984,
    'budget': 30000000,
    'main_actor': 'Robert De Niro',
    'slogan': 'As boys, they said they would die for each other. As men, they did.'
}

print(dict1.keys())
print(dict1.values())
print(*dict1.keys())
print(dict1.keys().mapping)

for key,value in dict1.items():
    print(f'{key} - {value}')

# In Python, a "view object" is an object that provides a dynamic view of the underlying data.
# Specifically, the items() method applied to a dictionary returns a view object that allows you to see
# the key-value pairs in the dictionary without making a separate copy of them. This means that changes
# to the dictionary are reflected in the view object, and vice versa.
# When you call items() on a dictionary, it returns a view object that contains tuples representing the
# key-value pairs. Each tuple in the view object consists of two elements: the key and its corresponding
# value from the dictionary.




# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

total_sum = 0
for i in my_dictionary:
    total_sum += my_dictionary[i]
print(total_sum)

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

# Option 1
listb = [1, 2, 3, 4, 5, 3, 2, 1]
list_without_duplicates = set(listb)
print(list_without_duplicates)

# Option 2

result_list = []
for i in listb:
    if i not in result_list:
        result_list.append(i)
print(result_list)


# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

# Option1
set_common_values = set1.intersection(set2)
print(set_common_values)

# Option2
commonvalues = set1&set2
print(commonvalues)


set1_set2_notcommon_values1 = set1.difference(set2)
set2_set1_notcommon_values2 = set2.difference(set1)
print(set1_set2_notcommon_values1)
print(set2_set1_notcommon_values2)

set1_is_superset_of_set2 = set1.issuperset(set2)
set2_is_superset_of_set1 = set2.issuperset(set1)

print(set1_is_superset_of_set2)
print(set2_is_superset_of_set1)

