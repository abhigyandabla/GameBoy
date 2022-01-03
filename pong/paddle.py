from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(x, y)
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)

    # Moves paddle up
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    # Moves paddle down
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
