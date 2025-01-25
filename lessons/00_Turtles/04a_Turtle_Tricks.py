
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=1450, height=700, starty = 0, startx = 0)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(0)



def scorpion_tail():
    for i in range(500):
        tina.forward(i*1.01)
        tina.left(120 *1.01)
        tina.forward(i*1.01)
        tina.left(90 * 1.01)
        tina.forward(i*1.01)
        tina.left(72 * 1.01)
        tina.forward(i*1.01)
        tina.left(60 * 1.01)

scorpion_tail()

turtle.exitonclick()