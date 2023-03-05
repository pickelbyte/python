import webview
import tkinter as tk

def create_webview(url, title, self):
    webview.create_window(title=title, url=url)
    webview.start()
    self.destroy()

root = tk.Tk()
root.title("Choose Page")

l = tk.Label(root, text="Always put 'https://' in front of url")
l.pack()

e = tk.Entry(root)
e.insert(0, "https://")
e.pack()

c = tk.Button(root, text="OK", command=lambda: create_webview(e.get(), "Webpage", root))
c.pack()

root.mainloop()
