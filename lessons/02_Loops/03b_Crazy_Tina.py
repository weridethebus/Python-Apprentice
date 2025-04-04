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


forwards = [43,74,55,67,85]
lefts = [17,67,57,100,67]
colors = ["red", "teal", "yellow", "black", "indigo"]

for i in range(5):
    tina.color(colors[i])
    tina.forward(forwards[i])
    tina.left(lefts[i])

turtle.exitonclick()  

