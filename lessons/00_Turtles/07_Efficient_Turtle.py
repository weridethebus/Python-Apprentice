
tri = 3
rect = 4
pent = 5
hex = 6
hept = 7
oct = 8
nona = 9
deca = 10
sides = pent
angle = 360/sides
i = 0

import turtle
turtle.setup(height = 600, width  = 1450, startx = 0, starty = 0)
tina = turtle.Turtle()
tina.speed(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

def draw_polygon(sides):

    for i in range(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        tina.forward(i*1.30)
        tina.left(angle)
        print("loop iteration", i)
        
        

draw_polygon(sides)

turtle.exitonclick()