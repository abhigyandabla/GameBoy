from turtle import Turtle
import random


class Food(Turtle):

    # Constructor
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("LightGreen")
        self.speed("fastest")
        self.spawn()

    # Spawns food at random x and y coordinates
    def spawn(self):
        self.goto(random.randint(-275, 275),
                  random.randint(-275, 275))
