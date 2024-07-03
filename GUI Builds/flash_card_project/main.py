import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import time


BACKGROUND_COLOR = "#B1DDC6"
MY_BACKGROUND_COLOR = "#86FEB8" 
switch = 0
currentWord = 0

# read in the csv
dataframe = pd.read_csv("./data/Af_Eng_Top_100 - Sheet1.csv")

# functions
def switchCard():
    global switch
    global currentWord
    if (switch == 1):
        Canvas.itemconfig(current_img, image=front_card_img)
        Canvas.itemconfig(language_label, text="Afrikaans")
        Canvas.itemconfig(word_label, text=dataframe['Afrikkans'].values[currentWord])
        switch = 0
        mainWindow.after(1000, switchCard)
    else:
        Canvas.itemconfig(current_img, image=back_card_img)
        Canvas.itemconfig(language_label, text="English")
        Canvas.itemconfig(word_label, text=dataframe['English'].values[currentWord])
        switch = 1
        if (currentWord == 50):
            return "Game Complete"
        currentWord += 1
        mainWindow.after(1000, switchCard)

        

    

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
word_label = Canvas.create_text(400, 263, text=dataframe['Afrikkans'].values[currentWord], font=("Arial", 60, 'bold'))
Canvas.grid(row=0,column=0, columnspan=2)




# 3) add the buttons
x_img = PhotoImage(file="./images/x.png")
wrongBtn = tk.Button(image=x_img, highlightthickness=0)
wrongBtn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/tick.png")
rightBtn = tk.Button(image=right_img, highlightthickness=0)
rightBtn.grid(row=1, column=1)



mainWindow.after(1000, switchCard)


mainWindow.mainloop()