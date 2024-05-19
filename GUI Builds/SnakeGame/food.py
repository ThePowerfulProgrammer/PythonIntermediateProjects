from turtle import Turtle
import random

colors = ['red','blue','Spring Green', 'Yellow', 'gold', 'maroon', 'lightblue', 'green', 'purple','darkblue']

class Food(Turtle):
    
    def __init__(self):
        super().__init__() # Parent Ctor
        
        # What do I need my food to modify?
        
        self.shape('circle')
        self.color(random.choice(colors))
        self.penup()
        self.speed('fastest')
        self.goto(x=random.randint(-285,285), y=random.randint(-285,285))
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        
        print(self.pos())
        
    def move(self):
        self.color(random.choice(colors))
        self.goto(x=random.randint(-285,285), y=random.randint(-285,285))
        
        
        