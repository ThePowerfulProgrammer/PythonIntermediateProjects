from turtle import *
import random


colorList = [(238, 237, 233), (237, 234, 238), (233, 235, 240), (215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56), (11, 87, 108), (177, 190, 213), (111, 124, 153), (81, 142, 169), (73, 63, 53)]
colormode(255)

t = Turtle()
t.shape('turtle')
t.pensize(2)


def moveFd():
    t.forward(10)

def moveBd():
    t.backward(10)
    
def rotateLeft():
    t.left(10)

def rotateRight():
    t.right(10)
    
def colorChange():
    color = random.choice(colorList)
    print(color)
    t.pencolor(color)
    
def increaseWidth():
    size =  t.pensize()
    
    if (size < 10):
        size += 1
        t.pensize(size)
        
    print(size)

def decreaseWidth():
    size =  t.pensize()
    
    if (size > 0):
        size -= 1
        t.pensize(size)
    print(size)
    
        
    
screen = Screen()
screen.listen()

screen.onkeypress(fun=moveFd,key='w')
screen.onkeypress(fun=moveBd,key='s')
screen.onkeypress(fun=rotateLeft,key='a')
screen.onkeypress(fun=rotateRight,key='d')
screen.onkeypress(fun=screen.clearscreen,key='c')
screen.onkeypress(fun=screen.resetscreen,key='c')
screen.onkeypress(fun=colorChange,key='q')
screen.onkeypress(fun=increaseWidth,key='+')
screen.onkeypress(fun=decreaseWidth,key='-')


screen.title(titlestring="Etch-A-Sketch")
screen.screensize(3000,3000)

screen.exitonclick()
