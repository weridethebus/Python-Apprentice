"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 


forwards = [3,4,5,6]
lefts = [7,8,9,100]
colors = ["red", "teal"]

for  i in range(100):

    forward = 21
    left = 88
    color = "red"


    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  

