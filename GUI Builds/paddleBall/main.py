from turtle import Turtle,Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Paddle Ball')
screen.tracer(0)

paddle = Paddle(x_coordinate=-380, y_coordinate=0, color='Spring Green')

play = True
while play:
    screen.update()
    
    

screen.exitonclick()