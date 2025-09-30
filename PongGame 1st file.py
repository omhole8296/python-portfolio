import turtle as t
import PongGame as p
t.colormode(255)
screen = t.Screen()
screen.bgcolor("black")
screen.setup(1500, 700)
screen.tracer(0)

l=0
r=0
scoreboard=t.Turtle()
scoreboard.sety(275)
scoreboard.hideturtle()
scoreboard.color("white")
scoreboard.write(f"{l}:{r}",align="center",font=("Arial",40,"normal"))

midline=t.Turtle()
midline.teleport(0,300)
midline.pencolor("white")
midline.hideturtle()
midline.right(90)
midline.speed(0)

lscore=t.Turtle()
lscore.teleport(50,0)
lscore.pencolor("white")
lscore.hideturtle()
lscore.penup()
lscore.goto(0,-50)


while midline.ycor()>-300: 
    midline.pendown()
    midline.forward(15)
    midline.penup()
    midline.forward(15)



lpa=p.paddle(-700) 
rpa=p.paddle(700)

screen.listen()

ball=p.Ball()
ball.speed(0)   


screen.listen()
screen.onkeypress(lambda: p.press("Down"), "Down")
screen.onkeypress(lambda: p.press("Up"), "Up")
screen.onkeypress(lambda: p.press("w"), "w")
screen.onkeypress(lambda: p.press("s"), "s")

screen.onkeyrelease(lambda: p.release("Up"), "Up")
screen.onkeyrelease(lambda: p.release("Down"), "Down")
screen.onkeyrelease(lambda: p.release("w"), "w")
screen.onkeyrelease(lambda: p.release("s"), "s")

def game_loop():
    global l,r
    ball.move()  
    if l>9 or r>9:
        if l<r:
            lscore.write("Game Over \n Right Wins",align="center",font=("Arial",30,"normal"))
        else:
            lscore.write("Game Over \n Left Wins",align="center",font=("Arial",30,"normal"))
        ball.sety(0)
        ball.hideturtle()
        return 
    
    if ball.xcor()<-750 or ball.xcor()>750:
        scoreboard.clear()
        if ball.xcor()<-750:
            ball.goto(0,0)
            ball.bounce_x()
            r+=1
            scoreboard.write(f"{l}:{r}",align="center",font=("Arial",40,"normal"))
        else:
            ball.goto(0,0)
            ball.bounce_x()
            l+=1
            scoreboard.write(f"{l}:{r}",align="center",font=("Arial",40,"normal"))
            
    if ball.ycor()>330 or ball.ycor()<-330:
        ball.bounce_y()
    

    if (ball.distance(lpa)<50 and ball.xcor()<-690 and ball.xcor()>-710) or (ball.distance(rpa)<50 and ball.xcor()>690 and ball.xcor()<710):
        ball.bounce_x()

       
    if p.keys["Up"]:
        if rpa.ycor()<320:
            rpa.sety(rpa.ycor() + 20)
    if p.keys["Down"]:
        if rpa.ycor()>-320:
            rpa.sety(rpa.ycor() - 20)
    if p.keys["w"]:
        if lpa.ycor()<320:
            lpa.sety(lpa.ycor() + 20)
    if p.keys["s"]:
        if lpa.ycor()>-320:
            lpa.sety(lpa.ycor() - 20)
    screen.update()
    screen.ontimer(game_loop, 20)
screen.update()
game_loop()

screen.exitonclick()

