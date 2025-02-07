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

colors = ("red", "orange", "yellow", "green", "blue", "indigo", "violet", "magenta")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(0)
myTurtle.width(999999999999999999999999999999999999999999999999)

sides = 4
angle = 360 / sides

for i in range(360):
    if i == 100:
        myTurtle.width(999999999999999999999999999999999999999999999999999999)
    if i == 200:
        myTurtle.width(10099999999999999999999999999999999999999999999999999999)
    myTurtle.pencolor(getNextColor(i))
    myTurtle.forward(i)
    myTurtle.right(angle + 0.1)

myTurtle.hideturtle()

turtle.done()
