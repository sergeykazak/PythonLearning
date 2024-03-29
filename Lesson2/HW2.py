# from Lesson2 import sum_new

# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

# health = int(input("Need to check your current health level, Please provide current value: "))
#
# if  health <= 0:
#     print("False")
#     print("Your hero is dead. Please restart the game")
# else:
#     print("True")
#     print(f"You hero is alive. Its health is : {health}")


# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”


# number = int(input("Please input the number: "))
# if number % 2 == 0:
#     print(f'Number {number} that you\'ve provided is even')
# else:
#     print(f'Number {number} that you\' provided is odd')


# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и
# не являются столетиями (500, 600). Однако, если год делится без остатка
# на 400, он также считается високосным (1200, 2000)

#
# year = int(input("Please provide year: "))
#
# if year % 400 == 0:
#     print(f"Provided year: {year} is a leap year")
# elif year % 100 == 0:
#     print(f"Provided year: {year} is a not a leap year")
# elif year % 4 == 0:
#     print(f"Provided year: {year} is a leap year")
# else:
#     print("Stop")


# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

# text = input("The following text need to be printed: ")
# timesToPrint = int(input("How many times text should be printed: "))
#
# # for i in range(timesToPrint):
# #     print(f"Text that was provided by user is : {text} - iteration:  {i}")
#
#
# while timesToPrint > 0:
#     print(f"Text that was provided by user is : {text} - iteration:  {timesToPrint}")
#     timesToPrint -= 1
# else:
#     print("No more times to print the text")

# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

number1 = int(input("Please input first number: "))
number2 = int(input("Please input second number: " ))
operator = input("Please input which operation should be performed with number1 and number2."
                 " \n Possible values are: +, -, *, /: ")

def calculator(number1, number2, operator):
    if operator == "+":
        result = number1 + number2
        print(f'({number1} {operator} {number2} = {result}')
        return result
    elif operator == "-":
        result = number1 - number2
        print(f'({number1} {operator} {number2} = {result}')
        return result
    elif operator == '*':
        result = number1 * number2
        return result
    elif operator == '/':
        if number2 != 0:
            result = number1 / number2
        else:
            print(f'Operation can\'t be completed, cause number2 equals 0')
            return None
    else:
        print("System couldn't recognize which operation should be performed with provide numbers. Please try again.")
        return None
    print(f'Result {number1}{operator}{number2} = {result}')


