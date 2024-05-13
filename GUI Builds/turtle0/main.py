from turtle import Turtle,Screen

# Draw a square
def generateTurtleSquare(size:int):
    turtle = Turtle()
    turtle.color('indigo')
    turtle.shape('turtle')

    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    
    screen = Screen()
    screen.exitonclick()

# Generate a web
def generateGeometricPattern():
    turtwig = Turtle()
    for steps in range(100):
        for c in ('cyan','red', 'darkgreen'):
             turtwig.color(c)
             turtwig.forward(steps)
             turtwig.right(30)
    
    screen = Screen()
    screen.exitonclick()

# Generate a dash line
def generateDashedLine():
    turtwig = Turtle()
    
    for _  in range(10):
        turtwig.forward(10)
        turtwig.up()
        turtwig.forward(10)
        turtwig.down()
        
    screen = Screen()
    screen.exitonclick()
        
        
# Creates a shape of sides = 3-10
def generateShapes():
    colors = ['red','blue','green','darkred','cyan','yellow','black','pink']
    turtwig = Turtle()
    
    
    sides = 3
    angles = [120,90,72,60,51.43,45,40,36]
    for _ in range(len(angles)):
        turtwig.color(colors[_])
        
        for i in range(sides):
            turtwig.forward(100)
            turtwig.right(angles[_])
        sides += 1

        
    screen = Screen()
    screen.exitonclick()    

generateShapes()
    