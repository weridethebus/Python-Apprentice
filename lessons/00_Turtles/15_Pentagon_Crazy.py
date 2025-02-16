"""
Pentagon Crazy

This program already works. Run it, then change it to make it draw a different pattern.
"""

import random
import turtle

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")
window.setup( width = 1450, height = 700, startx = 0, starty = 0)

colors = ("red", "orange", "yellow", "chartreuse", "green", "cyan", "blue", "indigo", "purple")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(0)
myTurtle.width(1)

sides = 3

angle = 360 / sides

myTurtle.hideturtle()

for i in range(999999999999999999999999999999999999999999999999):
    if i == 100:
        myTurtle.width(2)
    if i == 200:
        myTurtle.width(3)
    myTurtle.pencolor(getNextColor(i))
    myTurtle.forward(i*1)
    myTurtle.right(angle)
    print("iteration number ", i)

myTurtle.hideturtle()

turtle.done()
