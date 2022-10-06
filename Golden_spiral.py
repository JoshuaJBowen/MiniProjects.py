#Golden_spiral.py

#Josh Bowen

#2/22/2021

import turtle

range_ = int(input("how many lines do you want?"))
loops = 3
cool = turtle.Turtle()
cool.speed(0)

for number in range(1,(range_+1)):
    turtle_number = turtle.Turtle()
    turtle_number.ht()
    turtle_number.speed(0)
    turtle_number.right(360*number*loops/range_)
    turtle_number.forward(360*number/range_)
    cool.goto(turtle_number.position())
    #turtle_number.color("white")
    #turtle_number.forward(-(375/range_*(number+1)))
    

