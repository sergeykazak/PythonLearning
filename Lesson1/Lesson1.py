print('Hello Pyhon')

message = 'First lesson'


number = 132121

print(id(message))
#  method id shows memory address where variable message is stored
#  all variables in Python have reference type, there are no primitives
number_new = 132121

print(id(number_new))
print(id(number))
# в python применяется ссылочная семантика , т.е. на 132121 ссылаются уже две переменные number и number_new

message_new = 'First lesson'

print(id(message_new))
# both variables message and message new reference to the same memory address cause their values are the same

# 1value = One
# print(1value)

s = 121
d = 'True'
f = True
print(type(s))
print(type(d))
print(type(f))
# type shows variable data type

# data type transformation:

num1 = 5
num2 = '6'
print(num1 + int(num2))

a = 5
b = "books"
print(str(a) + ' ' +  b)

print(342 // 42) #целочисленное деление
print (452344 % 424) #остаток от деления

# for user's data input method INPUT() is being used
# sample: Name = INPUT()
# Note: INPUT by default outputs string values, so for correct handling numbers it's necessary to
# transform data to the INT type: => NUM = INT(INPUT())

# for data output method PRINT() is being used


message = input('Waiting for you DOB: ')
print(message)

number = input('How old are you: ')
print(f'Your age is:{number}')
#  ChatGPT
# In Python, an f-string, or formatted string literal, is a way to embed expressions inside string
# literals, using curly braces {}. F-strings are prefixed with the letter 'f' or 'F' and are available
# in Python 3.6 and later versions.

# another way to print data
name = input()
print('Your age is, {}'.format(str(number)))



ChatGPT
# The import os statement in Python is used to bring the os module into your script or program.
# The os module provides a way to interact with the operating system, allowing you to perform various operations related to the file system, environment variables, and more.
#
# ChatGPT
# The import os statement in Python is used to bring the os module into your script or program.
# The os module provides a way to interact with the operating system, allowing you to perform
# various operations related to the file system, environment variables, and more.
#
# Some common functionalities provided by the os module include:
#
# File and Directory Operations:
# os.listdir(): Returns a list containing the names of the entries in the given directory.
# os.mkdir(): Creates a directory.
# os.remove(): Removes a file.
# os.rmdir(): Removes an empty directory.
# os.path.join(): Joins path components intelligently.
# File Path Manipulation:
# os.path.exists(): Checks if a path exists.
# os.path.abspath(): Returns the absolute path of a file.
# os.path.join(): Joins path components intelligently.
# Environment Variables:
# os.environ: A dictionary containing the environment variables.