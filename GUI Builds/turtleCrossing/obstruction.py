from turtle import Turtle
import random

colors = ['red','blue','maroon','green','yellow', 'silver','spring green', 'cyan', 'purple', 'pink', 'black',
          'green', 'red', 'blue', 'salmon', 'cyan', 'brown']


class Obstruction(Turtle):
    
    def __init__(self, startX, startY):
        super().__init__()
        
        self.startX = startX
        self.startY = startY
        
        # What do I need to override
        self.penup()
        self.setpos(x=self.startX, y=self.startY)
        self.color(random.choice(colors))
        self.shape('square')
        self.shapesize(stretch_len=4)
        self.speed('fastest')
        
        
    def drive(self, lowerBound, upperBound):
        self.backward(random.randint(lowerBound,upperBound))
        
    def reset(self):
        self.setpos(x=self.startX, y=self.startY)
        
    def checkPos(self):
        if self.xcor() < -300:
            self.reset()
        
        