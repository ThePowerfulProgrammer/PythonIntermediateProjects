import systemconstants
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

success = ''
timer = None


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
break_label = canvas.create_text(318,100, text='Work', font=(systemconstants.FONT_NAME, 35, 'bold'), fill="red")
timer_label = canvas.create_text(320,213, text="00:00", font=(systemconstants.FONT_NAME, 35, 'bold'), fill="lightgreen")
sessions_complete_label = canvas.create_text(320,300, text=success, fill='blue', font=(systemconstants.FONT_NAME, 20, 'italic'))

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
        
    # print(count) Redundant lol
    if count > 0:
        global timer
        timer = mainWindow.after(1000, count_down, count-1)
    elif count == 0:
        systemconstants.sessions += 1
        startCount()

def startCount():
    
    if systemconstants.sessions % 8 == 0:
        seconds = 60*systemconstants.WORK_MIN
        canvas.itemconfig(break_label, text='Work', fill='red')  
        updateSessionsComplete()      
        count_down(seconds)        
        
    elif systemconstants.sessions % 2 != 0:
        seconds = 60*systemconstants.SHORT_BREAK_MIN     
        canvas.itemconfig(break_label, text='Break', fill='pink')
        count_down(seconds)
    
    else:
        seconds = 60*systemconstants.lONG_BREAK_MIN
        canvas.itemconfig(break_label, text='Big Break', fill='lightblue')        
        count_down(seconds)
        
def updateSessionsComplete():
    global success
    success +='✓'
    canvas.itemconfigure(sessions_complete_label, text=success)
    
        
def resetCount():
    global timer
    mainWindow.after_cancel(timer)
    global success
    success= ''
    canvas.itemconfigure(timer_label, text="00:00")
    canvas.itemconfigure(sessions_complete_label, text=success)
    systemconstants.sessions = 0
    
    

# Start btn
start_btn = ttk.Button(master=mainWindow, text='start', padding=(5,5,5,5), command=startCount).grid(column=1, row=3, sticky=(tk.W))

# reset btn
reset_btn =  ttk.Button(master=mainWindow, text="reset", padding=(5,5,5,5), command=resetCount).grid(column=3, row=3)



# Start ain window
mainWindow.mainloop()
