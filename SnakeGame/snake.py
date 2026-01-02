import turtle as t
import random 
positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake():
    
    def __init__(self):
        self.seg = []
        self.createsnake()
        self.head = self.seg[0]
        self.head.shape("triangle")
     
    def createsnake(self):   
        for pos in positions:
            vasu = t.Turtle("square")
            vasu.penup()
            vasu.color("white")
            vasu.goto(pos)
            self.seg.append(vasu)


    def left(self):
        if self.head.heading() != 0: 
            self.head.setheading(180) 

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def k(self):
        vasu = t.Turtle("square")
        vasu.penup()
        vasu.color("white")
        tail = self.seg[-1].position()
        vasu.goto(tail)
        self.seg.append(vasu)


    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            self.seg[i].goto(self.seg[i - 1].position())
        self.head.forward(20)
        
        if not(-300<self.head.xcor() <300) or not(-300<self.head.ycor() <300):
            # xpos=self.head.xcor()
            # ypos=self.head.ycor()
            # if self.head.heading() == 0 or self.head.heading() ==180:
            #     self.head.goto(-xpos,ypos)
            # elif self.head.heading() == 90 or self.head.heading() ==270:
            #     self.head.goto(xpos,-ypos)
            
            if self.head.xcor() > 300:
                self.head.setx(-300)
            elif self.head.xcor() < -300:
                self.head.setx(300)
            elif self.head.ycor() > 300:
                self.head.sety(-300)
            elif self.head.ycor() < -300:
                self.head.sety(300)

class food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.speed("fast")
        self.goto(random.randint(-280,280),random.randint(-280,280))
        self.color("blue")

        
        
