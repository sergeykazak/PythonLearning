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