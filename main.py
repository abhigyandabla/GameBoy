from turtle import Screen
from race import race
from snake_game import game
from hangman import hangman_main
from sketch import sketch_main
from pong import pong_main

# Make screen
screen = Screen()
screen.setup(600, 600)

# Let user decide which game they want to play
user_decision = screen.textinput(title="Choose a game",
                                 prompt="What game do you want to play? (Race, Snake, Hangman, Sketch, Pong): ")

# Run game based off user decision
if user_decision.lower() == "race":
    race.run_turtle_race()
elif user_decision.lower() == "snake":
    game.run_snake_game()
elif user_decision.lower() == "hangman":
    hangman_main.run_hangman_game()
elif user_decision.lower() == "sketch":
    sketch_main.run_sketch()
elif user_decision.lower() == "pong":
    pong_main.run_pong_game()

# Screen exits when "red x" is clicked
screen.exitonclick()
