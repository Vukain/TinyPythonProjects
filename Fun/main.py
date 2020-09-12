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
    pivot = find_pivot(lst, start, end)
    small_right = start
    pivot_right = start
    for i in range(start, end + 1):
        x = int(lst[i])
        if  x < pivot:
            lst.insert(small_right, lst.pop(i))
            small_right += 1
            pivot_right += 1
        elif x == pivot:
            lst.insert(pivot_right, lst.pop(i))
            pivot_right += 1
    return small_right, pivot_right - 1
    
a, b = partition(x, 0, len(x) - 1)

print(a, b)
for el in x:
    print(el, end=" ")
