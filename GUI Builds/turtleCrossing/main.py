from turtle import Screen
from player import Player
from obstruction import Obstruction
import time

screen = Screen()
screen.setup(width=600,height=500)
screen.bgcolor("White")
screen.title("Why did the turtle cross the road?")
screen.tracer(0) # Stop refreshing screen

player = Player()

topObstructions = []
startX = 280
startY = 252
for i in range(4):
    obstruction = Obstruction(startX=startX,startY=startY)
    topObstructions.append(obstruction)
    startY -= 58    

bottomObstructions = []
startX = 280
startY = 20
for i in range(5):
    obstruction = Obstruction(startX=startX,startY=startY)
    bottomObstructions.append(obstruction)
    startY -= 58
    
obstrunctions = topObstructions + bottomObstructions


screen.listen()
screen.onkeypress(fun=player.moveForward, key='w')
screen.onkeypress(fun=player.moveBackward, key='s')

play = True 
refereshRate = 0.15
while play:
    screen.update()
    time.sleep(refereshRate)    
    
    for o in obstrunctions:
        o.drive(lowerBound=10, upperBound=60)
        o.checkPos()

    
    if (player.ycor() > 240):
        player.reset()
        for o in obstrunctions:
            o.reset()
            
        refereshRate -= 0.05
        
        if (refereshRate < 0):
            play = False
    
    if (player.ycor() < -240):
        player.reset()




