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
    if win == True:
        msg.showinfo(title="Game over", message=f"{out}'s win!")
        resetcmd()
    else:
        win = False


def update(self, txt="-"):
    global out, turnlbl, win
    if self["text"] == '-' and not checkwin():
        self["text"] = txt
        checkwin()
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

spaces = tk.Frame(root, width=300, height=300)
spaces.grid(column=1, row=1)

#----------------------------------#
a1 = tk.Label(spaces, text='-', font=lgfont)
a2 = tk.Label(spaces, text='-', font=lgfont)
a3 = tk.Label(spaces, text='-', font=lgfont)
a1.grid(row=0, column=0, sticky=tk.W, padx=20)
a2.grid(row=0, column=1, sticky=tk.W, padx=20)
a3.grid(row=0, column=2, sticky=tk.W, padx=20)
a1.bind("<Button-1>", lambda e:update(a1, out))
a2.bind("<Button-1>", lambda e:update(a2, out))
a3.bind("<Button-1>", lambda e:update(a3, out))
#----------------------------------#
b1 = tk.Label(spaces, text='-', font=lgfont)
b2 = tk.Label(spaces, text='-', font=lgfont)
b3 = tk.Label(spaces, text='-', font=lgfont)
b1.grid(row=1, column=0, sticky=tk.W, padx=20)
b2.grid(row=1, column=1, sticky=tk.W, padx=20)
b3.grid(row=1, column=2, sticky=tk.W, padx=20)
b1.bind("<Button-1>", lambda e:update(b1, out))
b2.bind("<Button-1>", lambda e:update(b2, out))
b3.bind("<Button-1>", lambda e:update(b3, out))
#----------------------------------#
c1 = tk.Label(spaces, text='-', font=lgfont)
c2 = tk.Label(spaces, text='-', font=lgfont)
c3 = tk.Label(spaces, text='-', font=lgfont)
c1.grid(row=2, column=0, sticky=tk.W, padx=20)
c2.grid(row=2, column=1, sticky=tk.W, padx=20)
c3.grid(row=2, column=2, sticky=tk.W, padx=20)
c1.bind("<Button-1>", lambda e:update(c1, out))
c2.bind("<Button-1>", lambda e:update(c2, out))
c3.bind("<Button-1>", lambda e:update(c3, out))
#----------------------------------#

reset = tk.Button(root, text="RESET", font=smfont, command=resetcmd)
reset.grid(row=6, column=0)

turnlbl = tk.Label(root, text=f"{out}'s Turn", font=medfont)
turnlbl.grid(row=6, column=2)

msg.showinfo(title="Startup", message="""
Click the spot to fill it in with the current turn""")

root.mainloop()
