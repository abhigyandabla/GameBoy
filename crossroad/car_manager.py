from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SAFE_ZONE_TOP = 250
SAFE_ZONE_BOTTOM = -250


class CarManager:

    # Constructor
    def __init__(self):
        self.cars = []
        self.level = 1

    # Makes car and adds to list of cars
    def make_car(self):
        car = Turtle("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        car.penup()
        y_coord = random.randint(SAFE_ZONE_BOTTOM, SAFE_ZONE_TOP)
        car.goto(300, y_coord)
        self.cars.append(car)

    # Moves cars by MOVE_INCREMENT to the left
    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - MOVE_INCREMENT * self.level, car.ycor())

    def level_up(self):
        self.level += 1

    def remove_cars(self):
        for car in self.cars:
            if car.xcor() < -330:
                self.cars.remove(car)
