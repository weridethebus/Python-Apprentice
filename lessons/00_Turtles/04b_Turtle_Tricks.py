
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600, starty = 0, startx = 0)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed = 0

def shape_spiral():
    for i in range(500):
        tina.forward(i*1.001)
        tina.left(72 * 1.01)
        tina.forward(i*1.001)
        tina.left(120 * 1.01)
        tina.forward(i*1.001)
        tina.left(90 * 1.01)
        tina.forward(i*1.001)
        tina.left(60 * 1.01)
shape_spiral()


turtle.exitonclick()
