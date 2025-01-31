import turtle as turtle
turtle.setup( width = 1375, height = 600, startx = 0, starty = 0)
rootbeer = turtle.Turtle()
rootbeer.speed(250)
rootbeer.speed(100)

whatever = 2


def ninja_star():
    for i in range(10000):
        print("loop iteration", i)
        rootbeer. forward(2)
        rootbeer. left(whatever)


ninja_star()


turtle. exitonclick