# Log without dates
import math


# You will be given an array of events, which are represented by strings. The strings are dates in HH:MM:SS format.
# It is known that all events are recorded in chronological order and two events can't occur in the same second.
# Return the minimum number of days during which the log is written.
#
# Example:
#
# Input -> ["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"]
# Output -> 1
#
# Input -> ["12:12:12"]
# Output -> 1
#
# Input -> ["12:00:00", "23:59:59", "00:00:00"]
# Output -> 2
#
# Input -> []
# Output -> 0

def check_logs(log):
    if len(log) == 0:
        return 0
    elif len(log) == 1:
        return 1
    days_counter = 1
    for i in range(1, len(log)):
        if log[i - 1] >= log[i]:
            days_counter += 1
    #             return days_counter

    # return the mininum number of days
    return days_counter


log1 = ["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"]
print(check_logs(log1))




# Refactored Greetings

# The following code could use a bit of object-oriented artistry. While it's a simple method and works
# just fine as it is, in a larger system it's best to organize methods into classes/objects.
# (Or, at least, something similar depending on your language)
#
# Refactor the following code so that it belongs to a Person class/object. Each Person instance will
# have a greet method. The Person instance should be instantiated with a name so that it no longer
# has to be passed into each greet method call.
#
# Here is how the final refactored code would be used:
#
# joe = Person('Joe')
# joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
# joe.name          # should == 'Joe'

#Option 1
class Person:
    def __init__(self,my_name):
        self.name = my_name

    def greet(self,your_name):
        return f'Hello {your_name}, my name is {self.name}'


#Option 2
# class Person(object):
#
#     def __init__(self, my_name):
#         self.name = my_name
#
#     def greet(self, your_name):
#         return "Hello %s, my name is %s" % (your_name, self.name) - instead of % characters python uses values from brackets



# These are not my grades! (Revamped !)

# At the end of the last semester, Prof. Joey Greenhorn implemented an online report card for his students in
# order to save paper. Everything seemed to be working fine back then, but since the start of the new semester
# he has received several emails from students complaining about erroneous grades showing up in their online
# report cards. Can you help him correct his implementation of the "Student" class?
#
# The "Student" class should behave like this :
#
# someStudent = Student()
# someOtherStudent = Student()
# someStudent.add_grade(98)
# someOtherStudent.add_grade(77)
# someStudent.grades == [98] # Evaluates to True
# someOtherStudent.grades == [77] # Evaluates to True


class Student:

    def __init__(self, first_name, last_name, grades=None):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)



# Person Class Bug

# The following code was thought to be working properly, however when the code tries to access the age of the
# person instance it fails.
#
# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)
# For this exercise you need to fix the code so that it works correctly.
#
# Note: the order of the person's full name is first name and last name.

# Option 1
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + ' ' + last_name

# Option 2 with separate @property decorator method
# class Person():
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     @property
#     def full_name(self):
#         return self.first_name + ' ' + self.last_name


# First-Class Function Factory

# Write a function, factory, that takes a number as its parameter and returns another function.
# The returned function should take an array of numbers as its parameter, and return an array of those
# numbers multiplied by the number that was passed into the first function.
# In the example below, 5 is the number passed into the first function. So it returns a function that
# takes an array and multiplies all elements in it by five.
#
# Translations and comments (and upvotes) welcome!

# HW




# Color Ghost

# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
#
# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"

import random


class Ghost:

    def __init__(self):
        color_options = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(color_options)

    pass


# Building Spheres
# Now that we have a Block let's move on to something slightly more complex: a Sphere.
#
# Arguments for the constructor
#
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)


# sizes = [width,length,height]
class Block:

    def __init__(self, sizes):
        self.width = sizes[0]
        self.length = sizes[1]
        self.height = sizes[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        return 2 * (self.width * self.length + self.length * self.height + self.width * self.height)

    # Good Luck!

# Building Spheres
import math


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = round(4 / 3 * math.pi * self.radius ** 3, 5)
        return volume

    def get_surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 5)

    def get_density(self):
        return self.mass / self.get_volume()


# Double value every next call

# This kata is about static method that should return different values.
# On the first call it must be 1, on the second and others - it must be a double from previous value.
# Look tests for more examples, good luck :)

class Class:
    counter = 1

    @staticmethod
    def get_number():

        Class.counter += 1
        return 2 ** (Class.counter - 1)



# OOP: Object Oriented Piracy

# Option A:
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        weight_unit = 1
        crew_member = 1.5 * weight_unit
        total_crew = self.crew * crew_member
        if self.draft - total_crew > 20:
            return True
        else:
            return False


# Option B;
# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#     # Your code here
#     def is_worth_it(self):
#         return self.draft - self.crew * 1.5 > 20


# Thinkful - Object Drills: Quarks

# Background
#
# You're modelling the interaction between a large number of quarks and have decided to create a Quark class so
# you can generate your own quark objects.
#
# Quarks are fundamental particles and the only fundamental particle to experience all four fundamental forces.
#
# Your task
# Your Quark class should allow you to create quarks of any valid color ("red", "blue", and "green") and any
# valid flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').
#
# Every quark has the same baryon_number (BaryonNumber in C#): 1/3.
#
# Every quark should have an .interact() (.Interact() in C#) method that allows any quark to interact with
# another quark via the strong force. When two quarks interact they exchange colors.



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def jump(self, number, direction='to the Right'):
        return f'Animal jumped {direction} {number} times'


class Dog(Animal):
    def __init__(self, breed, name, age):
        super().__init__(name, age)
        self.breed = breed

    def jump(self, **kwargs):
        dct = kwargs
        direction = dct['direction']
        number = dct['number']

        return f'Dog with name {self.name} jumped {direction} {number} times'

dog = Dog('Ovcharka', 'Max', 12)
print(dog.jump(number=14, direction='UP'))

print(Dog.__mro__)  # result: (<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)
                   # it demonstrate from left to the right all inheritance chain for class Dog



#  Задача реализовать класс Stack ,  у которого есть метод
# 1. Метод init - создает новый стек. Параметры не принимает. Создает атрибут экземпляра values, где в будущем
#  будут храниться элементы стека (list). Изначально при ининциализации значение равно пустому листу.
# 2. Метод push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# 3. Метод pop - удаляет верхний элемент из стека. Параметры не требуются. ничего не возвращает. Если пытаемся удалить
#  из пустого стека - то необходимо вывести сообщение  "Stack is empty"
# 4. Метод peek - возвращает верхний элемент стека, но не удаляет его. Параметры не требует, стек не изменяется.
#     Если стек пустой, то распечатайте пустой стек
# 5. Метод is_empty - проверяет пустой ли стек. Параметры не требует. Возвращает True или False.
# 6. Метод size - возвращает количество элементов в стеке. Параметры не принимает. Возвращает целое цисло.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


    def is_empty(self):
        return len(self.stack) == 0 # if it will be so then True

    def get_stack(self):
        return self.stack



stack1 = Stack()
print(stack1.is_empty())
print(stack1.get_stack())
stack1.pop() # result Stack is empty
# print(stack1.pop()) # returns None cause pring requires to receive something
stack1.push(2)
print(stack1.get_stack())
stack1.push('House')
stack1.push([12,312,43])
print(stack1.peek())
print('-----------------')

print(stack1.get_stack())
print(stack1.size())
stack1.pop()
print(stack1.get_stack())
