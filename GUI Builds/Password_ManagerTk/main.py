import tkinter as tk 
from tkinter import PhotoImage, messagebox 
from PyGeneratePassword import PasswordGenerate
import pyperclip
import json

def save():
    
    if (ApplicationEntry.get() == '' or userEntry.get() == '' or passwordEntry == ''):
        messagebox.showinfo(title="Correct Errors", message="Ensure all fields are complete")
    else:       
        is_okay = messagebox.askokcancel(title="Confirm Details", message=f"Are you okay with: \n {ApplicationEntry.get()} \n {userEntry.get()} \n"
                               f"{passwordEntry.get()}")
        
        if (is_okay):    
            pyperclip.copy(passwordEntry.get())
            new_data = {
                ApplicationEntry.get(): {
                    'email': userEntry.get(),
                    'password': passwordEntry.get()
                }
            }
            
            # Open file and write
            with open("./data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
            
            with open('./data.json', 'w') as file:
                json.dump(data, file, indent=4)
        
        ApplicationEntry.delete(0,tk.END)
        
        passwordEntry.delete(0,tk.END)
        
    return ""

def generatePassword():
    password = PasswordGenerate()
    pyperclip.copy(password)
    passwordEntry.delete(0,tk.END)
    passwordEntry.insert(0,password)
    
    


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
ApplicationEntry.focus()

userEntry = tk.Entry(width=52, border=2)
userEntry.grid(row=2, column=1, columnspan=2)
userEntry.insert(0, "ashishr0301@gmail.com")

passwordEntry = tk.Entry(width=33, border=2)
passwordEntry.grid(row=3, column=1)

# buttons
generateButton = tk.Button(text="Generate Password", bg="white", command=generatePassword)
generateButton.grid(row=3,column=2)

addButton = tk.Button(text="Add", bg="white", width=44, pady=3, padx=3, command=save)
addButton.grid(row=4, column=1, columnspan=2)

mainWindow.mainloop()