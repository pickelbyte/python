import tkinter as tk
import csv

with open('airports.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

codes = []
for airport in data:
    codes.append(airport[0])

names = []
for airport in data:
    names.append(airport[1])

countries = []
for airport in data:
    countries.append(airport[2])

def update(data):
    results.delete(0, tk.END)
    for item in data:
        results.insert(tk.END, item)

def fillout(e):
    searchbar.delete(0, tk.END)
    searchbar.insert(0, results.get(tk.ANCHOR))

def check(e):
    typed = searchbar.get()

    if typed == '':
        data = data
    else:
	data = []
        for item in data:
	    if typed.lower() in item.lower():
		data.append(item)
    update(data)

root = tk.Tk()
root.title("Airport distance calculator")

searchlbl = tk.Label(root, text="Search for an airport")
searchlbl.pack(pady=20)

searchbar = tk.Entry(root)
searchbar.pack(pady=20)

results = tk.Listbox(root, width=30)
results.pack(pady=5)

results.bind("<<ListboxSelect>>", fillout)
searchbar.bind("<KeyRelease>", check)

update(data)

root.mainloop()

