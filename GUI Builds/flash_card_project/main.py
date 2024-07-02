import tkinter as tk
from tkinter import PhotoImage
import pandas as pd



BACKGROUND_COLOR = "#B1DDC6"
MY_BACKGROUND_COLOR = "#86FEB8" 
current_word = 0

# read in the csv
dataframe = pd.read_csv("./data/Af_Eng_Top_100 - Sheet1.csv")

# functions



# a) Create the GUI

# 1) --> MainWindow
mainWindow = tk.Tk()
mainWindow.title("Super Flash")
mainWindow.configure(background=MY_BACKGROUND_COLOR, padx=50, pady=50)

# 2) --> Create the flash card
front_card_img = PhotoImage(file="./images/card_front.png")
frontCanvas = tk.Canvas(master=mainWindow, width=800, height=526, background=MY_BACKGROUND_COLOR, highlightthickness=0)
frontCanvas.create_image(400,263, image=front_card_img)
frontCanvas.grid(row=0,column=0, columnspan=2)
front_title_text = frontCanvas.create_text(400,150, text="Afrikaans", font=("Arial", 40, "italic"))
front_af_word = frontCanvas.create_text(400, 263, text=dataframe['Afrikkans'].values[0], font=("Arial", 60, 'bold'))



# 3) add the buttons
x_img = PhotoImage(file="./images/x.png")
wrongBtn = tk.Button(image=x_img, highlightthickness=0)
wrongBtn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/tick.png")
rightBtn = tk.Button(image=right_img, highlightthickness=0)
rightBtn.grid(row=1, column=1)












mainWindow.mainloop()