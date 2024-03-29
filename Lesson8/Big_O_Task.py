import time

def print_num(arr: list):
    t = time.time()
    for i in arr:
        print(i, end=' ')
    print()
    print(time.time() -t)

# print_num([34, 23, 12, 54, 13] * 100000)


#сложность времени 0(n^2)

def print_pairs(arr: list):
    t = time.time()
    for num1 in arr:
        for num2 in arr:
            print(num1, num2, end= ' | ')
    print()
    print(time.time() - t)

print_pairs([34, 23, 12, 54, 13]* 100)