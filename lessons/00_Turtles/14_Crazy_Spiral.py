import turtle as turtle
turtle.setup( width = 1450, height = 700, startx = 0, starty = 0)
rootbeer = turtle.Turtle()
rootbeer.speed(0)

sides = 3
angle = 360/sides

def crazy_spiral():
    for i in range(360):
        print("loop iteration", i)
        rootbeer.forward (i*1.00000000001)
        rootbeer.left(angle + 0.0625)


crazy_spiral()

turtle.exitonclick()