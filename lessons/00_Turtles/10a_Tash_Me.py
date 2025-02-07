
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=1450, height=700, starty = 0, startx = 0)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(0)

def loading_screen():
    for i in range(10000000000000000000):
        tina.forward(1)
        tina.left(1)


loading_screen()

turtle.exitonclick()