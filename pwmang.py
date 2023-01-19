import tkinter as tk
from tkinter import filedialog
import csv
import os

main_folder = os.path.expanduser("~")+"/Documents/"

Lfont=("Arial", 20)
Mfont=("Arial", 16)
Sfont=("Arial", 12)

root = tk.Tk()
root.geometry("720x480")
root.title("PWMang")
root.configure(bg="#707070")
root.resizable(False, False)

def invalid_popup():
    popup = tk.Toplevel(win)
    top.geometry("200x100")
    top.title("Warning")
    Label(top, text= """Invalid File!
                        CSV required""", font=Mfont).place(x=150,y=80)

def browse_files():
    filename = filedialog.askopenfilename(initialdir = main_folder, title = "Select a File", filetypes = (("CSV files", "*.csv*"),("all files","*.*")))
    root.title(f"PWMang - {filename}")
    with open(filename, newline='') as csvfile:
        contents = list(csv.reader(csvfile, delimiter=","))
    return contents
    

pwlist = tk.Frame(root, width=480, height=460, bg="#b5b5b5")
pwlist.place(x=230, y=10)
sidebar = tk.Frame(root, width=200, height=460, bg="#b5b5b5")
sidebar.place(x=10, y=10)
sidebar.pack_propagate(False)
pwlist.pack_propagate(False)

selectfilebtn = tk.Button(sidebar, text="Import Passwords", font=Mfont, command=browse_files)
selectfilebtn.place(x=2, y=2)


root.mainloop()
