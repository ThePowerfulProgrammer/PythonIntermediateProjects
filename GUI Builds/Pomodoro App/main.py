from systemconstants import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import time

def print_something(args):
    print(args)

# Step 1) UI Setup

mainWindow = tk.Tk()
mainWindow.title("Pomodoro Study App")
mainWindow.configure(bg="black", padx=0, pady=0)
mainWindow.after(1000, print_something, 'hello world')


# 640 * 426 Canvas
canvas = tk.Canvas(width=640, height=426)

gradient_img_jpg = Image.open('GUI Builds/Pomodoro App/gradient.jpg')
gradient_img = ImageTk.PhotoImage(gradient_img_jpg) 

canvas.create_image(320,213, image=gradient_img)
canvas.grid(column=2,row=2, sticky=(tk.N, tk.W, tk.E, tk.S))
timer = canvas.create_text(320, 213, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
timer_label = canvas.create_text(320,100, text="Timer", font=(FONT_NAME, 35, 'bold'), fill="white")
# canvas.itemconfigure(timer,text="01:00")

# Start btn
start_btn = ttk.Button(master=mainWindow, text='start', padding=(5,5,5,5)).grid(column=1, row=3, sticky=(tk.W))

# reset btn
reset_btn =  ttk.Button(master=mainWindow, text="reset", padding=(5,5,5,5)).grid(column=3, row=3)

# Start ain window
mainWindow.mainloop()
