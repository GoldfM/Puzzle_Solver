from pprint import pprint
from tkinter import Tk, Label, Button, PhotoImage, ttk, messagebox, Entry, END, Frame



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

def window():
    # block_1.place(x=18,y=31,width=25,height=25)
    window = Tk()
    window["bg"] = "#362b2b"
    window.geometry("750x400")
    window.title("Puzzle Solver")
    window.resizable(False, False)
    x=18
    y=-10
    for i in range(1,82):
        if (i-1)%3==0:
            x+=9
        if (i-1)%9==0:
            x=18
            y+=37
        if (i-1)%27==0:
            y+=9
        obj = Entry(font=("Calibri", 17, "bold"), bg="white", fg="black", justify="center")
        obj.place(x=x,y=y,width=27,height=27)
        x+=37

    window.mainloop()




window()
