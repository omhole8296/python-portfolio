import turtle as t

keys = {"Up": False, "Down": False, "w": False, "s": False}
def press(key): 
    keys[key] = True

def release(key): 
    keys[key] = False

class paddle(t.Turtle):
    def __init__(self,k):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.goto(k,0)


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.7, 0.7)
        self.dx = 10
        self.dy = 10   

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1