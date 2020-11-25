gra = True
win = False
plx = True
ply = False

print("Welcome to the Tic Tac Toe!\nIt's a game for two players.\nOne player uses X, the other O.")
print("The goal is to get 3 X'es or 3 O'es in a line, before the opponent does.")
print("Players take turn and pick a zone in a 3x3 grid.")
print("Each zone is marked by a number.")
print("Wanna play?")

x = input("Yes/No\n").lower()
if x == 'no':
    gra = False
elif x == 'yes':
    pass
else:
    print("You're drunk, go home!")
    gra = False

print("Pick X or O Player One")
p1 = input().upper()
if p1 == 'X':
    p2 = 'O'
else:
    p2 = 'X'

listawyb = []
pola = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}


def plansza():
    print(' ')
    print('   |   |   ')
    print(f" {pola['1']} | {pola['2']} | {pola['3']} ")
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f" {pola['4']} | {pola['5']} | {pola['6']} ")
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f" {pola['7']} | {pola['8']} | {pola['9']} ")
    print('   |   |   ')
    print(' ')


def wincon():
    if pola['1'] == pola['2'] == pola['3'] or pola['4'] == pola['5'] == pola['6'] \
            or pola['7'] == pola['8'] == pola['9'] or pola['1'] == pola['4'] == pola['7'] \
            or pola['2'] == pola['5'] == pola['8'] or pola['3'] == pola['6'] == pola['9'] \
            or pola['1'] == pola['5'] == pola['9'] or pola['3'] == pola['5'] == pola['7']:
        return True
    else:
        return False


while gra:

    while plx:

        plansza()

        i = input('Pick a number Player One\n')
        if i.lower() == 'stop':
            gra = False
            plx = False
            break
        if i in listawyb:
            print('Number already picked!')
            continue

        listawyb.append(i)
        pola[i] = p1

        if wincon():
            win = True
            plx = False
        if win:
            plansza()
            print('Congratulations, Player One won!')
            gra = False
            break
        if len(listawyb) == 9:
            plansza()
            print('Game Over!\nNobody scored 3 signs in a line.')
            gra = False
            break

        plx = False
        ply = True

    while ply:

        plansza()

        i = input('Pick a number Player Two\n')
        if i.lower() == 'stop':
            gra = False
            ply = False
            break
        if i in listawyb:
            print('Number already picked!')
            continue

        listawyb.append(i)
        pola[i] = p2

        if wincon():
            win = True
        if win:
            plansza()
            print('Congratulations, Player Two won!')
            gra = False
            break
        if len(listawyb) == 9:
            plansza()
            print('Game Over!\nNobody scored 3 signs in a line.')
            gra = False
            break

        ply = False
        plx = True

print("Bye, bye!")