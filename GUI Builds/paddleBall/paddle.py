from turtle import Turtle

class Paddle():
    
    def __init__(self, x_coordinate, y_coordinate, color):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.color = color
        
        turtle = Turtle(shape='square')
        turtle.penup()
        
        turtle.setpos(x=self.x_coordinate, y=self.y_coordinate)
        turtle.shapesize(stretch_wid=3,stretch_len=1)
        turtle.color(self.color)
        
        self.paddle = turtle
        
        