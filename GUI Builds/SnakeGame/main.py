from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Python")
screen.tracer(0)

player_Name = screen.textinput(title="Player Name: ", prompt="Enter Name: ")



snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(fun=snake.Up,key="Up")
screen.onkeypress(fun=snake.Down,key="Down")
screen.onkeypress(fun=snake.Right,key="Right")
screen.onkeypress(fun=snake.Left,key="Left")


#Play The Game
play = True
while play: 
    screen.update()
    time.sleep(0.07)

    snake.move()

    
    if (snake.snakeHead.distance(food) < 15 ):
        print("Consumed")
        snake.addSegment()
        food.move()
        score.incrementScore()
        score.rewrite()

        
    if (snake.detectCollission()):
        play = False
        score.gameOver()
        

        

print(score.getScore())

if (score.replaceHighScore(player_name=player_Name)):
    print("You have the new highest score")


screen.exitonclick()