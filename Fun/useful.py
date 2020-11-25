# PRIMES

prime_numbers = [num for num in range(
    2, 1000) if all(num % n for n in range(2, num))]
# print(prime_numbers)

prims = []

for num in range(2, 1000):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        prims.append(num)
# print(prims)

# LEAP YEAR

x = int(input('gimme a year: '))

# prosto i szybko
if x % 4 == 0 and x % 100 != 0:
    print('yea')
elif x % 400 == 0:
    print('yea')
else:
    print('nope')
# odtworzenie struktury skryptu
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print('yea')
        else:
            print('nope')
    else:
        print('yea')
else:
    print('nope')
# jednolinijkowiec
print("yea" if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0) else "nope")

# MANUAL SORTING

liszt = [7, 1, 3, 6, 2, 4, 5]

sorting = True
while sorting:
    sorting = False
    for idx, num in enumerate(liszt[:-1]):
        if liszt[idx] > liszt[idx+1]:
            sorting = True
            ns = liszt.pop(idx)
            liszt.append(ns)
            break
    else:
        print(liszt)

# STRING TO DICT

txt = 'lorem,ipsum,dolor,sit,amet'
txt_list = txt.split(',')
txt_list2 = txt_list.copy()
txt_list.append('')

x = txt.count(',')
y = '{"'+txt.replace(',', '":{"')+'":""}' + x * '}'
# print(y)
z = eval(y)
print(z)


def dicter(lister):
    x = {}
    if len(lister) == 2:
        x[lister[0]] = lister[1]
    else:
        x[lister[0]] = dicter(lister[1:])
    return x


def dicter2(lister):
    x = {}
    x[lister[0]] = lister[1] if len(lister) == 2 else dicter2(lister[1:])
    #x[lister[0]] = "" if len(lister) == 1 else dicter2(lister[1:])
    return x


def dicter3(lister):
    x = {}
    if len(lister) == 1:
        x[lister[0]] = ''
    else:
        x[lister[0]] = dicter3(lister[1:])
    return x

# WORD INVERSE IN SENTENCE


stg = "un dos tres"

lis2 = []
for word in stg.split():
    word2 = ""
    idx = 0
    for letter in word:
        idx -= 1
        word2 += word[idx]
    lis2.append(word2.capitalize())
print(" ".join(lis2))

lis3 = [word[::-1].capitalize() for word in stg.split()]
print(" ".join(lis3))
