from turtle import Screen, TurtleScreen
from snake_game.food import Food
from snake_game.scoreboard import Scoreboard
from snake_game.snake import Snake
import time

# Took inspiration from 100 Days of Code by Angela Yu on Udemy, made a similar project in the course
# but the code in this is my own.


def run_snake_game():
    # Run function so game only runs when called

    # Making screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    delay = 0.1

    # Making snake_game, head, food, and scoreboard
    snake = Snake()
    head = snake.head
    food = Food()
    scoreboard = Scoreboard()

    # Enabling action listeners
    screen.listen()
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")

    # Starting game using while loop
    game_on = True
    while game_on:
        # Regular update to continue game for every delay in time
        screen.update()
        time.sleep(delay)
        snake.move()

        # Checking if snake_game collides with food
        if head.distance(food) < 15:
            food.spawn()
            scoreboard.add_score()
            snake.extend()

        # Checking if snake_game collides with wall
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            scoreboard.game_over()
            game_on = False

        # Checking if snake_game head collides with its tail
        if snake.self_collision():
            scoreboard.game_over()
            game_on = False

    # Exits program when "red x" is clicked
    screen.exitonclick()
    TurtleScreen._RUNNING = True
