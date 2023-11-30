import turtle
import random

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed (0 is the fastest)

# Function to draw a colorful petal
def draw_petal():
    t.color("red")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50, 60)
    t.left(120)
    t.circle(50, 60)
    t.end_fill()

# Move the turtle to the starting position
t.penup()
t.goto(0, -200)
t.pendown()

# Draw multiple petals to form a flower
for _ in range(36):  # Draw 36 petals
    draw_petal()
    t.left(10)  # Rotate the turtle for the next petal

# Add a flower center
t.penup()
t.goto(0, -200)
t.color("yellow")
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
t.exitonclick()
