from turtle import *
import random

# import colorgram

# colors = colorgram.extract("image.jpg",35)


# allColors = []

# for i in range(len(colors)):
#     current = colors[i]
#     rgb = current.rgb 
#     rgbTuple = (rgb.r, rgb.g, rgb.b)
    
#     allColors.append(rgbTuple)
    
# print(allColors)
    
colorList = [(238, 237, 233), (237, 234, 238), (233, 235, 240), (215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56), (11, 87, 108), (177, 190, 213), (111, 124, 153), (81, 142, 169), (73, 63, 53)]

# Create a hirst Painting
def generatePainting():
    colormode(255)
    t = Turtle()
    t.penup()
    t.setpos(-200,-200)
    t.pendown()
    
    t.shape('turtle')
    t.speed('fastest')
    
    for row in range(10):
        for col in range(10):
            color = random.choice(colorList)
            t.pencolor(color)

            
            t.dot(size=20)
            t.penup()
            if (col != 9):
                t.fd(50)
                t.pendown()
        if (row % 2 == 0):
            t.left(90)
            t.penup()
            t.fd(50)
            t.left(90)
            t.pendown()
        else:
            t.right(90)
            t.penup()
            t.fd(50)
            t.right(90)
            t.pendown()
            
    screen = Screen()
    screen.exitonclick()
            
generatePainting()
    