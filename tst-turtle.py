import turtle

# Create a Turtle screen/window
wn = turtle.Screen()
wn.title("Turtle Triangle")  # Set the window title

# Create a Turtle object
t = turtle.Turtle()

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)  # Move forward by 100 units
        t.left(120)     # Turn left by 120 degrees

# Call the function to draw the triangle
draw_triangle()

# Close the window when clicked
wn.exitonclick()
