import pandas as pd
from turtle import Turtle, Screen

screen = Screen()

screen.title('Guess the U.S. state')
image = 'GUI Builds/states-guessing-game/blank_states_img.gif'
screen.register_shape(image)

screen.exitonclick()