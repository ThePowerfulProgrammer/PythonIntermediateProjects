# Imports 
from tkinter import *
from tkinter import ttk

# The backbone 
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


# Main App window
root = Tk()
root.title("Conversion ft - m ")

# Create a content frame
'''
Frame widget, which will hold contents of our UI
'''
mainFrame = ttk.Frame(master=root,padding="3 3 12 12")
mainFrame.grid(column=0,row=0,sticky=(N, W, E, S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)

# Create the first widget

feet = StringVar()
feet_entry = ttk.Entry(master=mainFrame, width=7,textvariable=feet)
feet_entry.grid(column=2, row=1,sticky=(W,E))

# The remaining widgets
meters = StringVar()
ttk.Label(master=mainFrame, textvariable=meters).grid(column=2, row=2, sticky=W)

ttk.Button(master=mainFrame,text="calculate", command=calculate).grid(column=3, row=3,sticky=W)

ttk.Label(master=mainFrame, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(master=mainFrame, text='is equivalent to').grid(column=1, row=2, sticky=E)
ttk.Label(master=mainFrame,text='meters').grid(column=3, row=2, sticky=W)


# Access mainFrame methods
for child in mainFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)


root.mainloop()