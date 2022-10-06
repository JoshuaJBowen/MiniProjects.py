# Four Bugs
# Josh Bowen
# 12/23/2021


dispx = 100#int(input("what would you like your initial x displacement to be?  "))
dispy = 100#int(input("what would you like your initial y displacement to be?  "))

scale = 1
change = 1/scale

import turtle

wn = turtle.Screen()
wn.setworldcoordinates(-100,-100,100,100)

A = turtle.Turtle()
B = turtle.Turtle()
C = turtle.Turtle()
D = turtle.Turtle()

A.speed(0)
A.up()
A.goto(dispx, dispy)
A.seth(181)
A.down()

B.speed(0)
B.up()
B.goto(-dispx, dispy)
B.seth(270)
B.down()

C.speed(0)
C.up()
C.goto(-dispx, -dispy)
C.seth(0)
C.down()

D.speed(0)
D.up()
D.goto(dispx, -dispy)
D.seth(90)
D.down()

changex = 0
changey = 0

for i in range(300*scale):
    A.fd(change)
    B.fd(change)
    C.fd(change)
    D.fd(change)
    A.seth(A.towards(B.xcor(), B.ycor()))
    B.seth(B.towards(C.xcor(), C.ycor()))
    C.seth(C.towards(D.xcor(), D.ycor()))
    D.seth(D.towards(A.xcor(), A.ycor()))

    if i == 100*scale:
        wn.setworldcoordinates(-75,-75,75,75)

    if i == 125*scale:
        wn.setworldcoordinates(-50,-50,50,50)

    if i == 175*scale:
        wn.setworldcoordinates(-25,-25,25,25)

    if i == 225*scale:
        wn.setworldcoordinates(-10,-10,10,10)

wn.setworldcoordinates(-25,-25,25,25)
one = input("")
wn.setworldcoordinates(-50,-50,50,50)
two = input("")
wn.setworldcoordinates(-75,-75,75,75)
three = input("")
wn.setworldcoordinates(-100,-100,100,100)
four = input("")
wn.setworldcoordinates(-125,-125,125,125)
    #wn.setworldcoordinates(-dispx + changex, -dispy + changey, dispx - changex, dispy - changey)
    #changex = changex + 1
    #changey = changey + 1
