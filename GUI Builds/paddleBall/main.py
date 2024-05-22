from turtle import Turtle,Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Paddle Ball')
screen.tracer(0)

paddle = Paddle(x_coordinate=-380, y_coordinate=0, color='Spring Green')

screen.listen()
screen.onkeypress(fun=paddle.Up, key='Up')
screen.onkeypress(fun=paddle.Down, key='Down')



play = True
while play:
    screen.update()
    
    paddle.checkCoordinates()
        
    
    

screen.exitonclick()