import turtle as turtle
turtle.setup( width = 1450, height = 700, startx = 0, starty = 0)
rootbeer = turtle.Turtle()
rootbeer.speed(250)

def crazy_spiral():
    for i in range(1000):
        print("loop iteration", i)
        rootbeer.begin_fill()
        rootbeer.forward (i*1.25)
        rootbeer.left(72.1)
        rootbeer.end_fill()


crazy_spiral()

turtle.exitonclick()