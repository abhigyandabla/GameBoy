from turtle import Turtle

TO_WIN = 5


class Scoreboard(Turtle):

    # Constructor
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score(self.l_score, self.r_score)

    # Updates score and clears previous one
    def update_score(self, left, right):
        self.clear()
        self.write(arg=f"{left} : {right}", align="center", font=("Arial", 20, "normal"))

    # Adds score to side which won point
    def add_score(self, side):
        if side == "left":
            self.l_score += 1
        elif side == "right":
            self.r_score += 1

        self.update_score(self.l_score, self.r_score)

    # Returns True if a side wins, False otherwise
    def game_over(self):
        return self.l_score >= TO_WIN or self.r_score >= TO_WIN

    # Pops up game over message
    def game_over_pop_up(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 30, "normal"))
