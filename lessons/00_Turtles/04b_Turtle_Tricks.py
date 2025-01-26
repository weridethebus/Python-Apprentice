
import random
import turtle

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")
window.setup( width = 1450, height = 700, startx = 0, starty = 0)

colors = ("red", "blue", "green", "yellow", "orange")

tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)
tina.width(1)



def shape_spiral():
    tina.penup()
    tina.goto(-100, 100)
    tina.pendown()
    tina.pencolor("blue")
    for i in range(100):
        tina.forward(i*1.1)
        tina.left(120 * 1.01)
    tina.penup()
    tina.goto(100,100)
    tina.pendown()
    tina.pencolor("red")
    for i in range(100):
        tina.forward(i*1.1)
        tina.left(90 * 1.01)
    tina.penup()
    tina.goto(-100,-100)
    tina.pendown()
    tina.pencolor("green")
    for i in range(100):
        tina.forward(i*1.1)
        tina.left(72 * 1.01)
    tina.penup()
    tina.goto(100, -100)
    tina.pendown()
    tina.pencolor("yellow")
    for i in range(100):
        tina.forward(i*1.1)
        tina.left(60 * 1.01)
shape_spiral()


turtle.exitonclick()
