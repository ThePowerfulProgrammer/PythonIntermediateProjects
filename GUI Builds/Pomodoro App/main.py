from systemconstants import *
from PIL import Image, ImageTk
import tkinter as tk


# Step 1) UI Setup

mainWindow = tk.Tk()
mainWindow.title("Pomodoro Study")

# 640 * 426

canvas = tk.Canvas(width=640, height=426)
gradient_img_jpg = Image.open('GUI Builds/Pomodoro App/gradient.jpg')
gradient_img = ImageTk.PhotoImage(gradient_img_jpg) 

canvas.create_image(320,213, image=gradient_img)
canvas.pack()

mainWindow.mainloop()
