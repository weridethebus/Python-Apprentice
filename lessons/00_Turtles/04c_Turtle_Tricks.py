
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=1450, height=700, starty = 0, startx = 0)    # Set the size of the window
soda = turtle.Turtle()                  # Create a turtle named tina
soda.speed(0)

def slowest_circ():
    for i in range(750):
        soda.forward(i)
        soda.left(i*180.001)

slowest_circ()




turtle.exitonclick()
