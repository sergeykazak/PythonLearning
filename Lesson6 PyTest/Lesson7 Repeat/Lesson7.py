
def factorial(n):
    # for i in range(5): # range that will be created: from 0 to 4
    result = 1
    for i in range(1, n+1):  # n+1 - cause we need to have whole range in method calculation: if n = 5 to have 5 in range
        result *= i
    return result
print(factorial(5)) # 120 = 1 * 2 * 3 * 4 * 5

#  with recursion

def factorialRecursia():
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(-2)) # 120 = 1 * 2 * 3 * 4 * 5


#Task: find substring in string and pring "hit' if found and 'Missed' if not:

# def findSubstring(st, subst):
#     if subst.lower() in st.lower():
#         return 'Hit'
#     else:
#         return 'Missed'
#
# print(findSubstring('Andy', 'a'))
#
# # solution with List Comprehesion
#
# def findSubstr(st, subst):
#     return ('Hit' if subst.lower() in st.lower() else 'Missed')
#
# print(findSubstr('Football', 'LL'))


# write method to find 1st and last index of the letter in the string
# Option1
def first_last(letter, st):
    lst = []
    if letter not in st:
        return None, None

    for index, char in enumerate(st):
        if char == letter:
            lst.append(index)
    return lst[0], lst[-1]

print(first_last('o', 'observation'))


# Option2

def first_last_new(letter, st):
    start_index = st.find(letter)
    if start_index == -1:
        return None, None
    final_index = st.rfind(letter)
    return start_index, final_index

print(first_last_new('n', 'anakonda'))


#Task: from the string 'гр@ол@лз@ож@вф@aa@' remove @ and preceding letter character to get 'голова'

def clearString(st):
    lst = []
    for i in st:
        if i != '@':
            lst.append(i)
        else:
            lst.pop()
    return ''.join(lst)

print(clearString('гр@ол@лщ@ож@вф@aa@'))