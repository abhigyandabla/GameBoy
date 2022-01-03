from turtle import Turtle

MOVE_DISTANCE = 13


class Ball(Turtle):

    # Constructor
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("SpringGreen")
        self.setheading(45)
        self.x_move_dist = MOVE_DISTANCE
        self.y_move_dist = MOVE_DISTANCE

    # Moves ball
    def move(self):
        self.goto(self.xcor() + self.x_move_dist,
                  self.ycor() + self.y_move_dist)

    # Returns True if ball collides with top or bottom wall, False otherwise
    def collision_with_wall(self):
        return self.ycor() > 275 or self.ycor() < -275

    # Makes ball bounce in opposite y direction
    def y_bounce(self):
        self.y_move_dist *= -1

    # Makes ball bounce in opposite x direction
    def x_bounce(self):
        self.x_move_dist *= -1

    # Resets ball to origin and changes direction
    def reset_pos(self):
        self.goto(0, 0)
        self.x_bounce()
