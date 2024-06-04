import pandas as pd
from turtle import Turtle, Screen
import turtle

screen = Screen()

screen.title('Guess the U.S. state')
image = 'GUI Builds/states-guessing-game/blank_states_img.gif'
screen.addshape(name=image,shape=None)
turtle.shape(image)

def getLatLong(x,y):
    print(x,y)

df = pd.read_csv('GUI Builds/states-guessing-game/50_states.csv')

print(df[['x', 'y']])


turtle.onscreenclick(fun=getLatLong)
turtle.mainloop()