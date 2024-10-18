"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""

import turtle
turtle.setup(width=500, height=500, starx=0, starty=0)

def set_turtle_image(turtle, image_name):
    from pathlib import Path
    image_dir = Path(_file_).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)


screen = turtle.screen()
screen.setup(width = 600, height = 600)

t = turtle.Turtle()

set_turtle_image(t, "emoji.png")

t.penup()
t.speed(3)

for i in range(4):
    t.goto(200, 200)
    t.goto(-200, -200)