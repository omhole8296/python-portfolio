import turtle as t
import turtle_cross_path as tp

screen = t.Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=tp.Player()
screen.onkey(player.front,"Up")
over=t.Turtle()
over.penup()
over.hideturtle()
over.color("black")

car=tp.CarManager()
score=tp.Scoreboard()
def game_loop():
    screen.update()
    car.car()
    if player.ycor()>=280:
        player.sety(-280)
        car.addspeed()
        score.score()
        
    for i in car.newc:
        if player.distance(i) < 25:
            over.write("Game Over",align="center",font = ("Courier", 24, "normal"))
            return
        
    screen.ontimer(game_loop, 100) 

game_loop()  

screen.exitonclick()

