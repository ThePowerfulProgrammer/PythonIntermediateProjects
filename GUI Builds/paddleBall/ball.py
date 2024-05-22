from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__() # Parent ctor
        
        # What do I need to modify 
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(x=random.randint(-395,395), y=random.randint(-295,295))
        self.speed('fastest')
        
        print(self.pos())
        
        
    def move(self):
        self.goto(x=random.randint(-395,395), y=random.randint(-295,295))
        