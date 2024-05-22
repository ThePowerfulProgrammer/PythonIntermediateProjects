from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Paddle Ball')
screen.tracer(0)

paddle = Paddle(x_coordinate=-380, y_coordinate=0, color='Spring Green')
ball = Ball()

screen.listen()
screen.onkeypress(fun=paddle.Up, key='Up')
screen.onkeypress(fun=paddle.Down, key='Down')



play = True
while play:
    screen.update()
    time.sleep(0.2)
    
    paddle.checkCoordinates()
    
    ball.move()
            

screen.exitonclick()