from turtle import Turtle, Screen

# Setup turtle and screen
tim = Turtle()
screen = Screen()

# Set background color and line color
screen.bgcolor("black")
tim.color("white")

# Set line thickness
tim.pensize(5)

# Display the title "Etch A Sketch"
screen.title("Etch A Sketch")

# Define movement functions
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_down():
    tim.right(90)
    tim.forward(10)
    tim.left(90)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

# Bind keys to movement functions
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)

# Keep the window open
screen.mainloop()


# This was a old project from 100 days of code udemy. :)
