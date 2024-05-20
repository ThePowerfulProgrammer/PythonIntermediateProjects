from turtle import Turtle



class Snake(object):
    
    def __init__(self) -> None:
        self.XCORR = 0
        self.yCORR = 0
        self.segments = []

        
        
        for i in range(3):
            t = Turtle(shape='square')
            t.penup()
            t.color('Spring Green')
            t.setpos(x=self.XCORR, y=self.yCORR)
            self.XCORR -= 20
             
            print(t.speed())
            self.segments.append(t)
            
        self.snakeHead = self.segments[0]
        self.snakeTail = self.segments[-1]
        print(self.snakeHead.pos())
        
                
    
    def addSegment(self):
        t = Turtle(shape='square')
        t.penup()
        t.color('Spring Green')
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        t.setpos(x=new_x, y=new_y)
        
        self.segments.append(t)
        
            
    def move(self):
        for snakeSeg in range(len(self.segments)-1, 0, -1):
            
            new_x = self.segments[snakeSeg-1].xcor()
            new_y = self.segments[snakeSeg-1].ycor()
            
            self.segments[snakeSeg].goto(new_x,new_y)
            
        self.snakeHead.fd(20)
        
    def detectWallCollision(self):
        if (self.snakeHead.xcor() > 300 or self.snakeHead.xcor() < -300):
            return True
        elif (self.snakeHead.ycor() > 300 or self.snakeHead.ycor() < -300):
            return True
        return False
        
    def detectSelfCollision(self):
        for segment in self.segments[1:]:
            if (self.snakeHead.distance(segment) < 5):
                return True
        return False
            
    def detectCollission(self):
        return (self.detectWallCollision() or self.detectSelfCollision())
        
    # Change direction to right    
    def Right(self):
        if self.snakeHead.heading() != 180:
            self.snakeHead.setheading(0)
        
    # change direction to left 
    def Left(self):
        if self.snakeHead.heading() != 0:
            self.snakeHead.setheading(180)
        
    # Change direction to up
    def Up(self):
        if self.snakeHead.heading() != 270:
            self.snakeHead.setheading(90)

    # Change direction to down
    def Down(self):
        if self.snakeHead.heading() != 90:
            self.snakeHead.setheading(270)
        
        
        
        
            
            