import math


def copydict(dict):
    ndict = {}
    for k, v in dict.items():
        ndict[k] = v
    print(ndict)


def addict(dict1, dict2):
    ndict = {}
    for k, v in dict1.items():
        ndict[k] = v
    for k, v in dict2.items():
        ndict[k] = v
    print(ndict)

# addict({'a':1, 'b':2}, {'b':3, 'c':4, 'd':5})

def primer(y):
    if y <= 1:
        print(y, "nie moze byc liczba ujemna i mniejsza od 1")
    else:
        x = y // 2
        while x > 1:
            if y % x == 0:
                print(y, 'dzieli sie prez', x)
                break
            x -= 1
        else:
            print(y, 'jest liczba pierwsza')


pot = [2, 4, 9, 16, 25]

pot1 = []
for num in pot:
    pot1.append(math.sqrt(num))

pot2 = list(map(math.sqrt, pot))

pot3 = [math.sqrt(num) for num in pot]

#print(pot1, pot2, pot3, sep="\n")
