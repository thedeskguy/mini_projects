from turtle import Turtle,Screen

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

paddle_a=Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(350,0)

screen.listen()
def paddle_a_up():
    new_y=paddle_a.ycor()+20
    paddle_a.goto(paddle_a.xcor(),new_y)
def paddle_a_down():
    new_y=paddle_a.ycor()-20
    paddle_a.goto(paddle_a.xcor(),new_y)
screen.onkey(paddle_a_up,"Up")
screen.onkey(paddle_a_down,"Down")

game_is_on=True
while game_is_on:
    screen.update()



screen.exitonclick()