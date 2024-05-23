from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG Battle')
screen.tracer(0)

player1 = Paddle(x_coordinate=-380, y_coordinate=0, color='Spring Green')
player2 = Paddle(x_coordinate=378, y_coordinate=0, color='red')
ball = Ball()

screen.listen()
screen.onkeypress(fun=player1.Up, key='Up')
screen.onkeypress(fun=player1.Down, key='Down')

screen.onkeypress(fun=player2.Up, key='w')
screen.onkeypress(fun=player2.Down, key='s')


play = True
while play:
    time.sleep(0.1)
    screen.update()
    
    player1.checkCoordinates()
    player2.checkCoordinates()
    ball.move()
    ball.outOfBounds()
    
    if (player1.paddle.distance(ball) <= 38):
        ball.reBound()
    elif (player2.paddle.distance(ball) <= 38):
        ball.reBound()
    

            

screen.exitonclick()