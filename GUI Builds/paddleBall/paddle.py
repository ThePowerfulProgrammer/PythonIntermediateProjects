from turtle import Turtle

class Paddle():
    
    def __init__(self, x_coordinate, y_coordinate, color):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.color = color
        
        turtle = Turtle(shape='square')
        turtle.penup()
        
        turtle.setpos(x=self.x_coordinate, y=self.y_coordinate)
        turtle.shapesize(stretch_wid=1,stretch_len=3)
        turtle.setheading(90)
        turtle.color(self.color)
        
        self.paddle = turtle
        
    def Up(self):
        if (self.paddle.heading() != 90):
            self.paddle.setheading(90)
        self.paddle.fd(20)
        
    def Down(self):
        if (self.paddle.heading() != 270):
            self.paddle.setheading(270)
        self.paddle.fd(20)
        