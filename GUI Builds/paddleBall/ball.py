from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__() # Parent ctor
        
        # members unique to Ball
        self.moveX = 10
        self.moveY = 10
        
        # What do I need to modify 
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(x=0, y=0)
        self.speed('slow')
        
        print(self.pos())


    def move(self):
        distanceX = self.xcor() + self.moveX
        distanceY = self.ycor() + self.moveY
        self.goto(x=distanceX,y=distanceY)
        
    def outOfBounds(self):
        if self.ycor() > 295:
            self.moveX = self.moveX
            self.moveY = -self.moveY
            return True
        elif self.ycor() < -295:
             self.moveX = self.moveX
             self.moveY = -(self.moveY)
             return True
        return False 
     
    def reBound(self):
        left_or_right = random.randint(0,1)
        if (left_or_right == 0):
            self.moveX = -self.moveX
            self.moveY = 10
        else:
            self.moveX = -self.moveX
            self.moveY = -self.moveY
        
        