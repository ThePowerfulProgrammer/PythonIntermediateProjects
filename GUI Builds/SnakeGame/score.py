from turtle import Turtle
import re

file = 'C:/Users/ashis/OneDrive/Desktop/Python/Python Intermediate Projects/GUI Builds/SnakeGame/highScores.txt'

class Score(Turtle):
    
    def __init__(self):
        super().__init__() # Parent ctor
        self.score = 0
        # What do I need to override
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
    
    def replaceHighScore(self, player_name):
        currentScore = 0
        with open(file,'r') as rFile:
                line = rFile.readline()

                res = [int(i) for i in line if i.isdigit()]
            
                currentScore = res[0]        
    
        if self.score > currentScore:
            with open(file, 'w') as wFile:
                wFile.write(f'{player_name}:{self.score}')
            return True
        else:
            return False
            
                
                
        
