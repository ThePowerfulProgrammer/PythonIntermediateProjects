import pandas as pd
from turtle import Screen
from player import Player

import turtle

screen = Screen()
player = Player()


screen.title('Guess the U.S. state')
image = 'GUI Builds/states-guessing-game/blank_states_img.gif'
screen.addshape(name=image,shape=None)
turtle.shape(image)

def getLatLong(x,y):
    print(x,y)

turtle.onscreenclick(fun=getLatLong)




turtle.mainloop()
player.writeState(100,100,'Miss')