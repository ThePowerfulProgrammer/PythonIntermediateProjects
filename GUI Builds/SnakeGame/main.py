from turtle import *
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Python")
screen.tracer(0)



snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(fun=snake.Up,key="Up")
screen.onkeypress(fun=snake.Down,key="Down")
screen.onkeypress(fun=snake.Right,key="Right")
screen.onkeypress(fun=snake.Left,key="Left")

play = True
counter = 0
while play: 
    screen.update()
    time.sleep(0.1)

    snake.move()
    


    



screen.exitonclick()