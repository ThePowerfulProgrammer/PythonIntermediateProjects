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

screen.tracer(0)

df = pd.read_csv('GUI Builds/states-guessing-game/50_states.csv')

play = True
correctGuesses = 0
while play:
    screen.update()
    stateGuess = screen.textinput(title="Enter a state", prompt="State: ")
    stateGuess.lower()
    stateGuess.capitalize() 
    try:
        filtered = df[(df.state == stateGuess)].iloc[0]
        player.writeState(lat=filtered.x, lon=filtered.y, stateName=filtered.state)
        keepPlaying = screen.numinput(title='Keep Playing? ', prompt='0 | 1', default=0, minval=0, maxval=1)
        if (keepPlaying == 1):
            play = False
            
    except IndexError:
        print("Incorrect")
        
    if correctGuesses == len(df.index):
        play = False
        

if (correctGuesses == len(df.index)):
    print("You WON!!!")
else:
    print("You LOST!!!")