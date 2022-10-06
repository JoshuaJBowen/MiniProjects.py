# Logarithmic Spiral
# Josh Bowen
# 12/21/2021

# moving onto the log spiral

import turtle
import math

x = 2*math.log(math.pi)
print(x)


pi = math.pi
radius = 10

#create a list of values (fractions of pi) for the turtles x and y functions??
values = []
s = 8
for n in range(int(s/2),int(-s/2),-1):
    x = 2*n*pi/(s)
    values.append(x)
values.append(-pi)

wn = turtle.Screen()
wn.bgcolor("black")

trace = turtle.Turtle()
trace.color("white")
trace.speed(1)
trace.up()
trace.goto(radius*math.cos(pi),radius*math.sin(pi))
trace.down()


for i in values:
    x = radius*(math.log(i))
    y = radius*math.sqrt(abs(i))
    trace.goto(x, y)
    


    
