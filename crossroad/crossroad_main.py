import time
from turtle import Screen
from crossroad.player import Player
from crossroad.car_manager import CarManager
from crossroad.scoreboard import Scoreboard
import random


def run_crossroad():
    # Run function so game runs only when called

    # Setting up screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Setting up player, car manager, scoreboard
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    # Enabling action listeners
    screen.listen()
    screen.onkey(player.move, "Up")

    # While loop that runs the game
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        # Moves all cars
        car_manager.move()

        # Removes cars moved out of bounds to left
        car_manager.remove_cars()

        # If player hasn't finished, keep moving
        if player.finished_level():
            scoreboard.level_up()
            player.level_reset()
            car_manager.level_up()

        # If player hit by car, end game
        for car in car_manager.cars:
            if player.distance(car) < 20:
                scoreboard.game_over()
                game_is_on = False

        # Creates new car if random number is 1, 1 in 4 chance of creating
        # car every single loop
        random_num = random.randint(1, 4)
        if random_num == 1:
            car_manager.make_car()


    # Exits program when "red x" is clicked
    screen.exitonclick()
