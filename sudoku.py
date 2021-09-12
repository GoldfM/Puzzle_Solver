from pprint import pprint


def find_empty_cell(bord):
    for a in range(9):
        for b in range(9):
            if bord[a][b]==0:
                return a,b
    return None, None


def check(bord,row,col,value):
    for c in bord[row]:
        if c==value:
            return False
    for r in range(9):
        if bord[r][col]==value:
            return False
    square_x=(row//3)*3
    square_y =(col//3)*3
    for a in range(square_x,square_x+3):
        for b in range(square_y, square_y + 3):
            if bord[a][b]==value:
                return False
    return True



def solve_sudoku(bord):

    a,b = find_empty_cell(bord)
    if a == None or b == None:
        return True

    for value in range (1,10):
        if check(bord,a,b,value):
            bord[a][b] = value

            if solve_sudoku(bord):
                return True
        bord[a][b] = 0

    return False

def main():
    table_1 = [
        [8, 0, 0, 0, 0, 5, 0, 2, 9],
        [2, 0, 6, 0, 0, 1, 3, 0, 4],
        [0, 4, 0, 7, 0, 0, 1, 0, 8],

        [0, 0, 0, 0, 0, 0, 8, 0, 5],
        [9, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 9, 1],

        [0, 0, 0, 1, 0, 2, 4, 0, 0],
        [0, 0, 4, 0, 3, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 6]
    ]

    table_clear=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    table_2=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 9, 0, 5, 0],
        [0, 0, 9, 8, 2, 0, 0, 1, 3],

        [1, 0, 7, 0, 9, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 4, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],

        [0, 2, 0, 0, 7, 4, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 6, 0, 1, 0, 5, 4, 0, 0],
    ]
    print(solve_sudoku(table_2))
    pprint(table_2)



main()
