import random
from hangman.hangman_art import stages
from hangman.hangman_words import word_list
from turtle import Turtle, Screen, TurtleScreen

# Took inspiration from a similar project we did in the 100 days of code course by Angela Yu on Udemy
# It was a hangman console game that I coded myself with the help of the course content and made use
# of turtle all by myself to change this game from console only to GUI - this wasn't a part of the course


def run_hangman_game():
    # Run function so game runs only when called

    # Setting up screen
    screen = Screen()
    screen.setup(width=600, height=600)

    # Creates turtle responsible for writing logo
    logo_turtle = Turtle()
    logo_turtle.hideturtle()
    logo_turtle.penup()
    logo_turtle.goto(-250, 140)
    logo_turtle.hideturtle()
    logo_turtle.write(arg="HANGMAN", font=("Courier", 30, "normal"))

    # Creates turtle responsible for writing "already guessed" message
    message_turtle = Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.goto(-250, 25)
    message_turtle.hideturtle()

    # Creates turtle responsible for writing display of word being guessed
    display_turtle = Turtle()
    display_turtle.hideturtle()
    display_turtle.penup()
    display_turtle.goto(-250, -100)
    display_turtle.hideturtle()

    # Creates turtle responsible for writing whether user wins or looses
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(-250, -200)
    result_turtle.hideturtle()

    # Creates turtle responsible for drawing stages
    drawing_turtle = Turtle()
    drawing_turtle.hideturtle()
    drawing_turtle.penup()
    drawing_turtle.goto(150, 0)
    drawing_turtle.hideturtle()

    # Game related variables
    game_is_finished = False
    lives = len(stages) - 1

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    display = []
    for _ in range(word_length):
        display += "_"

    while not game_is_finished:
        guess = screen.textinput(title="Make a guess", prompt="Guess a letter: ").lower()

        # Clears message turtle, drawing turtle, display turtle
        message_turtle.clear()
        display_turtle.clear()
        drawing_turtle.clear()

        # Checks if guess is in chosen word
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        display_turtle.write(arg=f"{' '.join(display)}", font=("Arial", 12, "normal"))

        # If guess isn't in chosen word, reduces lives
        if guess not in chosen_word:
            message_turtle.write(arg=f"You guessed {guess}, that's not in the word. You lose a life.",
                                 font=("Arial", 12, "normal"))
            lives -= 1
            if lives == 0:
                game_is_finished = True
                result_turtle.write(arg=f"You lose. Correct word: {chosen_word}", font=("Arial", 18, "normal"))

        # If no more blanks left, you win message given
        if not "_" in display:
            game_is_finished = True
            result_turtle.write(arg="You win.", font=("Arial", 18, "normal"))

        # Draws stages of hangman
        drawing_turtle.write(arg=stages[lives], font=("Arial", 15, "normal"))

    screen.exitonclick()
    TurtleScreen._RUNNING = True
