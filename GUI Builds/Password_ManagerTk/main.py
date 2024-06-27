import tkinter as tk 
from PIL import Image, ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

mainWindow = tk.Tk()
mainWindow.title("Password Generator")
mainWindow.configure(width=800, height=500, background="white")


mainCanvas = tk.Canvas(width=800,height=500, background="white")
img = Image.open("GUI Builds/Password_ManagerTk/logo.png")
logo = ImageTk.PhotoImage(img)
mainCanvas.create_image(400,200, image=logo)

mainCanvas.create_text(425,250,text="Text",font=("Oswald", 20, 'bold'))

mainCanvas.pack()
mainWindow.mainloop()