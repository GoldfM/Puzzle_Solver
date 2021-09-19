from tkinter import Tk, Label, Button, Entry



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





def solve_sudoku(bord, label_blocks):
    a,b = find_empty_cell(bord)
    if a == None or b == None:
        return True
    for value in range (1,10):
        if check(bord,a,b,value):
            bord[a][b] = value
            label_blocks[a][b].configure(text=value)
            if solve_sudoku(bord,label_blocks):
                return True
        bord[a][b] = 0

    return False




def translate(names_block, label_blocks):
    table=[
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
    for i,z in enumerate(names_block):
        num=z.get()
        if num!='':
            num=int(num)
            row=(i)//9+1
            col=(i)%9+1
            table[row-1][col-1]=num
            label_blocks[row-1][col-1].configure(text=num)
    solve_sudoku(table,label_blocks)



def window():
    window = Tk()
    window["bg"] = "#362b2b"
    window.geometry("850x470")
    window.title("Puzzle Solver")
    window.resizable(False, False)
    x=20
    y=-20
    entry_blocks=[]
    for i in range(1, 82):
        if (i - 1) % 3 == 0:
            x += 10
        if (i - 1) % 9 == 0:
            x = 20
            y += 40
        if (i - 1) % 27 == 0:
            y += 10
        obj = Entry(font=("Calibri", 20, "bold"), bg="white", fg="black", justify="center")
        obj.place(x=x, y=y, width=30, height=30)
        x += 40
        entry_blocks.append(obj)
    label_blocks=[]
    cur_list=[]
    y=-20
    for i in range(1,82):
        if (i-1)%3==0:
            x+=10
        if (i-1)%9==0:
            x=450
            y+=40
        if (i-1)%27==0:
            y+=10
        obj = Label(font=("Calibri", 20, "bold"), bg="white", fg="black", justify="center")
        obj.place(x=x,y=y,width=30,height=30)
        x+=40
        cur_list.append(obj)
        if len(cur_list)==9:
            label_blocks.append(cur_list)
            cur_list=[]

    btn=Button(text="РЕШИТЬ",font="Calibri 20 bold",bg="#362b2b",fg="#f67300",command=lambda:translate(entry_blocks, label_blocks))
    btn.place(width=140, height=40,x=135,y=420)
    line_1 = Label(bg='#f67300')
    line_1.place(x=139, y=18, width=3, height=394)
    line_2 = Label(bg='#f67300')
    line_2.place(x=269, y=18, width=3, height=394)
    line_3 = Label(bg='#f67300')
    line_3.place(x=13, y=147, width=385, height=3)
    line_4 = Label(bg='#f67300')
    line_4.place(x=13, y=277, width=385, height=3)

    _line_1 = Label(bg='#f67300')
    _line_1.place(x=139+430, y=18, width=3, height=394)
    _line_2 = Label(bg='#f67300')
    _line_2.place(x=269+430, y=18, width=3, height=394)
    _line_3 = Label(bg='#f67300')
    _line_3.place(x=13+430, y=147, width=385, height=3)
    _line_4 = Label(bg='#f67300')
    _line_4.place(x=13+430, y=277, width=385, height=3)


    window.mainloop()




window()
