import tkinter as tk 
from PIL import Image, ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

mainWindow = tk.Tk()
mainWindow.title("Password Generator")
mainWindow.configure(background="white", padx=20, pady=20)

# canvas
mainCanvas = tk.Canvas(width=200,height=200, background="white")
mainCanvas.grid(column=0, row=1)
img = Image.open("GUI Builds/Password_ManagerTk/logo.png")
logo = ImageTk.PhotoImage(img)
mainCanvas.create_image(100,100, image=logo)
mainCanvas.grid(row=0, column=1)

# labels
ApplicationLabel = tk.Label(text="Website:",font=("Courier", 15, 'bold'), background="white").grid(row=1,column=0)
email_username_Label = tk.Label(text="Email/Username:",font=("Courier", 15, 'bold'), background="white").grid(row=2,column=0)
passwordLabel = tk.Label(text="Password:",font=("Courier", 15, 'bold'), background="white").grid(row=3,column=0)

# entry
ApplicationEntry = tk.Entry(width=50, border=5)
ApplicationEntry.grid(row=1, column=1, sticky=(tk.W))
email_username_Entry = tk.Entry(width=50, border=5)
email_username_Entry.grid(row=2, column=1, sticky=(tk.W))
passwordEntry = tk.Entry(width=21, border=5)
passwordEntry.grid(row=3, column=1, sticky=(tk.W), pady=0)

# buttons
generateButton = tk.Button(text="Generate Password", bg="white")
generateButton.grid(row=3,column=2,sticky=(tk.E))

addButton = tk.Button(text="Add", bg="white", width=50)
addButton.grid(row=4, column=1, sticky=(tk.W))

mainWindow.mainloop()