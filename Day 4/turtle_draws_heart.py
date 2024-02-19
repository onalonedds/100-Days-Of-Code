import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(0)

# Move the pen to starting point
t.penup()
t.goto(0, -200)
t.pendown()

# Draw the heart shape
t.begin_fill()
t.color('red')
t.left(140)
t.forward(224)
for i in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for i in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()