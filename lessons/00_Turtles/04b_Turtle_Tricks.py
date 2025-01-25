
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=1450, height=700, starty = 0, startx = 0)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(0)



def shape_spiral():
    for i in range(100):
        tina.forward(i*1.1)
        tina.left(120 * 1.01)
    tina.penup()
    tina.goto(0,0)
    tina.pendown()
    for i in range(200):
        tina.forward(i*1.1)
        tina.left(90 * 1.01)
    tina.penup()
    tina.goto(0,0)
    tina.pendown()
    for i in range(300):
        tina.forward(i*1.1)
        tina.left(72 * 1.01)
    tina.penup()
    tina.goto(0,0)
    tina.pendown()
    for i in range(400):
        tina.forward(i*1.1)
        tina.left(60 * 1.01)
shape_spiral()


turtle.exitonclick()
