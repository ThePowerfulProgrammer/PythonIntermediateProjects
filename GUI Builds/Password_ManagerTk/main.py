import tkinter as tk 
from tkinter import PhotoImage

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Read from entry widgets and write to a file called data.txt
# EG: App | email | password

def printData(**dict):
    
    if (ApplicationEntry.get() == '' or userEntry.get() == '' or passwordEntry == ''):
        pass
        print("Please fill in all values \n")
    else:
        print(ApplicationEntry.get())
        print(userEntry.get())
        print(passwordEntry.get(), "\n")
        # Open file and write
        with open("./data.txt", "a") as file:
            file.write(f"{ApplicationEntry.get()} | {userEntry.get()} | {passwordEntry.get()} ")
    
        ApplicationEntry.delete(0,tk.END)
        
        passwordEntry.delete(0,tk.END)
        
    return ""
    


# ---------------------------- UI SETUP ------------------------------- #

mainWindow = tk.Tk()
mainWindow.title("Password Generator")
mainWindow.configure(background="white", padx=50, pady=50)

# canvas
logo_img = PhotoImage(file="./logo.png")
mainCanvas = tk.Canvas(master=mainWindow,width=200,height=200, background="white", borderwidth=0, highlightthickness=0)
mainCanvas.create_image(100,100, image=logo_img)
mainCanvas.grid(row=0, column=1)

# labels
ApplicationLabel = tk.Label(text="Website:", background="white", font=("Courier", 15)).grid(row=1,column=0)
userLabel = tk.Label(text="Email/Username:", background="white", font=("Courier", 15)).grid(row=2,column=0)
passwordLabel = tk.Label(text="Password:", background="white", font=("Courier", 15)).grid(row=3,column=0)

# entry
ApplicationEntry = tk.Entry(width=52, border=2)
ApplicationEntry.grid(row=1, column=1, columnspan=2)

userEntry = tk.Entry(width=52, border=2)
userEntry.grid(row=2, column=1, columnspan=2)
userEntry.insert(0, "ashishr0301@gmail.com")

passwordEntry = tk.Entry(width=33, border=2)
passwordEntry.grid(row=3, column=1)

# buttons
generateButton = tk.Button(text="Generate Password", bg="white")
generateButton.grid(row=3,column=2)

addButton = tk.Button(text="Add", bg="white", width=44, pady=3, padx=3, command=printData)
addButton.grid(row=4, column=1, columnspan=2)

mainWindow.mainloop()