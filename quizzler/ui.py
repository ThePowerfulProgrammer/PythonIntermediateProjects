from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self):
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("350x500")
        self.window.configure(background=THEME_COLOR, pady=20, padx=20)
        
        self.score = 0
        textLabel = Label(text=f"Score: {self.score}", background=THEME_COLOR, font=("Arial",15), foreground="white", pady=10)
        textLabel.grid(row=0,column=1, sticky=(NE))
        
        
        
        mainCanvas = Canvas(master=self.window, width=300, height=250, background="white", )
        mainCanvas.grid(row=1, column=0, columnspan=2)
        
        trueImage = PhotoImage(file="quizzler/images/true.png")
        trueBtn = Button(image=trueImage, highlightthickness=0)
        trueBtn.grid(row=2, column=0, padx=10, pady=10)
        
        falseImage = PhotoImage(file="quizzler/images/false.png")
        falseBtn = Button(image=falseImage, highlightthickness=0)
        falseBtn.grid(row=2, column=1, padx=10, pady=10)
        
        
        
        self.window.mainloop()

