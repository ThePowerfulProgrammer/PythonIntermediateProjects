import pandas as pd
from tkinter import PhotoImage
import tkinter as tk


BACKGROUND_COLOR = "#B1DDC6"
MY_BACKGROUND_COLOR = "#86FEB8" 
switch = 0
currentWord = 0
correctGuesses = {}
incorrectGuesses = {}
right = 0
wrong = 0
sample = None

# Read in the dataframe
try:
    dataframe = pd.read_csv("./data/Af_Eng_Top_100 - Sheet1.csv")
except FileNotFoundError:
    print("File not found, check current directory of operation")


 # commands
 
def switchCard():
    global switch
    global sample 
    global currentWord
    if (switch == 1):
        Canvas.itemconfig(current_img, image=front_card_img)
        Canvas.itemconfig(language_label, text="Afrikaans")
        Canvas.itemconfig(word_label, text=sample[0])
        switch = 0
        mainWindow.after(3000, switchCard)
    else:
        Canvas.itemconfig(current_img, image=back_card_img)
        Canvas.itemconfig(language_label, text="English")
        Canvas.itemconfig(word_label, text=sample[1])
        switch = 1
        if (currentWord == 6):
            mainWindow.destroy()
            return "Game Complete"
        currentWord += 1
        mainWindow.after(3000, switchCard)
        
    pass

def randomWord():
    global sample
    sample = dataframe.sample(n=1).values[0]
    print(sample)
    word = sample[0]    
    Canvas.itemconfigure(word_label,text=word)



# a) Create the GUI

# 1) --> MainWindow
mainWindow = tk.Tk()
mainWindow.title("Super Flash")
mainWindow.configure(background=MY_BACKGROUND_COLOR, padx=50, pady=50)

# 2) --> Create the flash card
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")

Canvas = tk.Canvas(master=mainWindow, width=800, height=526, background=MY_BACKGROUND_COLOR, highlightthickness=0)
current_img = Canvas.create_image(400,263, image=front_card_img)
language_label = Canvas.create_text(400,150, text="Afrikaans", font=("Arial", 40, "italic"))
word_label = Canvas.create_text(400, 263, text="Word", font=("Arial", 60, 'bold'))
Canvas.grid(row=0,column=0, columnspan=2)




# 3) add the buttons
x_img = PhotoImage(file="./images/x.png")
wrongBtn = tk.Button(image=x_img, highlightthickness=0, command=randomWord)
wrongBtn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/tick.png")
rightBtn = tk.Button(image=right_img, highlightthickness=0, command=randomWord)
rightBtn.grid(row=1, column=1)



mainWindow.after(4000, switchCard)


mainWindow.mainloop()