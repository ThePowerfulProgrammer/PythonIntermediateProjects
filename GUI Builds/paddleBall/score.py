from turtle import Turtle

class Score(Turtle):
    
    def __init__(self, x, y):
        super().__init__() # Parent ctor
        self.score = 0
        self.x = x 
        self.y = y
        
        # What do I need to overload?
        self.shape('square')
        self.speed('fastest')
        self.goto(x=self.x, y=self.y)
        self.color('white')
        self.write(arg=f'{self.score}', align='center', font=('Oswald', 50, 'bold'))
        self.hideturtle()
        
        
    def incrementScore(self):
        self.clear()
        self.score += 1
        
    def rewrite(self):
        self.goto(x=self.x, y=self.y)        
        self.write(arg=f'{self.score}', align='center', font=('Oswald', 50, 'bold'))

        
    def getScore(self):
        return f'Final Score: {self.score}'
    

    
    
        
        
        