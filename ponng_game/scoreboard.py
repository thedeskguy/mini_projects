from turtle import Turtle,Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,200)
        self.score_a=0
        self.score_b=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_a}  {self.score_b}",align="center",font=("Courier",80,"normal"))

    def increase_score_a(self):
        self.score_a+=1
        self.update_scoreboard()

    def increase_score_b(self):
        self.score_b+=1
        self.update_scoreboard()