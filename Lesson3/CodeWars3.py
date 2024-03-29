#     # def check_alive(health):
#     #     if  health < 0:
#     #         return False
#     #     elif isinstance(health, (int, float)) &  0 < health < 10:
#     #         return True
#     #     else:
#     #         return False
#
#
#
#
#
# # Who ate the cookie?
#
# def cookie(x):
#     if isinstance(x, str):
#         return "Who ate the last cookie? It was Zach!"
#     elif isinstance(x, bool):
#         return "Who ate the last cookie? It was the dog!"
#     elif isinstance(x, (int, float)):
#         return "Who ate the last cookie? It was Monica!"
#
#
# # another option to solve cookie task:
# def cookie(x):
#     return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")

# Filter the number

def filter_string(st):
    stnew = ''
    for i in st:
        if i.isdigit():
            stnew += i
    return int(stnew)

# solution to the same task:
def filter_string(string):
    return int(''.join(filter(str.isdigit, string)))


# Sentence Smash
#
# Write a function that takes an array of words and smashes them together into a sentence
# and returns the sentence. You can ignore any need to sanitize words or add punctuation,
# but you should add spaces between each word. Be careful, there shouldn't be a space at the
# beginning or the end of the sentence!

def sentence(words):
    result = ''
    for item in words:
        result += item + ' '
    return result.strip()


# Needle in the haystack
# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:
# Example(Input --> Output)
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

def find_needle(haystack):
    wordToFind = 'needle'

    try:
        index = haystack.index(wordToFind)
        return f'found the needle at position {index}'
    except ValueError:
        return 'needle not found in the haystack'



haystack1 = ['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle1', 'something somebody lost a while ago']
result = find_needle(haystack1)
print(result)


# Selective fear of numbers
# I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated:
# The number I'm afraid of depends on which day of the week it is... This is a concrete description of my mental illness:
# Monday --> 12
# Tuesday --> numbers greater than 95
# Wednesday --> 34
# Thursday --> 0
# Friday --> numbers divisible by 2
# Saturday --> 56
# Sunday --> 666 or -666
# Write a function which takes a string (day of the week) and an integer (number to be tested) so it tells the
# doctor if I'm afraid or not. (return a boolean)

def am_I_afraid(day,num):
    if day == 'Monday' and num == 12:
        return True
    elif day == 'Tuesday' and num > 95:
        return True
    elif day == 'Wednesday' and num == 34:
        return True
    elif day == 'Thursday' and num == 0:
        return True
    elif day == 'Friday' and num % 2 == 0:
        return True
    elif day == 'Saturday' and num == 56:
        return True
    elif day == 'Sunday' and  num in (-666, 666):
        return True
    else:
        return False
    ... # your code here


# NATO Phonetic Alphabet (retired)
# Complete the function nato that takes a word in parameter and returns a string that spells the word using the NATO
# phonetic alphabet.
# There should be a space between each word in the returned string, and the first letter of each word should be capitalized.
# For those of you that don't want your fingers to bleed, this kata already has a dictionary typed out for you.
#
# Examples:
# "hi"      -->  "Hotel India"
# "abc"     -->  "Alpha Bravo Charlie"
# "babble"  -->  "Bravo Alpha Bravo Bravo Lima Echo"
# "Banana"  -->  "Bravo Alpha November Alpha November Alpha"

# LETTERS is preloaded

# LETTERS is preloaded

def nato(word):
    dict = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
            "H": "Hotel", 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
            'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
            'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}
    letters = list(word.upper())
    result = []
    for x in letters:
        if x in dict:
            result.append(dict[x])

    return ' '.join(result)

    pass

word1 = 'asgas'
a = nato(word1)
print(a)


# Converting 12-hour time to 24-hour time

# Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds
# easy enough, right? Well, let's see if you can do it!
#
# You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive),
# a minute (always in the range of 0 to 59, inclusive), and a period (either a.m. or p.m.) as input.
#
# Your task is to return a four-digit string that encodes that time in 24-hour time.
# Notes:
# By convention, noon is 12:00 pm, and midnight is 12:00 am.
# On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as,
# for example, 12:15 am. On 24-hour clock, this translates to 0015.

def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    timeIn24Format = ''

    modifiedMinute = '0' + str(minute) if minute < 10 else str(minute)
    if hour in range(1, 12) and period == 'am':
        timeIn24Format = '0' + str(hour) + modifiedMinute
    # elif hour == 10 and period == 'am':
    #     timeIn24Format = str(hour) + modifiedMinute
    # elif hour == 11 and period == 'am':
        timeIn24Format = str(hour) + modifiedMinute
    elif hour in range(1, 12) and period == 'pm':
        timeIn24Format = str(12 + hour) + modifiedMinute
    elif hour == 12 and period == 'am':
        timeIn24Format = '00' + modifiedMinute
    elif hour == 12 and period == 'pm':
        timeIn24Format = '12' + modifiedMinute
    return timeIn24Format

# Option B:
def to24hourtime(hour, minute, period):
    if period == 'pm' and 0 < hour < 12: hour += 12
    elif period == 'am' and hour == 12: hour = 0
    return f'{hour:02d}{minute:02d}'


# Jaden Casing Strings
# DESCRIPTION:
#
# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013).
# Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter,
# he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word,
# check out how contractions are expected to be in the example below.
#
# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes
# from Jaden Smith, but they are not capitalized in the same way he originally typed them.
#
# Example:
#
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    result = []
    for i in string.split():
        result.append(i.capitalize())
    return ' '.join(result)

s = 'safs asfsa asf asfas'
s1 = to_jaden_case(s)
print(s1)


# The mean of two means
# Write a function that takes as parameters an array (arr) and 2 integers (x and y).
# The function should return the mean between the mean of the the first x elements of the array
# and the mean of the last y elements of the array.
#
# The mean should be computed if both x and y have values higher than 1 but less or equal
# to the array's length. Otherwise the function should return -1.
#
# [1, 3, 2, 4], 2, 3 => should return 2.5
# because: the mean of the the first 2 elements of the array is (1+3)/2=2 and the mean of the
# last 3 elements of the array is (4+2+3)/3=3 so the mean of those 2 means is (2+3)/2=2.5.


def get_mean(arr, x, y):
    a = len(arr)

    if 1 < x <= a and 1 < y <= a:
        first_elements_mean = sum(arr[:x]) / x
        last_elements_mean = sum(arr[-y:]) / y
        first_last_mean = (first_elements_mean + last_elements_mean) / 2
        return first_last_mean
    else:
        return -1



# Filter the number
#
# Oh, no! The number has been mixed up with the text. Your goal is to retrieve the number from the text,
# can you return the number back to its original state?

# Task
# Your task is to return a number from a string.
# Details:
# You will be given a string of numbers and letters mixed up, you have to return all the numbers in that string in
# the order they occur.

def filter_strings(st):
    result = ''
    for i in list(st):
        if i.isdigit():
            result.append(i)
    return int(''.join(result))

a = 'aaaaa'
b = filter_strings(a)
print(b)

