from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__() # Parent ctor
        self.score = 0
                
        self.shape("square")
        self.goto(x=0,y=270)
        self.color("White")
        self.write(arg=f"Score: {self.score}",align='center',font=('Times New Roman',18,'bold'))
        self.hideturtle()

        
    def incrementScore(self):
        self.clear()
        self.score += 1

        
    def rewrite(self):
        self.write(arg=f"Score: {self.score}",align='center',font=('Times New Roman',18,'bold'))        
    
    def gameOver(self):
        self.goto(x=0,y=0)
        self.write(f"GAME OVER: Final Score {self.score}", align='center', font=('Oswald', 20, 'italic'))
        
    
    def getScore(self):
        return f"Final Score {self.score}"
        