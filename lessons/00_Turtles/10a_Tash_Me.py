



import turtle as turtle
screen = turtle.Screen()
screen.setup(width=540, height=250, startx=0, starty=0)
screen.bgcolor('white')

def get_mossed():
    

    

    t1 = turtle.Turtle()
    t1.penup()
    t1.shape("turtle")

    t2 = turtle.Turtle()
    t2.penup()
    t2.shape("arrow")
    
    t2. goto(200,1)
    t1. goto(200,50)
    t2. goto(-200, 70)
    t1. goto(-200, 100)
    t2. goto(200, 100)
    print("That turtle got mossed!")

get_mossed()



turtle.exitonclick()