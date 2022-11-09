from tkinter import *
import tkinter.messagebox as tkm
root = Tk()

turns = 0

# button1 function


def f1():
    global turns
    b1 = button1.cget("text")
    if b1 == "":
        turns = turns + 1
        if turns % 2 == 0:
            button1.configure(text="O")
            checking()
        elif turns % 2 == 1:
            button1.configure(text="X")
            checking()
        else:
            pass
    else:
        pass

# button2 function


def f2():
    global turns
    b2 = button2.cget("text")
    if b2 == "":
        turns = turns + 1
        print(turns)
        if turns % 2 == 0:
            button2.configure(text="O")
            checking()
        elif turns % 2 == 1:
            button2.configure(text="X")
            checking()
        else:
            pass
    else:
        pass

# button3 function


def f3():
    global turns
    b3 = button3.cget("text")
    if b3 == "":
        turns = turns + 1
        print(turns)
        if turns % 2 == 0:
            button3.configure(text="O")
            checking()
        elif turns % 2 == 1:
            button3.configure(text="X")
            checking()
        else:
            pass
    else:
        pass

# button4 function


def f4():
    global turns
    b4 = button4.cget("text")
    if b4 == "":
        turns = turns + 1
        print(turns)
        if turns % 2 == 0:
            button4.configure(text="O")
            checking()
        elif turns % 2 == 1:
            button4.configure(text="X")
            checking()
        else:
            pass
    else:
        pass

# button5 function


def f5():
    global turns
    b5 = button5.cget("text")
    if b5 == "":
        turns = turns + 1
        print(turns)
        if turns % 2 == 0:
            button5.configure(text="O")
            checking()
        elif turns % 2 == 1:
            button5.configure(text="X")
            checking()
        else:
            pass
    else:
        pass

# button6 function


def f6():
    global turns
    b6 = button6.cget("text")
    if b6 == "":
        turns = turns + 1
        print(turns)
        if turns % 2 == 0:
            button6.configure(text="O")
            checking()
        elif turns % 2 == 1:
            button6.configure(text="X")
            checking()
        else:
            pass
    else:
        pass

# button7 function


def f7():
    global turns
    b7 = button7.cget("text")
    if b7 == "":
        turns = turns + 1
        print(turns)
        if turns % 2 == 0:
            button7.configure(text="O")
            checking()
        elif turns % 2 == 1:
            button7.configure(text="X")
            checking()
        else:
            pass
    else:
        pass

# button8 function


def f8():
    global turns
    b8 = button8.cget("text")
    if b8 == "":
        turns = turns + 1
        print(turns)
        if turns % 2 == 0:
            button8.configure(text="O")
            checking()
        elif turns % 2 == 1:
            button8.configure(text="X")
            checking()
        else:
            pass
    else:
        pass

# button9 function


def f9():
    global turns
    b9 = button9.cget("text")
    if b9 == "":
        turns = turns + 1
        print(turns)
        if turns % 2 == 0:
            button9.configure(text="O")
            checking()
        elif turns % 2 == 1:
            button9.configure(text="X")
            checking()
        else:
            pass
    else:
        pass

# this displays when x wins


def xcondition():
    quest = tkm.askquestion("Title", "X won, do you want to play Again?")
    if quest == "yes":
        global turns
        turns = 0
        button1.configure(text="")
        button2.configure(text="")
        button3.configure(text="")
        button4.configure(text="")
        button5.configure(text="")
        button6.configure(text="")
        button7.configure(text="")
        button8.configure(text="")
        button9.configure(text="")
    else:
        frame.quit()

# This displays when o wins


def ocondition():
    quest = tkm.askquestion("Title", "O won, do you want to play Again?")
    if quest == "yes":
        global turns
        turns = 0
        button1.configure(text="")
        button2.configure(text="")
        button3.configure(text="")
        button4.configure(text="")
        button5.configure(text="")
        button6.configure(text="")
        button7.configure(text="")
        button8.configure(text="")
        button9.configure(text="")
    else:
        frame.quit()

# winning conditions


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
    if b1 == "X" and b2 == "X" and b3 == "X":
        xcondition()
    elif b4 == "X" and b5 == "X" and b6 == "X":
        xcondition()
    elif b7 == "X" and b8 == "X" and b9 == "X":
        xcondition()
    elif b1 == "X" and b4 == "X" and b7 == "X":
        xcondition()
    elif b2 == "X" and b5 == "X" and b8 == "X":
        xcondition()
    elif b3 == "X" and b6 == "X" and b9 == "X":
        xcondition()
    elif b1 == "X" and b5 == "X" and b9 == "X":
        xcondition()
    elif b3 == "X" and b5 == "X" and b7 == "X":
        xcondition()

    # O wins
    if b1 == "O" and b2 == "O" and b3 == "O":
        ocondition()
    elif b4 == "O" and b5 == "O" and b6 == "O":
        ocondition()
    elif b7 == "O" and b8 == "O" and b9 == "O":
        ocondition()
    elif b1 == "O" and b4 == "O" and b7 == "O":
        ocondition()
    elif b2 == "O" and b5 == "O" and b8 == "O":
        ocondition()
    elif b3 == "O" and b6 == "O" and b9 == "O":
        ocondition()
    elif b1 == "O" and b5 == "O" and b9 == "O":
        ocondition()
    elif b3 == "O" and b5 == "O" and b7 == "O":
        ocondition()

# UI


frame = Frame(root)
frame.grid(row=0, column=0)
button1 = Button(frame, text="", width=10, height=5, command=f1)
button1.grid(row=0, column=0)

button2 = Button(frame, text="", width=10, height=5, command=f2)
button2.grid(row=0, column=1)

button3 = Button(frame, text="", width=10, height=5, command=f3)
button3.grid(row=0, column=2)

button4 = Button(frame, text="", width=10, height=5, command=f4)
button4.grid(row=1, column=0)

button5 = Button(frame, text="", width=10, height=5, command=f5)
button5.grid(row=1, column=1)

button6 = Button(frame, text="", width=10, height=5, command=f6)
button6.grid(row=1, column=2)

button7 = Button(frame, text="", width=10, height=5, command=f7)
button7.grid(row=2, column=0)

button8 = Button(frame, text="", width=10, height=5, command=f8)
button8.grid(row=2, column=1)

button9 = Button(frame, text="", width=10, height=5, command=f9)
button9.grid(row=2, column=2)

root.mainloop()
