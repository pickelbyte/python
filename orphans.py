import time, sys
try:
    import tkinter as tk
except ImportError:
    print("No tkinter")
    input()
    sys.exit()
import random

font = ("Arial", 16)
orphans = 0
numorphans = 0
def genorphans():
    orphans = random.randint(2,10)
    return orphans
def update():
    global orphans, orphanstxt, numorphans, numorphanstxt
    numorphans = genorphans()
    numorphanstxt["text"] = f"There are {numorphans} on the street. Run them over?"
def yes():
    global orphans, orphanstxt, numorphans
    orphans += numorphans
    orphanstxt["text"] = f"Orphans: {orphans}"
    update()
def no():
    orphanstxt["text"] = f"Orphans: {orphans}"
    update()

root = tk.Tk()
root.title("orphan killer")

yesopt = tk.Button(root, text="yes", command=yes, font=font)
noopt = tk.Button(root, text="no", command=no, font=font)
orphanstxt = tk.Label(root, text=f"Orphans: {orphans}", font=font)
numorphanstxt = tk.Label(root, text=f"There are {numorphans} on the street. Run them over?", font=font)
numorphanstxt.pack()
orphanstxt.pack()
yesopt.pack()
noopt.pack()

update()
