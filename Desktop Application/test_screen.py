from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, padding=400)
frame.grid()
ttk.Label(frame, text="Testing").grid(column=0, row=0)
ttk.Button(frame, text="Exit", command=root.destroy).grid(column=0, row=20)
root.mainloop()
