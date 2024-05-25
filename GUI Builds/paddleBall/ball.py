from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__() # Parent ctor
        
        # members unique to Ball
        self.moveX = 10
        self.moveY = 10
        self.moveSpeed = 0.2
        
        # What do I need to modify 
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(x=0, y=0)
        self.speed('slow')
        
        print(self.pos())
        
    
    def restart(self):
        self.moveX *= -1
        self.moveY *= -1
        self.goto(x=0,y=0)
        self.moveSpeed = 0.1


    def move(self):
        distanceX = self.xcor() + self.moveX
        distanceY = self.ycor() + self.moveY
        self.goto(x=distanceX,y=distanceY)
        
    def outOfBounds(self):
        if self.ycor() > 295:
            self.moveY *= -1 
            return True
        elif self.ycor() < -295:
             self.moveY *= -1 
             return True
        return False 
     
     
    def rightOutOfBounds(self):
        if self.xcor() > 400:
            return True
        return False
    
    def leftOutOfBounds(self):
        if self.xcor() < -400:
            return True
        return False
    
    def reBound(self, paddle):
        if paddle == 'player1':
            left_or_right =  random.randint(0,1)
            if (left_or_right == 0):
                self.moveX *= -1
                self.moveY *= -1
            else: 
                self.moveX *= -1   
        elif paddle == 'player2':
            left_or_right =  random.randint(0,1)
            if (left_or_right == 0):
                self.moveX *= -1
                self.moveY *= -1
            else:
                self.moveY *= -1 
        if (self.moveSpeed > 0.02):
            self.moveSpeed -= 0.02
        else:
            self.moveSpeed = 0.02

        
        