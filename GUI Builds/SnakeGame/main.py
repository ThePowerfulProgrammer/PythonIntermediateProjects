from turtle import *
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Python")
screen.tracer(0)

turtles = []
xCorr = 0
yCorr = 0

for _ in range(3):
    t = Turtle(shape="square")
    t.penup()
    t.color("White")
    t.setpos(x=xCorr,y=yCorr)
    xCorr -= 20
    turtles.append(t)
    
play = True
counter = 0
while play:
    screen.update()
    for t in turtles:
        t.fd(20)
        time.sleep(0.1)
    
    counter += 1
    if (counter == 10):
        play = False
    



screen.exitonclick()