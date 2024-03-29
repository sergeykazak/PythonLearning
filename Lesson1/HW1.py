import Lesson2

#1.1

# Напишите программу, которая на входе получает имя пользователя, сохраняет его в переменную user_name
# и выводит строку  "Hello {user_name}!"

# username = input('What is your username?')
# print(f"Hello {username}")
# print("Hello {}".format(username))

# Напишите программу, которая на входе получает 2 числа, производит с ними
# арифметическую операцию(на ваше усмотрение), и выводит “Результат = {результат}”.



# Set the environment variable to a higher limit (e.g., 10000)
# os.environ['PYTHONINTLONGDIG'] = '10000'
#
#
# a = int(input('Input number A' ':' + ' '))
# b = int(input('Input number B' ':' + ' '))
# result1 = a ** b
# result2 = a // b
# result3 = a % b
#
#
# print(f'A power B result: {result1}')
# print(f'Division remainder: {result3}')


# 1.2
#1) Напишите программу, чтобы вывести:
#
# *********
# *          *
# *          *
# *********

print('#' + '\n' + '# *******' + '\n' + '# *          *' + '\n' + '# *          *' + '\n' +'# *********')

# 1.3. **
# Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
#
# Пример:
#
# Input: 3498
#
# Output:
# Тысячи - 3
# Сотни - 4
# Десятки - 9
# Единицы - 8
print(" \n ")
inputNumber = int(input('Please input 4 digit number' ': ' ''))
print('This number contains the following: ')
print(f"Thousands: {inputNumber // 1000}")
print(f"Hundreds: {inputNumber // 100 % 10}")
print(f"Tens: {inputNumber % 100 // 10}")
print(f"Units: {inputNumber % 100 % 10}")


# 1.4. **
# Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы  (a+b)2
# и сумму квадратов a2+b2 этих чисел.
#
# Пример:
#
# Input:
# 3
# 2
#
#
# Output:
# Квадрат суммы 3 и 2 равен 25
# Сумма квадратов 3 и 2 равна 13

number1 = int(input("Input number A: "))
number2 = int(input("Input number B: "))
square_of_sums = (number1 + number2) ** 2
sum_of_squares = number1 ** 2 + number2 ** 2

print('Square of sums of {} and {} equals: {}'.format(number1, number2,square_of_sums))
print(f'Sum of squares of {number1} and {number2} equals: {sum_of_squares}')