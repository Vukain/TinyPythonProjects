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