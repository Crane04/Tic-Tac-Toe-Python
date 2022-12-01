from tkinter import *
import tkinter.messagebox as tkm
import random
root = Tk()

game_array = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def init():
    cplays = random.choice(game_array)
    print(cplays)

    if buttons[cplays].cget("text") == "":
        if cplays == 0:
            button1.configure(text="O")
        elif cplays == 1:
            button2.configure(text="O")
        elif cplays == 2:
            button3.configure(text="O")
        elif cplays == 3:
            button4.configure(text="O")
        elif cplays == 4:
            button5.configure(text="O")
        elif cplays == 5:
            button6.configure(text="O")
        elif cplays == 6:
            button7.configure(text="O")
        elif cplays == 7:
            button8.configure(text="O")
        elif cplays == 8:
            button9.configure(text="O")
        checking()
    elif buttons[cplays].cget("text") == "X" or "O":
        init()
    else:
        pass
    print(game_array)


def player(x):
    if buttons[x].cget("text") == "X" or "O":
        pass
    if buttons[x].cget("text") == "":
        buttons[x].configure(text="X")
        checking()
        init()


frame = Frame(root)
frame.grid(row=5, column=5)
button1 = Button(frame, text="", width=10, height=5, command=lambda: player(0))
button1.grid(row=0, column=0)
button2 = Button(frame, text="", width=10, height=5, command=lambda: player(1))
button2.grid(row=0, column=1)
button3 = Button(frame, text="", width=10, height=5, command=lambda: player(2))
button3.grid(row=0, column=2)
button4 = Button(frame, text="", width=10, height=5, command=lambda: player(3))
button4.grid(row=1, column=0)
button5 = Button(frame, text="", width=10, height=5, command=lambda: player(4))
button5.grid(row=1, column=1)
button6 = Button(frame, text="", width=10, height=5, command=lambda: player(5))
button6.grid(row=1, column=2)
button7 = Button(frame, text="", width=10, height=5, command=lambda: player(6))
button7.grid(row=2, column=0)
button8 = Button(frame, text="", width=10, height=5, command=lambda: player(7))
button8.grid(row=2, column=1)
button9 = Button(frame, text="", width=10, height=5, command=lambda: player(8))
button9.grid(row=2, column=2)
buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

def checking():
    global turns
    b1 = button1.cget("text")
    b2 = button2.cget("text")
    b3 = button3.cget("text")
    b4 = button4.cget("text")
    b5 = button5.cget("text")
    b6 = button6.cget("text")
    b7 = button7.cget("text")
    b8 = button8.cget("text")
    b9 = button9.cget("text")
    # X wins
    if (b1 == "X" and b2 == "X" and b3 == "X") or (b4 == "X" and b5 == "X" and b6 == "X") or \
            (b7 == "X" and b8 == "X" and b9 == "X") or (b1 == "X" and b4 == "X" and b7 == "X") or \
            (b2 == "X" and b5 == "X" and b8 == "X") or (b3 == "X" and b6 == "X" and b9 == "X") or \
            (b1 == "X" and b5 == "X" and b9 == "X") or (b3 == "X" and b5 == "X" and b7 == "X"):
        print("You Won")
        tkm.showinfo("You Won")
        frame.quit()
    if (b1 == "O" and b2 == "O" and b3 == "O") or (b4 == "O" and b5 == "O" and b6 == "O") or \
            (b7 == "O" and b8 == "O" and b9 == "O") or (b1 == "O" and b4 == "O" and b7 == "O") or \
            (b2 == "O" and b5 == "O" and b8 == "O") or (b3 == "O" and b6 == "O" and b9 == "O") or \
            (b1 == "O" and b5 == "O" and b9 == "O") or (b3 == "O" and b5 == "O" and b7 == "O"):
        print("Computer Won")
        tkm.showinfo("You Lost!")
        frame.quit()

init()
root.mainloop()
