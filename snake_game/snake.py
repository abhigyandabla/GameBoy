from turtle import Turtle

# Constants
MOVE_DISTANCE = 20
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    # Constructor
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creates snake_game segments in starting positions
    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_segment(pos)

    # Adds segment at given position
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    # Moves every segment in snake_game
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    # Extends one more segment onto tail
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Returns True is snake_game collides with self, False otherwise
    def self_collision(self):
        for segment in self.segments:
            if segment == self.head:
                pass
            elif self.head.distance(segment) < 2:
                return True
        return False

    # Turns left as long as heading is not right
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    # Turns right as long as heading is not left
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    # Turns upwards as long as heading is not down
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    # Turns downwards as long as heading is not up
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
