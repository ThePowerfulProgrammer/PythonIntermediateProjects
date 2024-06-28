import tkinter as tk 
from tkinter import PhotoImage

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

mainWindow = tk.Tk()
mainWindow.title("Password Generator")
mainWindow.configure(background="white", padx=50, pady=50)

# canvas
logo_img = PhotoImage(file="GUI Builds/Password_ManagerTk/logo.png")
mainCanvas = tk.Canvas(master=mainWindow,width=200,height=200, background="white", borderwidth=0, highlightthickness=0)
mainCanvas.create_image(100,100, image=logo_img)
mainCanvas.grid(row=0, column=1)

# labels
ApplicationLabel = tk.Label(text="Website:", background="white", font=("Courier", 15)).grid(row=1,column=0)
email_username_Label = tk.Label(text="Email/Username:", background="white", font=("Courier", 15)).grid(row=2,column=0)
passwordLabel = tk.Label(text="Password:", background="white", font=("Courier", 15)).grid(row=3,column=0)

# entry
ApplicationEntry = tk.Entry(width=52, border=2)
ApplicationEntry.grid(row=1, column=1, columnspan=2)

email_username_Entry = tk.Entry(width=52, border=2)
email_username_Entry.grid(row=2, column=1, columnspan=2)

passwordEntry = tk.Entry(width=33, border=2)
passwordEntry.grid(row=3, column=1)

# buttons
generateButton = tk.Button(text="Generate Password", bg="white")
generateButton.grid(row=3,column=2)

addButton = tk.Button(text="Add", bg="white", width=44)
addButton.grid(row=4, column=1, columnspan=2)

mainWindow.mainloop()