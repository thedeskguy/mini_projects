from turtle import Turtle,Screen
from paddle import Paddle
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

paddle_a=Paddle((350,0))
paddle_b=Paddle((-350,0))

screen.listen()
screen.onkey(paddle_a.go_up,"Up")
screen.onkey(paddle_a.go_down,"Down")
screen.onkey(paddle_b.go_up,"w")
screen.onkey(paddle_b.go_down,"s")

game_is_on=True
while game_is_on:
    screen.update()



screen.exitonclick()