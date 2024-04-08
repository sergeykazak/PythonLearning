# Simple Fun #9: Array Packing

# Task
#
# You are given an array of up to four non-negative integers, each less than 256.
#
# Your task is to pack these integers into one number M in the following way:
#
# The first element of the array occupies the first 8 bits of M;
# The second element occupies next 8 bits, and so on.


def array_packing(arr):
        binary = []
        for i in arr[::-1]: #переворачиваем массив
            i_bin = bin(i)[2:] #отрезаем все с 0 по 2 символ
            binary.append('0' * (8 - len(i_bin)) + i_bin) #добавляем недостающие нули до 8 символов
            print(binary)
        str_long = ''.join(binary)
        print(str_long)
        return  int(str_long,2) #переводим string в двоичный  integer


# Count characters in your string

# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.

#!!!!! Hint: use https://docs.python.org/3/library/collections.html#collections.Counter

from collections import Counter

def count(s):
    return Counter(s)


# If you can read this...

# Task
# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).
#
# Input:
# If, you can read?
#
# Output:
# India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo

# from preloaded import NATO # NATO['A'] == 'Alfa', etc


from preloaded import NATO  # NATO['A'] == 'Alfa', etc

def to_nato(words: str) -> str:
    dict = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
            'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
            'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
            'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}
    lst = []
    for i in words:
        if i.upper() in NATO.keys():
            lst.append(NATO[i.upper()])
        else:
            if i != ' ':
                lst.append(i)

    return ' '.join(lst)

# Option 2 with list comprehension usage:

return ' '.join(NATO.get(c, c) for c in words.upper() if c != ' ')
#get method in python: https://www.w3schools.com/python/ref_dictionary_get.asp

#Option 3 with lambda expression instead of function usage:

from preloaded import NATO  # NATO['A'] == 'Alfa', etc

to_nato = lambda words: ' '.join(NATO.get(c,c) for c in words if c != ' ')


# Analysis of Algorythms: Big O Analysis
# https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/

# https://blog.garybricks.com/efficiency-and-big-o-notation-overview-with-python-examples

# https://medium.com/analytics-vidhya/big-o-notations-and-its-examples-in-python-9d7e3c1ef09d


# Find the unique number
#DESCRIPTION:

# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
# findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# This is the first kata in series:
#
# Find the unique number (this kata)
# Find the unique string
# Find The Unique

# Option with bad perfomance:
def find_uniq(arr):
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            return arr[i]
    # your code here
    return n   # n: unique number in the array

#Option with good performance:
def find_uniq(arr):
    a, b = set(arr)
    if arr.count(a) == 1:
        return a
    return b


# Exclamation marks series #7: Remove words from the sentence if it contains one exclamation mark

# Description:
#
# Remove words from the sentence if they contain exactly one exclamation mark. Words are separated by a single space,
# without leading/trailing spaces.
#
# Examples
#
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove(s):
    x = []
    w = s.split()
    for i in w:
        if i.count('!') == 1:
            continue
        else:
            x.append(i)
    return ' '.join(x)


# All Star Code Challenge #15
# Your family runs a shop and have just brought a Scrolling Text Machine
# (http://3.imimg.com/data3/RP/IP/MY-2369478/l-e-d-multicolour-text-board-250x250.jpg) to help get some more business.
# The scroller works by replacing the current text string with a similar text string, but with the first letter
# shifted to the end; this simulates movement.
# Your father is far too busy with the business to worry about such details, so, naturally,
# he's making you come up with the text strings.
# Create a function named rotate() that accepts a string argument and returns an array of strings with each
# letter from the input string being rotated to the end.
#
# rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"

def rotate(str_):
    lst = []
    for i in range(len(str_)):
        str_ = str_[1:] + str_[0]
        lst.append(str_)
    return lst


# Greatest Position Distance Between Matching Array Values
# The goal of this Kata is to return the greatest distance of index positions between matching number values
# in an array or 0 if there are no matching values.
#
# Example: In an array with the values [0, 2, 1, 2, 4, 1] the greatest index distance is between the matching
# '1' values at index 2 and 5. Executing greatestDistance/greatest_distance/GreatestDistance with this array
# would return 3. (i.e. 5 - 2)
#
# Here are some extra examples:
#
# [0, 2, 1, 2, 4, 1]            => 3 (1's at indices 2 and 5)
# [9, 7, 1, 2, 3, 7, 0, -1, -2] => 4 (7's at indices 1 and 5)
# [0, 7, 0, 2, 3, 7, 0, -1, -2] => 6 (0's at indices 0 and 6)
# [1, 2, 3, 4]                  => 0 (no repeated elements)

# To do at home!!!!!!!!!

# Password maker

# DESCRIPTION:
#
# One suggestion to build a satisfactory password is to start with a memorable phrase or sentence and make
# a password by extracting the first letter of each word.
#
# Even better is to replace some of those letters with numbers (e.g., the letter O can be replaced with
# the number 0):
#
# instead of including i or I put the number 1 in the password;
# instead of including o or O put the number 0 in the password;
# instead of including s or S put the number 5 in the password.
# Examples:
#
# "Give me liberty or give me death"  --> "Gml0gmd"
# "Keep Calm and Carry On"            --> "KCaC0"

import re
def make_password(phrase):
    lst = phrase.split('')
    password = ''
    for i in lst:
        password += i[0]
        password = re.sub('[iI]]','1', password)
        password = re.sub('[oO]]','0', password)
        password = re.sub('[sS]]','5', password)
    return password

# Option B using maketrans method
TABLE = str.maketrans('iIoOsS','110055')

def make_password(s):
    return ''.join(w[0] for w in s.split()).translate(TABLE)

# Option 3
SWAP = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}

def make_password(phrase):
    return ''.join(SWAP.get(a[0], a[0]) for a in phrase.split())

# Option4

def to_num(word):
    match list(word):
        case ('I' | 'i'), *_: return '1'
        case ('O' | 'o'), *_: return '0'
        case ('S' | 's'), *_: return '5'
        case char, *_:        return char

def make_password(sentence):
    return ''.join(to_num(word) for word in sentence.split())