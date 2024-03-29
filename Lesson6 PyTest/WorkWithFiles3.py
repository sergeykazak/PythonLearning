# Task
# find all words in file ending with 'll' and provide them on the screen
# !!! It's necessary to:
# - exclude duplications
# - bring all words to uppercase
# - alocate words on the screen (output) in the order of double sorting:
#  a) intiall to sort accordint to  the word length increase
#  b) if lenght is the same the allocate them in alphabetic order

from pprint import pprint
file_name = 'TestFileW.txt'


# Option 1
# with open(file_name, mode = 'r', encoding='utf-8') as f:
#     lst = set() # use set() cause it excludes duplicates
#     for word in f:
#         print(word)
#         a = word.strip().split()
#         for i in a:
#             c = i[-2:]
#             if c.upper() == 'LL':
#                 lst.add(i.upper())
# pprint(lst)
#
# for i in sorted(lst, key= lambda x: (len(x), x)): # sorted returns list sorted by length and alphabet simultaneously
#     print(i)
   # третий параметр (len(x), x) - где len(x) - сортирует по длине
# x - сортирует по алфавиту/
# если есть оба len(x) и x - то сортирует и по алфавиту и по длине
# -len(x) - сортирует в обратном порядке по длине, начиная с самых длинных

# Option 2

with open(file_name, 'r', encoding='utf-8') as file:
    lst = set()
    for word in file:
        a = word.strip()
        if a.upper().strip()[-2:] == 'LL':
            lst.add(word.upper().strip())
#
# pprint(lst)

for i in sorted(lst, key=lambda x: (len(x), x)):
    print(i)