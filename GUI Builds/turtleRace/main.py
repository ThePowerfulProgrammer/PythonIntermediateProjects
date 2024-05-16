from turtle import *
import random

screen = Screen()
screen.setup(width=500,height=400)
screen.bgcolor('azure')


bet = screen.textinput(title='Race Bet!!!', prompt='Which turtle do you think will win? ')

while bet not in ('lightgreen','Darkgreen','blue','red','blue'):
    bet = screen.textinput(title='Race Bet!!!', prompt='Which turtle do you think will win? ')


turtwig = Turtle(shape='turtle')
torterra = Turtle(shape='turtle')
squirtle = Turtle(shape='turtle')
blastoise = Turtle(shape='turtle')
shuckle = Turtle(shape='turtle')

turtwig.color('lightgreen')
turtwig.penup()
turtwig.goto(x=-230,y=0)

torterra.color('Darkgreen')
torterra.penup()
torterra.goto(x=-230, y=-60)

squirtle.color('blue')
squirtle.penup()
squirtle.goto(x=-230, y=-120)

blastoise.color('black')
blastoise.penup()
blastoise.goto(x=-230, y=60)

shuckle.color('red')
shuckle.penup()
shuckle.goto(x=-230, y=120)

turtles = [turtwig,torterra,shuckle,squirtle,blastoise]

play = False
if bet:
    play = True

while play:
    
    for turtle in turtles:
        if turtle.xcor() > 230:
            play = False
            
            if (turtle.pencolor() == bet):
                print(f"You are the winner!, The winner is {turtle.pencolor()}")
            else:
                 print(f"You are the loser!, The winner is {turtle.pencolor()}")
        
        turtle.fd(random.choice([0,10]))
        
    



screen.exitonclick()



