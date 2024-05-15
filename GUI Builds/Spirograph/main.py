import random 
from turtle import *

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def generateSpirograph():
    colormode(255)
    t = Turtle()
    t.speed('fastest')
    
    for _  in range(80):
        t.circle(100)
        t.left(10)
        t.pencolor(random_color())
            
    screen = Screen()
    screen.exitonclick()
    
generateSpirograph()