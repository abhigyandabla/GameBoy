from turtle import Screen, TurtleScreen
from pong.paddle import Paddle
from pong.ball import Ball
from pong.scoreboard import Scoreboard
import time

# Took inspiration from 100 Days of Code by Angela Yu on Udemy, made a similar project in the course
# but the code in this is my own.


def run_pong_game():
    # Made run function so it runs when called

    # Setting up screen
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    # Making paddles, ball, and scoreboard
    l_paddle = Paddle(-350, 0)
    r_paddle = Paddle(350, 0)
    ball = Ball()
    scoreboard = Scoreboard()

    # Enabling action listeners
    screen.listen()
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")

    # Looping to continue game
    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()
        ball.move()

        # Detecting ball's collision with wall
        if ball.collision_with_wall():
            ball.y_bounce()

        # Detecting ball's collision with right paddle
        if ball.distance(r_paddle) < 55 and ball.xcor() > 320:
            ball.x_bounce()

        # Detecting ball's collision with left paddle
        if ball.distance(l_paddle) < 55 and ball.xcor() < -320:
            ball.x_bounce()

        # Detecting if ball is out of bounds to right and left gains point
        if ball.xcor() > 385:
            ball.reset_pos()
            scoreboard.add_score("left")

        # Detecting if ball is out of bounds to left and right gains point
        if ball.xcor() < -385:
            ball.reset_pos()
            scoreboard.add_score("right")

        # Check if a player has won
        if scoreboard.game_over():
            scoreboard.game_over_pop_up()
            game_on = False

    # Screen exits when "red x" is clicked
    screen.exitonclick()
    TurtleScreen._RUNNING = True
