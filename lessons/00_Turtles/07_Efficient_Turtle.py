
tri = 3
rect = 4
pent = 5
hex = 6
hept = 7
oct = 8
nona = 9
deca = 10
sides = tri
angle = 360/sides
i = 0

import turtle
turtle.setup(510, 250, startx = 0, starty = 0)
tina = turtle.Turtle()

def draw_polygon(sides):

    for i in range(1000):
        tina.forward(i*1.25)
        tina.left(angle)
        print("loop iteration", i)
        
        

draw_polygon(sides)

turtle.exitonclick()