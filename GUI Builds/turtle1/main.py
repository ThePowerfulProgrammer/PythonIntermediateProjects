from turtle import *
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def walk():
    turtwig = Turtle()
    turtwig.shape('turtle')
    turtwig.speed(5)
    turtwig.pensize(width=6)
    colormode(255)

    angles = [0,90,180,270]
        
    for _ in range(100):
        turtwig.setheading(random.choice(angles))
        turtwig.pencolor(random_color())
        turtwig.fd(40)

    screen = Screen()
    screen.exitonclick()
    
walk()