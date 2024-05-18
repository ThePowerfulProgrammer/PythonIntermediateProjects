from turtle import *
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Python")
screen.tracer(0)



snake = Snake()

play = True
counter = 0
while play:
    screen.update()
    time.sleep(0.1)

    snake.move()

    



screen.exitonclick()