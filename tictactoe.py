import tkinter as tk
from tkinter import messagebox as msg

lgfont = ("Arial", 36)
medfont = ("Arial", 18)
smfont = ("Arial", 12)
out = 'X'
win = False

def checkwin():
    global win, out
    if a1["text"] == out and a2["text"] == out and a3["text"] == out:
        win = True
    elif a1["text"] == out and b2["text"] == out and c3["text"] == out:
        win = True
    elif a1["text"] == out and b1["text"] == out and c1["text"] == out:
        win = True
    elif b1["text"] == out and b2["text"] == out and b3["text"] == out:
        win = True
    elif c2["text"] == out and b2["text"] == out and a2["text"] == out:
        win = True
    elif c1["text"] == out and c2["text"] == out and c3["text"] == out:
        win = True
    elif c1["text"] == out and b2["text"] == out and a3["text"] == out:
        win = True
    elif c3["text"] == out and b3["text"] == out and a3["text"] == out:
        win = True
    else:
        win = False

    if win:
        msg.showinfo(title="Game Over", message=f"{out}'s have won!")
        resetcmd()

def update(self, txt="-"):
    global out, turnlbl, win
    if self["text"] == '-':
        self["text"] = txt
        if out == 'X':
            out = 'O'
        else:
            out = 'X'
        turnlbl["text"] = f"{out}'s Turn"
    else:
        self["text"] = self["text"]

def clear(self):
    self["text"] = '-'
    

def resetcmd():
    global out, turnlbl
    turnlbl["text"] = "X's Turn"
    clear(a1)
    clear(a2)
    clear(a3)
    clear(b1)
    clear(b2)
    clear(b3)
    clear(c1)
    clear(c2)
    clear(c3)

root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

msg.showinfo(title="Startup", message="""
Press space when you think you won! 
Press the corresponding button to fill that grid spot with the current turn.""")

#----------------------------------#
a1 = tk.Label(root, text='-', font=lgfont)
a2 = tk.Label(root, text='-', font=lgfont)
a3 = tk.Label(root, text='-', font=lgfont)
a1.grid(row=0, column=0, sticky=tk.W, padx=10)
a2.grid(row=0, column=1, sticky=tk.W, padx=10)
a3.grid(row=0, column=2, sticky=tk.W, padx=10)
#----------------------------------#
b1 = tk.Label(root, text='-', font=lgfont)
b2 = tk.Label(root, text='-', font=lgfont)
b3 = tk.Label(root, text='-', font=lgfont)
b1.grid(row=1, column=0, sticky=tk.W, padx=10)
b2.grid(row=1, column=1, sticky=tk.W, padx=10)
b3.grid(row=1, column=2, sticky=tk.W, padx=10)
#----------------------------------#
c1 = tk.Label(root, text='-', font=lgfont)
c2 = tk.Label(root, text='-', font=lgfont)
c3 = tk.Label(root, text='-', font=lgfont)
c1.grid(row=2, column=0, sticky=tk.W, padx=10)
c2.grid(row=2, column=1, sticky=tk.W, padx=10)
c3.grid(row=2, column=2, sticky=tk.W, padx=10)
#----------------------------------#

#----------------------------------#
at1 = tk.Button(root, text='a1', font=lgfont, command=lambda: update(a1, out))
at2 = tk.Button(root, text='a2', font=lgfont, command=lambda: update(a2, out))
at3 = tk.Button(root, text='a3', font=lgfont, command=lambda: update(a3, out))
at1.grid(row=3, column=0, sticky=tk.W, padx=10)
at2.grid(row=3, column=1, sticky=tk.W, padx=10)
at3.grid(row=3, column=2, sticky=tk.W, padx=10)
#----------------------------------#
bt1 = tk.Button(root, text='b1', font=lgfont, command=lambda: update(b1, out))
bt2 = tk.Button(root, text='b2', font=lgfont, command=lambda: update(b2, out))
bt3 = tk.Button(root, text='b3', font=lgfont, command=lambda: update(b3, out))
bt1.grid(row=4, column=0, sticky=tk.W, padx=10)
bt2.grid(row=4, column=1, sticky=tk.W, padx=10)
bt3.grid(row=4, column=2, sticky=tk.W, padx=10)
#----------------------------------#
ct1 = tk.Button(root, text='c1', font=lgfont, command=lambda: update(c1, out))
ct2 = tk.Button(root, text='c2', font=lgfont, command=lambda: update(c2, out))
ct3 = tk.Button(root, text='c3', font=lgfont, command=lambda: update(c3, out))
ct1.grid(row=5, column=0, sticky=tk.W, padx=10)
ct2.grid(row=5, column=1, sticky=tk.W, padx=10)
ct3.grid(row=5, column=2, sticky=tk.W, padx=10)
#----------------------------------#

reset = tk.Button(root, text="RESET", font=medfont, command=resetcmd)
reset.grid(row=6, column=0)

turnlbl = tk.Label(root, text=f"{out}'s Turn", font=medfont)
turnlbl.grid(row=6, column=2)

root.mainloop()
