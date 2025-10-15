from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

paddle_a=Paddle((350,0))
paddle_b=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(paddle_a.go_up,"Up")
screen.onkey(paddle_a.go_down,"Down")
screen.onkey(paddle_b.go_up,"w")
screen.onkey(paddle_b.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detect collision with paddles
    if (ball.distance(paddle_a)<50 and ball.xcor()>320) or (ball.distance(paddle_b)<50 and ball.xcor()<-320):
        ball.bounce_x()

    #Detect when paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.increase_score_a()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.increase_score_b()


screen.exitonclick()