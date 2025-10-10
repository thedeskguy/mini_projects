from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

colors=["red","orange","yellow","green","blue","purple"]
y_coordinates=[-70,-40,-10,20,50,80]

all_turtles=[]
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_coordinates[turtle_index])
    all_turtles.append(new_turtle)
is_race_on=False
if user_bet:
    is_race_on=True
while is_race_on: 
    for turtle in all_turtles:
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                break
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                break
screen.exitonclick()