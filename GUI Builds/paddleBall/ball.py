from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__() # Parent ctor
        
        # What do I need to modify 
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(x=0, y=0)
        self.speed('slow')
        
        print(self.pos())
        
        
    def move(self):
        distanceX = self.xcor() + 10
        distanceY = self.ycor() + 10
        self.goto(x=distanceX,y=distanceY)
        
    def checkPos(self):
        pass
        