import turtle
turtle.setup(525, 250, startx = 0, starty = 0)
tina = turtle.Turtle()
tina.speed(1000000000000000000000000000000000000000000)

def circle_fractal():
    for i in range(10000000000000000000000000000000000000000000000000000000000000000000):
        print("loop iteration", i)
        tina.pencolor("orange")
        tina.circle(i*0.9999999999999999999999999999999999999999999999999999999999999999999999999999999)

circle_fractal()

turtle.exitonclick()