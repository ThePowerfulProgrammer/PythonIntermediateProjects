from turtle import Turtle



class Snake(object):
    

    
    def __init__(self) -> None:
        self.XCORR = 0
        self.yCORR = 0
        self.segments = []
        
        
        for _ in range(3):
            t = Turtle(shape='square')
            t.penup()
            t.color('white')
            t.setpos(x=self.XCORR, y=self.yCORR)
            self.XCORR -= 20
            
            self.segments.append(t)
            
    def move(self):
        for snakeSeg in range(len(self.segments)-1, 0, -1):
            
            new_x = self.segments[snakeSeg-1].xcor()
            new_y = self.segments[snakeSeg-1].ycor()
            
            self.segments[snakeSeg].goto(new_x,new_y)
            
        snakeHead = self.segments[0]
        snakeHead.fd(20)
        
        
            
            