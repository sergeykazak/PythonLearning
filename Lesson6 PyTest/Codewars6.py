# Regex count lowercase letters
# Your task is simply to count the total number of lowercase letters in a string.

import re
def lowercase_count(strng):
    pattern = r'[a-z]'
    x = re.findall(pattern, strng, re.fullmatch())
    print(len())


# Regexp Basics - is it a digit?
# Option 1
import re
def is_digit(n):
    pattern = r'\d'
    x = re.findall(pattern,n)
    if n in x:
        return True
    else:
        return False
    #your code here

#Option 2:
# import re
# def is_digit(n):
#     return bool(re.fullmatch(r'\d', n))

# Simple validation of a username with regex
# Write a simple regex to validate a username. Allowed characters are:
#
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

import re
# Option 1

def validate_usr(username):
    pattern = r'[a-z0-9_]{4,16}'
    x = re.fullmatch(pattern, username)
    return bool(x)

# Option 2
def validate_usr(username):
    pattern = r'[a-z0-9_]{4,16}'
    print(username)
    x = re.fullmatch(pattern, username)
    print(x)
    if x is not None:
        return True
    else:
        return False


# if x is None, meaning the username did not match the pattern, then bool(x) will be False.
# If x is not None, meaning the username did match the pattern, then bool(x) will be True.

# Option 3
import re
# validate_usr = lambda str: bool(re.match('^[a-z\d_]{4,16}$', str))


# Filter the number
# Filter the number
#
# Oh, no! The number has been mixed up with the text. Your goal is to retrieve the number from the text, can
# you return the number back to its original state?
#
# Task
#
# Your task is to return a number from a string.
#
# Details
#
# You will be given a string of numbers and letters mixed up, you have to return all the numbers in that string
# in the order they occur.

import re
# Option 1
def filter_string(st):
    pattern = r'\d'
    x = re.findall(pattern, st)
    return int(''.join(x))

# Option 2
def filter_string(st):
    pattern = r'\D' # all except digits
    x = re.sub(pattern, '', st)
    return int(x)

import re

def is_it_a_num(s):
    print(s)
    pattern = r'\D'
    x = re.sub(pattern, "   ")
    print(x)
    y = ' '.join(x)
    print(y)
#     if s == x:
#         return
#     else:
#         return 'Not a phone number'


# Fix My Phone Numbers!
# Oh thank goodness you're here! The last intern has completely ruined everything!
#
# All of our customer's phone numbers have been scrambled, and we need those phone numbers to annoy them with endless
# sales calls!
#
# The Format
# Phone numbers are stored as strings and comprise 11 digits, eg '02078834982' and must always start with a 0.
# However, something strange has happened and now all of the phone numbers contain lots of random characters,
# whitespace and some are not phone numbers at all!
#
# For example,  '02078834982' has somehow become 'efRFS:)0207ERGQREG88349F82!' and there are lots more lines
# that we need to check.
#
# The Task
# Given a string, you must decide whether or not it contains a valid phone number. If it does, return the
# corrected phone number as a string ie. '02078834982' with no whitespace or special characters, else return
# "Not a phone number".

import re

def is_it_a_number(s):
    pattern = r'\D'
    phone_number_string = ''.join(re.sub(pattern, '', s))
    if len(phone_number_string) == 0 and phone_number_string.startswith('0'):
        return phone_number_string
    else:
        return "Not a phone number"



#Anything
        # What is the answer to life the universe and everything
#
# Create a function that will make anything true
#
#     anything({}) != [],          'True'
#     anything('Hello') < 'World', 'True'
#     anything(80) > 81,           'True'
#     anything(re) >= re,          'True'
#     anything(re) <= math,        'True'
#     anything(5) == ord,          'True'

# use this https://www.pythonpool.com/python-__lt__/

# TO READ:  https://docs.python.org/3/reference/datamodel.html

def anything(thing):
    """
        try to return anything else :)
    """
    return ComparisonAlwaysTrue()


class ComparisonAlwaysTrue:
    def __lt__(self, *args):
        return True

    def __le__(self, *args):
        return True

    def __gt__(self, *args):
        return True

    def __ge__(self, *args):
        return True

    def __eq__(self, *args):
        return True

    def __ne__(self, *args):
        return True


# https://www.w3schools.com/python/ref_func_filter.asp
# https://www.geeksforgeeks.org/reduce-in-python/
# https://www.w3schools.com/python/ref_func_map.asp


# Between extremes

# DESCRIPTION:
#
# Given an array of numbers, return the difference between the largest and smallest values.
# For example:
# [23, 3, 19, 21, 16] should return 20 (i.e., 23 - 3).
# [1, 434, 555, 34, 112] should return 554 (i.e., 555 - 1).
#
# The array will contain a minimum of two elements.
# Input data range guarantees that max-min will cause no integer overflow.

between_numbers = lambda x: max(x) - min(x)


