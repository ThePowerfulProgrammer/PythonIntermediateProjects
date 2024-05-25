from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG Battle')
screen.tracer(0)

player1 = Paddle(x_coordinate=-380, y_coordinate=0, color='Spring Green')
player2 = Paddle(x_coordinate=370, y_coordinate=0, color='red')
ball = Ball()

player1Score = Score(x=-362, y=220)
player2Score = Score(x=358, y=220)


screen.listen()
screen.onkeypress(fun=player1.Up, key='Up')
screen.onkeypress(fun=player1.Down, key='Down')

screen.onkeypress(fun=player2.Up, key='w')
screen.onkeypress(fun=player2.Down, key='s')


play = True
while play:
    time.sleep(ball.moveSpeed)
    screen.update()
    
    player1.checkCoordinates()
    player2.checkCoordinates()
    ball.move()
    ball.outOfBounds()
    
    if (player1.paddle.distance(ball) <= 38):
        ball.reBound('player1')
    elif (player2.paddle.distance(ball) <= 38):
        ball.reBound('player2')
        
    if ball.leftOutOfBounds():
        player2Score.incrementScore()
        player2Score.rewrite()
        ball.restart()
    elif ball.rightOutOfBounds():
        player1Score.incrementScore()
        player1Score.rewrite()
        ball.restart()    
    
    
    if (player1Score.score == 5):
        play = False
    elif (player2Score.score == 5):
        play = False
    

print(f"Final Scores: Player1: {player1Score.score} Player2: {player2Score.score}")            

screen.exitonclick()