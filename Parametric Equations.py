# Parametric Equations
# Josh Bowen
# 12/21/2021

# lets start with basic elipse

import turtle
import math


pi = math.pi
x_radius = 100
y_radius = 50

#create a list of values (fractions of pi) for the turtles x and y functions
values = []
s = 64
for n in range(int(s/2),int(-s/2),-1):
    x = 2*n*pi/(s)
    values.append(x)
values.append(-pi)

#initialize screen
wn = turtle.Screen()
wn.bgcolor("black")

#initialize turtle and start position
trace = turtle.Turtle()
trace.color("white")
trace.speed(1)
trace.up()
trace.goto(x_radius*math.cos(pi),y_radius*math.sin(pi))
trace.down()

#follow list of values and x y funtions to trace
for i in values:
    x = x_radius*math.cos(i)
    y = y_radius*math.sin(i)
    trace.goto(x, y)


    
