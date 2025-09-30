import turtle as t
import random 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

# car
class CarManager():
    def __init__(self):
        self.newc=[]
        self.mspeed= MOVE_INCREMENT 
        
    def car(self):
        r=random.randint(1,6)
        if r==1:
            y=random.randint(-250,250)
            c=t.Turtle("square")
            c.penup()
            c.shapesize(1,2)
            c.color(random.choice(COLORS))
            c.goto(300,y)
            self.newc.append(c)
        for i in self.newc:
            i.backward(self.mspeed)
            
    def addspeed(self):
        self.mspeed+=5
    
# player
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def front(self):
        self.forward(10)
        

# Scoreboard
class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.n=1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-200, 260)
        self.write(f"Level {self.n}",align="center",font = ("Courier", 24, "normal"))
    def score(self) :
        self.clear()  
        self.n+=1
        self.write(f"Level {self.n}",align="center",font = ("Courier", 24, "normal"))  
    
    
    
