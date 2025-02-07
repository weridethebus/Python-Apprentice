import turtle
turtle.setup(1375, 750, startx = 0, starty = 0)
tina = turtle.Turtle()
tina.speed(000000000000000000000000000000000000000000)

tina.penup()
tina.goto(0, -375)
tina.pendown()

def circle_fractal():
    for i in range(10000000000000000000000000000000000000000000000000000000000000000000):
        print("loop iteration", i)
        tina.pencolor("orange")
        tina.circle(i*0.9999999999999999999999999999999999999999999999999999999999999999999999999999999)

circle_fractal()

turtle.exitonclick()