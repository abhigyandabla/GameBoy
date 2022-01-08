from tkinter import *
from race import race
from snake_game import game
from hangman import hangman_main
from sketch import sketch_main
from pong import pong_main
from crossroad import crossroad_main

# Creating a new window and configurations
window = Tk()
window.title("Choose game!")
window.minsize(width=600, height=600)
window.config(padx=30, pady=30)

# Labels
label = Label(text="Choose a game to play!", font=("Courier", 18, "bold"))
label.pack()


# Buttons
def call_chosen_game(game_chosen):
    # Run game based off user decision
    window.destroy()
    if game_chosen == "race":
        race.run_turtle_race()
    elif game_chosen == "snake":
        game.run_snake_game()
    elif game_chosen == "hangman":
        hangman_main.run_hangman_game()
    elif game_chosen == "sketch":
        sketch_main.run_sketch()
    elif game_chosen == "pong":
        pong_main.run_pong_game()
    elif game_chosen == "crossroad":
        crossroad_main.run_crossroad()


def race_chosen():
    choice = "race"
    call_chosen_game(choice)


def snake_chosen():
    choice = "snake"
    call_chosen_game(choice)


def hangman_chosen():
    choice = "hangman"
    call_chosen_game(choice)


def sketch_chosen():
    choice = "sketch"
    call_chosen_game(choice)


def pong_chosen():
    choice = "pong"
    call_chosen_game(choice)


def crossroad_chosen():
    choice = "crossroad"
    call_chosen_game(choice)


# calls call_chosen_game() when pressed
button1 = Button(text="Race", command=race_chosen)
button1.config(padx=10, pady=10)
# button1.pack()
button1.place(x=245, y=100)

# calls call_chosen_game() when pressed
button2 = Button(text="Snake", command=snake_chosen)
button2.config(padx=10, pady=10)
# button2.pack()
button2.place(x=240, y=150)

# calls call_chosen_game() when pressed
button3 = Button(text="Hangman", command=hangman_chosen)
button3.config(padx=10, pady=10)
# button3.pack()
button3.place(x=230, y=200)


# calls call_chosen_game() when pressed
button4 = Button(text="Sketch", command=sketch_chosen)
button4.config(padx=10, pady=10)
# button4.pack()
button4.place(x=240, y=250)

# calls call_chosen_game() when pressed
button5 = Button(text="Pong", command=pong_chosen)
button5.config(padx=10, pady=10)
# button5.pack()
button5.place(x=245, y=300)

# calls call_chosen_game() when pressed
button6 = Button(text="Crossroad", command=crossroad_chosen)
button6.config(padx=10, pady=10)
# button6.pack()
button6.place(x=230, y=350)

window.mainloop()
