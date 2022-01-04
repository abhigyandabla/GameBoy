from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):

    # Constructor
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("ForestGreen")
        self.penup()
        self.goto(STARTING_POSITION)

    # Moves turtle up by MOVE_DISTANCE
    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    # Returns True when turtle finishes race, False otherwise
    def finished_level(self):
        return self.ycor() >= FINISH_LINE_Y

    def level_reset(self):
        self.goto(STARTING_POSITION)
