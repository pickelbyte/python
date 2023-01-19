import tkinter as tk
from tkinter import filedialog
import csv
import os

main_folder = os.path.expanduser("~")+"/Documents/"

Lfont=("Arial", 20)
Mfont=("Arial", 16)
Sfont=("Arial", 12)
contents = []

root = tk.Tk()
root.geometry("720x480")
root.title("PWMang")
root.configure(bg="#707070")
root.resizable(False, False)

def invalid_popup():
    popup = tk.Toplevel(root)
    popup.geometry("200x50")
    popup.title("Warning")
    tk.Label(popup, text= """Invalid File! CSV required""", font=Sfont).place(x=2, y=2)

def browse_files():
    global contents
    filename = filedialog.askopenfilename(initialdir = main_folder, title = "Select a File", filetypes = (("CSV files", "*.csv*"),("all files","*.*")))
    split = os.path.splitext(filename)
    ext = split[1]
    if ext != '.csv':
        invalid_popup()
    
    root.title(f"PWMang - {filename}")
    with open(filename, newline='') as csvfile:
        contents = list(csv.reader(csvfile, delimiter=","))

def make_pw_list():
    global contents
    # WIP

pwlist = tk.Frame(root, width=480, height=460, bg="#b5b5b5")
pwlist.place(x=230, y=10)
sidebar = tk.Frame(root, width=200, height=460, bg="#b5b5b5")
sidebar.place(x=10, y=10)
sidebar.pack_propagate(False)
pwlist.pack_propagate(False)

selectfilebtn = tk.Button(sidebar, text="Import Passwords", font=Mfont, command=browse_files)
selectfilebtn.place(x=2, y=2)

root.mainloop()
