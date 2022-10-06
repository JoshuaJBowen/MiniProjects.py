#RandomWalkingTurtle.py
#Josh Bowen
#4/13/2021

import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
t.speed(0)
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    angle = random.randint(0,6)
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left((angle)*60)
    else:
        t.right((angle)*60)

    t.forward(20)

wn.exitonclick()
