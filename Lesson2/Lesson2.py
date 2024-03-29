#
# x = 5
# print (x==5)
# print (x > 3 and x < 8)
# print(x > 3 and x > 10)
#
# print (x > 3 or x > 10)
# print (not x < 3 )
# print (not x > 5)
#
# num = 12
# if num == 2:
#     print('Two')
# elif num < 13:
#     print('Number is less then 2')
# else:
#     print("Not equal to 2")
#
#
#
# message1 = 'hello'
# message2 = 'goodbye'
#
# if len(message2) > len(message1):
#     print(message2)
# else:
#     print(message1)
#
#
# a = 'O'
# b = 'Q'
# # print (a > b)  comparison is being made usint character's ASCII code value
#
# #  while cycle
#
# i = 0
# while i < 5:
#     print('current value is:', i)
#     i = i + 1
#     if i == 3:
#         continue # all what is written to do after continue will be skipped and will go to the next iteration right away
#     #     when continue is used here then i = 3 won't be printed cause program will go the line 37
#     #     and result will be 1 2 4 5
#     print(i)
#
# print(" \n ")
#
# j = 10
# while j > 1:
#     print(j)
#     j = j - 1
# print("Processing stopped")
#
#
# print('\n')
# for k in range(5):
#     print(k)
# #  in this case digits from 0 till 4 will be printed.
#
# print('\n')
# for m in range(1,5,1):
#     print(m)
# # in this case (1,5,1) - first 1, count will begin from 1 and end at 5 with step = 1
#
# word1 = 'Manufaktuuri'
# index_of_string = word1.index('tuu')
# print(f"The index of 'tuu' in Manufaktuuri is: {index_of_string}")
#
# for i in word1:
#     print(f'{word1.index(i)} - {i}')
#
# print('\n')
#
# word2 = "Manufaktuuri 16 81"
# for index, symbol in enumerate(word2):
#     print(f'{index} - {symbol}')
#
#
# # К FALSE ПРИРАВНИВАЮТСЯ СЛЕДУЮЩИЕ ЗНАЧЕНИЯ:
# # БУЛЕВА ПЕРЕМЕННАЯ FALSE
# # ЗНАЧЕНИЕ NONE;
# # ЦЕЛОЕ ЧИСЛО 0;
# # ЧИСЛО С ПЛАВАЮЩЕЙ ТОЧКОЙ 0.0;
# # ПУСТАЯ СТРОКА (' ');
# # ПУСТОЙ СПИСОК ([]);
# # ПУСТОЙ СЛОВАРЬ ({});
# # ПУСТОЕ МНОЖЕСТВО (SET())
# #
# # ВСЕ ОСТАЛЬНЫЕ ЗНАЧЕНИЯ ПРИРАВНИВАЮТСЯ К TRUE.
#
# # all above mentioned can be checked using:
# print(bool(''))
# # where replace '' with desired input
#
# arr = ''
# if arr:
#     print("Not empty")
# else:
#     print("Empty")
# # '' - is a boolean expression with value False, therefore above provided code returns Empty
#
# # ФУНКЦИЯ В PYTHON - ОБЪЕКТ, ПРИНИМАЮЩИЙ АРГУМЕНТЫ И ВОЗВРАЩАЮЩИЙ ЗНАЧЕНИЕ. ОБЫЧНО ФУНКЦИЯ
# # ОПРЕДЕЛЯЕТСЯ С ПОМОЩЬЮ ИНСТРУКЦИИ DEF.
#
# def sum_new(x, y):
#     result = x + y
#     return result
#
#
# print(sum_new(534,5354))

# string = 'Hello'
# print(string[::-1])
# # [::-1] - mirror-like printing
#
# lst1 = [1,2,3]
# lst2 = [4,5]
# num = 10
#
# lst1.extend(lst2)
# print(lst1)
#
# lst1.append(num)
# print(lst1)
#
# lst3 = lst1 + lst2
# print(lst3)


# lstA = [1, 3, 5, 7]
# lstB = [2, 4, 6, 8]
# lstA.extend(lstB)
# a = sorted(lstA)
# print(a)
#
number = 20
lst = []
for i in range(number):
    if i % 2 == 0:
        lst.append(i)
print(lst)

numberA = 20
lst2 = ''
for i in range(20):
    if i % 2 == 0:
        lst2 += str(i)
print(lst2)