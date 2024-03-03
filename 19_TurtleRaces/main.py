import sys
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.title("Turtle Races")
screen.bgcolor("#fddda0")
screen.setup(600, 600)
user_bet = screen.textinput("Make your bet",
                            "Which turtle will win the race?\nEnter a color (red, black, green, blue, purple): ")
colors = ["red", "black", "green", "blue", "purple"]
winner = ""
race_is_on = False

if user_bet:
    race_is_on = True
else:
    sys.exit()


def print_message(msg, txt_color):
    writer_turtle = Turtle()
    writer_turtle.hideturtle()  # Hide the turtle, as we only want to see the text
    writer_turtle.penup()  # Prevent drawing when moving
    writer_turtle.goto(0, 0)
    writer_turtle.color(txt_color)
    writer_turtle.write(msg, align="center", font=("Arial", 24, "normal"))


y = 250

for color in colors:
    y -= 80
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-290, y)

while race_is_on:
    for turtle in screen.turtles():
        if turtle.xcor() <= 270:
            turtle.forward(randint(0, 10))
        else:
            race_is_on = False
            clr = turtle.color()
            if user_bet == clr[0]:
                print_message(f"{clr[0].title()} is a winner!\nYou guessed right!", clr[0])
            else:
                print_message(f"{clr[0].title()} is a winner!\nYou guessed wrong!", clr[0])

screen.exitonclick()
