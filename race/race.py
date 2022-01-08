from turtle import Turtle, Screen, TurtleScreen
import random

# Took inspiration from 100 Days of Code by Angela Yu on Udemy, made a similar project in the course
# but the code in this is my own.


def run_turtle_race():
    # Designed so the code doesn't run until called

    # Sets screen, and asks user for their bet
    screen = Screen()
    screen.setup(width=600, height=600)
    user_bet = screen.textinput(title="Make a bet", prompt="Who will win the race? Enter a color: ")

    # Constants
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-125, -75, -25, 25, 75, 125]
    turtle_list = []

    # Creates turtle responsible for writing results at end of game
    message_turtle = Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.goto(-110, 225)
    message_turtle.hideturtle()

    # Creates 6 different coloured turtles at different y positions
    for index in range(0, 6):
        t = Turtle(shape="turtle")
        t.color(colors[index])
        turtle_list.append(t)
        t.penup()
        t.goto(x=-250, y=y_positions[index])

    # Starts race is user has made bet
    is_race_on = False
    if user_bet:
        is_race_on = True

    # While loop which controls race
    while is_race_on:
        # Loop will move each turtle randomly anywhere from 0 to 10 coordinates
        for turtle in turtle_list:
            rand_dist = random.randint(0, 10)
            turtle.forward(rand_dist)

            # If a turtle crosses the finish line, race turned off and winner decided
            if turtle.xcor() >= 250:
                winner = turtle.pencolor()
                is_race_on = False

    # Makes different final message based off of user's bet
    if user_bet == winner:
        message = f"You win. The winner was the {winner} turtle!"
    else:
        message = f"You lose. The winner was the {winner} turtle!"

    # Message turtle writes final message
    message_turtle.write(message)

    # Screen exited when "red x" is clicked
    screen.exitonclick()
    TurtleScreen._RUNNING = True
