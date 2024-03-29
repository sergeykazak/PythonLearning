from functools import reduce

lst = [1, 3, 634, 543, 12, 43, 0, -32, -468]
#
#
# sum2 = list(map(lambda x: x+2, lst))
# print(sum2)
# # The map() function in Python returns an iterator, which is an object that can be iterated over (for example,
# # with a for loop), but it does not return a list or another type of collection by default.
# #
# # If you want to get a list from the map() function, you can explicitly convert it to a list using
# # the list() constructor.
#
print(sum2 := list(map(lambda x: x+2, lst))) # sample with walrus operator
# # The "walrus operator" := is a new operator introduced in Python 3.8. It is formally called the "Assignment
# # Expression" operator. This operator allows you to assign a value to a variable as part of an expression.
# # The walrus operator is particularly useful in situations where you want to assign a value to a variable and use
# # it in the same expression, especially in loops or when you want to avoid repeating calculations.
#
#
print(*sum2, sep='\n')
# # *sum2: The asterisk (*) symbol is used to unpack the elements of the sum2 iterable object.
# # It essentially means that each element of sum2 will be passed as a separate argument to the print function.
# # sep='\n': This specifies the separator between the items that are printed.
# # In this case, the '\n' specifies a newline character, so each item printed will be separated by a newline.
#
#
# def myfunc(a, b, c):
#     return a + b + c
#
# print(list(map(myfunc, (1,4,5,2), (32, 41, 12), (123, 12, 43)))) # [156, 57, 60] , where 156 = 1 + 32 + 123
#
# The map function in Python is used to apply a function to every item in an iterable (like a list) and return
# a new iterator that yields the results. It takes two arguments: the function you want to apply, and the
# iterable you want to apply it to.
#
# def myfunc(a, b):
#     return a + b
#
#
# lst2 = [12, 32, 255]
# print(list(map(myfunc, lst, lst2))) #[13, 35, 889] - 13 = 1 + 12
#
# lst3 = reversed(lst)
# print(list(map(myfunc, lst, lst3))) #[44, 15, 1177, 1177, 15, 44]

#
# arr = list(map(int, input().split())) # sample when map uses int method to all input digits
# print(arr)
#
#
# arr = list(map(str, input().split())) # sample when map uses str method to all input data
# print(arr)

# arr1 = map(lambda x: int(x) * int(x), temp := input().split())
# print(*arr1)

# another way to write this can be:
# a, b, *c = map(lambda x: int(x) * int(x), temp := input().split())
# print(temp)
# print(a)
# print(b)
# print(c)
#
# a = map(sum, int(temp := input().split()))
# print(temp)
# print(a)

# print(result := sum(map(int, input().split()))) # working code instead of row above a = = map(sum, int(temp := input().split()))

#
# c = map(lambda x, y: int(x) * y, temp := input().split(), [34, 13, 0, -13])
# print(temp)
# print(*c)

#
# res = filter(lambda x: x > 4, lst)
# print(*res) #634 543 12 43

# res1 = filter(lambda x, y: x if x > y else y, lst)
# print(*res1)

print(list(filter(lambda x: x % 2 == 0 and x > 0, lst)))

lst3 = ['dog', 'cat', 'rabbit', 'crocodile', 'giraffe']
print([i.upper() for i in (list(filter(lambda x: len(x) < 5, lst3)))]) #['DOG', 'CAT']

print(*map(lambda y: y.upper(), list(filter(lambda x: len(x) < 5, lst3))))  #DOG CAT

# to work with method reduce() we need to import library functools

sum_ = reduce(lambda x, y: x + y, lst) #we write sum_ cause 'sum' is a reserved word
print(sum_)

# The reduce() function in Python is used to apply a specified function (typically with two arguments) to the
# items of an iterable, cumulatively, so as to reduce the iterable to a single value.
# It's part of the functools module in Python.

lst4 = [-1, 0, 1]
sum1 = reduce(lambda x, y: x + 10 if  x > y else x - 10, lst4)
print(sum1)

sum2 = reduce(lambda x, y: x if x > y else y, lst) # max value in the list looksup , result: 634
print(sum2)
