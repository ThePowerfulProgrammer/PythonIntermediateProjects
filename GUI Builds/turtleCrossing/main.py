from turtle import Screen
from player import Player
import time

screen = Screen()
screen.setup(width=600,height=500)
screen.bgcolor("White")
screen.title("Why did the turtle cross the road?")
screen.tracer(0) # Stop refreshing screen

player = Player()

screen.listen()
screen.onkeypress(fun=player.moveForward, key='w')
screen.onkeypress(fun=player.moveBackward, key='s')

play = True 
refereshRate = 0.15
while play:
    screen.update()
    time.sleep(refereshRate)    
    
    if (player.ycor() > 240):
        player.reset()
        refereshRate -= 0.01
    
    if (player.ycor() < -240):
        player.reset()




