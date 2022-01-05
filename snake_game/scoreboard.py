from turtle import Turtle


class Scoreboard(Turtle):

    # Constructor
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 12, "normal"))

    # Adds and updates score by 1
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 12, "normal"))

    # Displays new message of "GAME OVER"
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 24, "normal"))
