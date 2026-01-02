import turtle as t
import snake as s
import random

t.colormode(255)
screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

scoreboard=t.Turtle()
snake=s.Snake()
foods=s.food()
gameover=t.Turtle()

gameover.hideturtle() 
gameover.color("white")
scoreboard.hideturtle() 
scoreboard.goto(0, 260)
scoreboard.color("white")
n=0 
scoreboard.write(f"Score : {n}",align="center",font=("Arial",30,"normal"))
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

def game_loop(n):
    for segment in snake.seg[1:]:  
        if snake.head.distance(segment) < 10:
            print(f"your score is : {n}")
            gameover.write("Game Over",align="center",font=("Arial",30,"normal"))
            return 
    
    screen.update()
    snake.move()
    if snake.head.distance(foods)<15:
        foods.goto(random.randint(-280,280),random.randint(-280,280))
        snake.k()
        n+=1
        scoreboard.clear()
        scoreboard.write(f"Score : {n}",align="center",font=("Arial",30,"normal"))
        
    screen.ontimer(lambda:game_loop(n), 100)
    
game_loop(n)

screen.exitonclick()