from turtle import Turtle, Screen

# Constants to move the turtle each time and angle by
MOVE_BY = 8
ANGLE_BY = 10


def run_sketch():

    # Making turtle and setting up screen
    t = Turtle()
    screen = Screen()
    screen.setup(width=600, height=600)

    # Turtle responsible for writing instructions
    instruction_turtle = Turtle()
    instruction_turtle.hideturtle()
    instruction_turtle.penup()
    instruction_turtle.goto(-250, 250)
    instruction_turtle.hideturtle()
    instruction_turtle.write(arg="Arrow keys to move, c to clear", font=("Arial", 12, "normal"))

    def move_forwards():
        t.forward(MOVE_BY)

    def move_backwards():
        t.backward(MOVE_BY)

    def turn_left():
        t.setheading(t.heading() + ANGLE_BY)

    def turn_right():
        t.setheading(t.heading() - ANGLE_BY)

    # Clears drawing and returns to origin
    def clear():
        t.clear()
        t.penup()
        t.home()
        t.pendown()

    screen.listen()
    screen.onkey(move_forwards, "Up")
    screen.onkey(move_backwards, "Down")
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(clear, "c")

    screen.exitonclick()
