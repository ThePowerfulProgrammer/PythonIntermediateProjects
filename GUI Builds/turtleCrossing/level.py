from turtle import Turtle 


class Level(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.level = 1
        # What do I need to modify
        self.speed('fastest')
        self.penup()
        self.hideturtle()
        self.color('Black')
        self.setpos(x=-270, y=220)
        self.write(f"Level: {self.level}", align='left', font=('Oswald', 15, 'italic'))
        
    def nextLevel(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='left', font=('Oswald', 15, 'italic'))