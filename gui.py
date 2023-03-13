import tkinter as tk
import csv

with open('airports.csv', newline='', encoding="utf-8") as csvfile:
    main_data = list(csv.reader(csvfile))

airports = []

for row in main_data:
    airports.append(row[0])

def cb_search(event):  
    search = search_str.get().upper()
    listbox.delete(0, tk.END)
    # If filter removed show all data
    if search == "":
        fill_listbox(airports) 
        return
  
    filtered_data = list()
    for item in airports:
        if item.find(search) >= 0:
            filtered_data.append(item)

    fill_listbox(filtered_data)   

def fill_listbox(ld):
    for item in ld:
        listbox.insert(tk.END, item)
  
def ok():
    pass

#second search box
def cb_search2(event):  
    search = search_str2.get().upper()
    listbox2.delete(0, tk.END)
    # If filter removed show all data
    if search == "":
        fill_listbox2(airports) 
        return
  
    filtered_data2 = list()
    for item in airports:
        if item.find(search) >= 0:
            filtered_data2.append(item)

    fill_listbox2(filtered_data2)   

def fill_listbox2(ld):
    for item in ld:
        listbox2.insert(tk.END, item)
  
def ok2():
    pass
    
# GUI
root = tk.Tk()
root.geometry("720x480")
root.resizable(False, False)

#search box 1
searchframe = tk.Frame(root, width=360, height=480, bg="grey")
searchframe.place(x=0, y=0)
searchframe.pack_propagate(False)

search_str = tk.StringVar()
search = tk.Entry(searchframe, textvariable=search_str, width=10)
search.place(y=5, x=5)

listbox = tk.Listbox(searchframe, width=10, height=25)
listbox.place(y=25, x=5)
fill_listbox(airports)

ok_btn = tk.Button(searchframe, text="OK", command=ok)
ok_btn.place(y=430, x=25)

search.bind('<KeyRelease>', cb_search)

#search box 2
search_str2 = tk.StringVar()
search2 = tk.Entry(searchframe, textvariable=search_str2, width=10)
search2.place(y=5, x=75)

listbox2 = tk.Listbox(searchframe, width=10, height=25)
listbox2.place(y=25, x=75)
fill_listbox2(airports)

ok_btn2 = tk.Button(searchframe, text="OK", command=ok2)
ok_btn2.place(y=430, x=90)

search2.bind('<KeyRelease>', cb_search2)
  
root.mainloop()
