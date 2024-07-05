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
switch_timer = None

# Read in the dataframe
try:
    dataframe = pd.read_csv("./data/Af_Eng_Top_100 - Sheet1.csv")
except FileNotFoundError:
    print("File not found, check current directory of operation")

# Commands
def switchCard():
    global switch, sample, currentWord, switch_timer
    if switch == 1:
        Canvas.itemconfig(current_img, image=front_card_img)
        Canvas.itemconfig(language_label, text="Afrikaans", fill="black")
        Canvas.itemconfig(word_label, text=sample[0], fill="black")
        switch = 0
        switch_timer = mainWindow.after(3000, switchCard)
    else:
        Canvas.itemconfig(current_img, image=back_card_img)
        Canvas.itemconfig(language_label, text="English", fill="white")
        Canvas.itemconfig(word_label, text=sample[1], fill="white")
        switch = 1
        if currentWord == 101:
            mainWindow.destroy()
            return "Game Complete"
        currentWord += 1
        switch_timer = mainWindow.after(3000, switchCard)

def randomWord():
    global sample, switch_timer
    if switch_timer is not None:
        mainWindow.after_cancel(switch_timer)
    sample = dataframe.sample(n=1).values[0]
    print(sample)
    Canvas.itemconfig(current_img, image=front_card_img)
    Canvas.itemconfig(language_label, text="Afrikaans", fill="black")
    Canvas.itemconfig(word_label, text=sample[0], fill="black")
    switch_timer = mainWindow.after(3000, switchCard)

# Create the GUI

# MainWindow
mainWindow = tk.Tk()
mainWindow.title("Super Flash")
mainWindow.configure(background=MY_BACKGROUND_COLOR, padx=50, pady=50)

# Create the flash card
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")

Canvas = tk.Canvas(master=mainWindow, width=800, height=526, background=MY_BACKGROUND_COLOR, highlightthickness=0)
current_img = Canvas.create_image(400, 263, image=front_card_img)
language_label = Canvas.create_text(400, 150, text="Afrikaans", font=("Arial", 40, "italic"))
word_label = Canvas.create_text(400, 263, text="Word", font=("Arial", 60, 'bold'))
Canvas.grid(row=0, column=0, columnspan=2)

# Add the buttons
x_img = PhotoImage(file="./images/x.png")
wrongBtn = tk.Button(image=x_img, highlightthickness=0, command=randomWord)
wrongBtn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/tick.png")
rightBtn = tk.Button(image=right_img, highlightthickness=0, command=randomWord)
rightBtn.grid(row=1, column=1)

randomWord()
switch_timer = mainWindow.after(3000, switchCard)

mainWindow.mainloop()
