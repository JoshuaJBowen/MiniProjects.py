# Cool_Shape.py

#Josh Bowen

#3/2/2021

import turtle

bgcolor = input("What color would you like your background to be?  ")
pencolor = input("What color would you like your pen to be?  ")
pensize = int(input("What size would you like your pen to be? (numbers only)  "))

screen = turtle.Screen()
turtle = turtle. Turtle()

turtle.speed(0)
screen.bgcolor(bgcolor)
turtle.color(pencolor)
turtle.pensize(pensize)
turtle.shape("turtle")

#for m in range(1,9):
 #   turtle.forward(-33.5)
for n in range(360):
    if n < 180:
        turtle.color(pencolor)
        turtle.forward(35)
        turtle.right(1440-n)
    else:
        turtle.color(bgcolor)
        turtle.forward(35)
        turtle.right(1440-n)
#    turtle.home()
 #   turtle.right(m*180/8)

screen.exitonclick()

