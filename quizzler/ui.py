from tkinter import *
from data import question_data
from quiz_brain import QuizBrain
from question_model import Question


THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("350x500")
        self.window.configure(background=THEME_COLOR, pady=20, padx=20)
        
        self.question_bank = []
        
        self.score = 0
        self.textLabel = Label(master=self.window,text=f"Score: {self.score}", background=THEME_COLOR, font=("Arial",15), foreground="white", pady=10)
        self.textLabel.grid(row=0,column=1, sticky=(NE))
        
        
        
        self.mainCanvas = Canvas(master=self.window, width=300, height=250, background="white", )
        self.mainCanvas.grid(row=1, column=0, columnspan=2)
        self.canvasText = self.mainCanvas.create_text(150,125,width=280, text="Begin Quiz", font=("Courier", 12))
        
        trueImage = PhotoImage(file="quizzler/images/true.png")
        self.trueBtn = Button(image=trueImage, highlightthickness=0, command=self.correctGuess) 
        self.trueBtn.grid(row=2, column=0, padx=10, pady=10)
        
        falseImage = PhotoImage(file="quizzler/images/false.png")
        self.falseBtn = Button(image=falseImage, highlightthickness=0, command=self.incorrectGuess)
        self.falseBtn.grid(row=2, column=1, padx=10, pady=10)
        
        
        self.getNextQuestion()
        self.window.mainloop()
        
        
    def getNextQuestion(self):        
        qText = self.quiz.next_question()
        self.mainCanvas.itemconfigure(self.canvasText, text=qText)
            
    def correctGuess(self):
        while (self.quiz.still_has_questions()):    
            self.score += 1
            self.textLabel.config(text=f"score: {self.score}")
            self.getNextQuestion()
        else:
            self.endGame()
        
    def incorrectGuess(self):
        if (self.quiz.still_has_questions()):    
            self.score += 1
            self.textLabel.config(text=f"score: {self.score}")
            self.getNextQuestion()
        else:
            self.endGame()
            
    def endGame(self):
        self.mainCanvas.itemconfig(self.canvasText, text=f"Final Score: {self.score}/{len(self.quiz.question_list)} ")
        

