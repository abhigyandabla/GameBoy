from turtle import Turtle


class Scoreboard(Turtle):

    # Constructor
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))

    # Adds and updates score by 1
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))

    # Displays new message of "GAME OVER"
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 24, "normal"))
