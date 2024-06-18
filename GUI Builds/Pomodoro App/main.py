import systemconstants
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import time


# Step 1) UI Setup

mainWindow = tk.Tk()
mainWindow.title("Pomodoro Study App")
mainWindow.configure(bg="black", padx=0, pady=0)


# 640 * 426 Canvas
canvas = tk.Canvas(width=640, height=426)

gradient_img_jpg = Image.open('GUI Builds/Pomodoro App/gradient.jpg')
gradient_img = ImageTk.PhotoImage(gradient_img_jpg) 

canvas.create_image(320,213, image=gradient_img)
canvas.grid(column=2,row=2, sticky=(tk.N, tk.W, tk.E, tk.S))
timer_label = canvas.create_text(320,213, text="00:00", font=(systemconstants.FONT_NAME, 35, 'bold'), fill="lightgreen")

# logic

def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60
    if (seconds == 0):
        canvas.itemconfig(timer_label, text=f"{minutes}:00")
    elif (seconds < 10):
        canvas.itemconfig(timer_label, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(timer_label, text=f"{minutes}:{seconds}")
        
    print(count)
    if count > 0:
        mainWindow.after(1000, count_down, count-1)
    elif count == 0:
        systemconstants.sessions += 1
        startCount()

def startCount():
    if systemconstants.sessions % 8 == 0:
        seconds = 60*1
        count_down(seconds)        
    elif systemconstants.sessions % 2 != 0 :
        seconds = 60*systemconstants.SHORT_BREAK_MIN        
        count_down(seconds)
    else:
        seconds = 60*systemconstants.lONG_BREAK_MIN        
        count_down(seconds)
        

# Start btn
start_btn = ttk.Button(master=mainWindow, text='start', padding=(5,5,5,5), command=startCount).grid(column=1, row=3, sticky=(tk.W))

# reset btn
reset_btn =  ttk.Button(master=mainWindow, text="reset", padding=(5,5,5,5)).grid(column=3, row=3)



# Start ain window
mainWindow.mainloop()
