from turtle import Turtle



class player(Turtle):
    
    def __init__(self):
        super().__init__() # Init all data using parent 
        
        # What do I need?
        
        
        # what do I need to overload
        self.penup()
        self.setpos(x=0, y=0)
        self.hideturtle()
        self.color('white')
        self.speed('fastest')
        
    def writeState(self, lat, lon, stateName):
        self.setpos(x=lat, y=lon)
        self.write(arg=stateName)
    
    
        
        