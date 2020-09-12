import random

def random_with_sum(number_of_values, asserted_sum):
    trial = 0
    numbers = list(range(number_of_values))
    while True:
        trial += 1
        for i in range(number_of_values):
            numbers[i] = random.randint(1, 100)
        if sum(numbers) == asserted_sum:
            yield(trial, numbers)
            trial = 0


for i in range(10):
    print(next(random_with_sum(3, 100)))
    
# 3 split partition quicksort
# put your python code here
x = input().split()

def find_pivot(lst, start, end):
    if int(lst[start]) <= int(lst[(start + end) // 2]) <= int(lst[end]):
        return int(lst[(start + end) // 2])
    elif int(lst[(start + end) // 2]) <= int(lst[end]) <= int(lst[start]):
        return int(lst[end])
    return int(lst[start])
    

def partition(lst, start, end):
    aaa = []
    bbb = []
    ccc = []
    pivot = find_pivot(lst, start, end)
    small_right = start
    pivot_right = start
    for i in range(start, end + 1):
        x = int(lst[i])
        if  x < pivot:
            aaa.append(lst[i])
            small_right += 1
            pivot_right += 1
        elif x == pivot:
            bbb.append(lst[i])
            pivot_right += 1
        else:
            ccc.append(lst[i])
            
        
    print(small_right, pivot_right - 1)
    for el in aaa:
        print(el, end=" ")
    for el in bbb:
        print(el, end=" ")
    for el in ccc:
        print(el, end=" ")
    
partition(x, 0, len(x) - 1)

