from tkinter import *
from tkinter import ttk

def printString(*args):
    print(feet.get())
    charactersLength = len(feet.get())
    feet_entry.delete(first=0, last=charactersLength)

    

# Main window
root = Tk()
root.title("Example Widget")


frame = ttk.Frame(master=root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)

feet = StringVar()
feet_entry = ttk.Entry(master=frame, width=20, textvariable=feet)
feet_entry.grid(column=2,row=1, sticky=(W,E))

btn = ttk.Button(master=frame, text="print", command=printString).grid(column=3,row=1)


root.mainloop()