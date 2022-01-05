from turtle import Turtle

FONT_LEVEL = ("Courier", 15, "normal")
FONT_GAME_OVER = ("Courier", 24, "normal")
STARTING_POSITION = (-280, 265)


class Scoreboard(Turtle):

    # Constructor
    def __init__(self):
        super().__init__()
        with open("crossroad/data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.level = 1
        self.print_level()

    # Writes current level onto screen
    def print_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level} High Score: {self.high_score}", font=FONT_LEVEL)

    # Increases level by 1
    def level_up(self):
        self.level += 1
        self.print_level()

    # Writes "GAME OVER"
    def game_over(self):
        self.goto(0, 0)
        if self.level > self.high_score:
            with open("crossroad/data.txt", mode="w") as data:
                data.write(f"{self.level - 1}")
        self.write(arg="GAME OVER", align="center", font=FONT_GAME_OVER)
