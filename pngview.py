#!/usr/bin/python
import sys
import tkinter as tk

def key():
    print("Key pressed")

root = tk.Tk()
root.title("")
root.bind('<Key-space>', lambda e: quit())

if len(sys.argv) == 2:
    print("Opening ",sys.argv[1])
    root.title(sys.argv[1])
    img = tk.PhotoImage(file=sys.argv[1])
    panel = tk.Label(root, image=img)
    panel.pack()
    root.mainloop()

else:
    print("Usage: ",sys.argv[0]," file.png ")



    
