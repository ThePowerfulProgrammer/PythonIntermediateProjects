from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG Battle')
screen.tracer(0)

paddle = Paddle(x_coordinate=-380, y_coordinate=0, color='Spring Green')
paddle2 = Paddle(x_coordinate=378, y_coordinate=0, color='red')
ball = Ball()

screen.listen()
screen.onkeypress(fun=paddle.Up, key='Up')
screen.onkeypress(fun=paddle.Down, key='Down')



play = True
while play:
    time.sleep(0.1)
    screen.update()
    
    paddle.checkCoordinates()
    ball.move()
    

            

screen.exitonclick()