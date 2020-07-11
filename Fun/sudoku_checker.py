

def check_sudoku(numbers):
    rows = numbers
    columns = []
    squares = []
    alle = [rows, columns, squares]

    for i in range(len(rows[0])):
        sth = ""
        for elem in rows:
            sth += elem[i]
        columns.append(sth)

    for i in range(0, 7, 3):
        for x in range(0, 7, 3):
            emp = ""
            emp += rows[i][x:x + 3] + rows[i + 1][x:x + 3] + rows[i + 2][x:x + 3]
            squares.append(emp)

    sudoku = True

    for elem in alle:
        for e in elem:
            cyf = '123456789'
            for c in e:
                if c in cyf:
                    cyf = cyf.replace(c, "")
            if len(cyf) != 0:
                sudoku = False

    if sudoku:
        print('\nThe given numbers create a proper sudoku!')
    else:
        print('\nNot a valid sudoku...')


nums = ['295743861', '431865927', '876192543', '387459216',
        '612387495', '549216738', '763524189', '928671354', '154938672']

check_sudoku(nums)
