
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here

import turtle

turtle.setup (width=600, height=600, startx = 0, starty = 0)

tina = turtle.Turtle()                  


i = 0

for i in range(50):
    print('loop iteration', i)
    tina.forward(i * 2.25)
    tina.left(72)

turtle.exitonclick() 