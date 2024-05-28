from turtle import Turtle 

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        
        # What do I need to mutate?
        self.speed('fast')
        self.shape('turtle')
        self.penup()
        self.setpos(x=0, y=-230)
        self.setheading(90)
        self.color('black')
        
    def moveForward(self):
        self.forward(20)
        
    def moveBackward(self):
        self.backward(20)
        
    # Win condiion
    def reset(self):
        self.setpos(x=0, y=-230)
        
