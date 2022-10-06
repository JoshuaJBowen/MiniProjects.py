#Bounce.py
#Josh Bowen
#3/11/2021

import turtle
import random

wn = turtle.Screen()
bro = turtle.Turtle()
bro.speed(5)
bro.width(1)

jake = turtle.Turtle()
jake.speed(5)
jake.width(1)

bro.up()
bro.goto(300,-300)
bro.down()
for n in range(4):
    bro.left(90)
    bro.forward(600)
bro.up()
bro.home()
bro.down()

while abs(float(bro.xcor()))< 300.0 and abs(float(bro.ycor()))<300 and abs(float(jake.xcor()))< 300.0 and abs(float(jake.ycor()))<300:
    choice = random.randint(0,4)
    if choice == 1:
        #bro.begin_fill()
        bro.right(90)#(random.randrange(180))
        if abs(bro.xcor()) > abs(bro.ycor()):
            go = int((299 - abs(bro.xcor()))/(2**.5))
            print(go, bro.xcor())
            if go != 0:
                bro.forward(random.randrange(-go,go))
            else:
                bro.up()#bro.goto(random.randrange(-300,300),random.randrange(-300,300))
                bro.home() #bro.stamp()
                bro.down()
        else:
            Go = int((299 - abs(bro.ycor()))/(2**.5))
            print(Go, bro.ycor())
            if Go != 0:
                bro.forward(random.randrange(-Go,Go))
            else:
                bro.up()#bro.goto(random.randrange(-300,300),random.randrange(-300,300))
                bro.home() #bro.stamp()
                bro.down()
    elif choice == 2:
        #bro.begin_fill()
        bro.left(90)#(random.randrange(180))
        if abs(bro.xcor()) > abs(bro.ycor()):
            go = int((299 - abs(bro.xcor()))/(2**.5))
            print(go, bro.xcor())
            if go != 0:
                bro.forward(random.randrange(-go,go))
            else:
                bro.up()#bro.goto(random.randrange(-300,300),random.randrange(-300,300))
                bro.home() #bro.stamp()
                bro.down()
        else:
            Go = int((299 - abs(bro.ycor()))/(2**.5))
            print(Go, bro.ycor())
            if Go != 0:
                bro.forward(random.randrange(-Go,Go))
            else:
                bro.up()#bro.goto(random.randrange(-300,300),random.randrange(-300,300))
                bro.home() #bro.stamp()
                bro.down()
        
    else:
        #bro.end_fill()
        if abs(bro.xcor()) > abs(bro.ycor()):
            go = int((299 - abs(bro.xcor()))/(2**.5))
            print(go, bro.xcor())
            if go != 0:
                bro.forward(random.randrange(-go,go))
            else:
                bro.up()#bro.goto(random.randrange(-300,300),random.randrange(-300,300))
                bro.home() #bro.stamp()
                bro.down()
        else:
            Go = int((299 - abs(bro.ycor()))/(2**.5))
            print(Go, bro.ycor())
            if Go != 0:
                bro.forward(random.randrange(-Go,Go))
            else:
                bro.up()#bro.goto(random.randrange(-300,300),random.randrange(-300,300))
                bro.home() #bro.stamp()
                bro.down()
    Choice = random.randint(0,4)
    if Choice == 1:
        #jake.begin_fill()
        jake.right(90)#(random.randrange(180))
        if abs(jake.xcor()) > abs(jake.ycor()):
            go = int((299 - abs(jake.xcor()))/(2**.5))
            print(go, jake.xcor())
            if go != 0:
                jake.forward(random.randrange(-go,go))
            else:
                jake.up()#jake.goto(random.randrange(-300,300),random.randrange(-300,300))
                jake.home()#jake.stamp()
                jake.down()
        else:
            Go = int((299 - abs(jake.ycor()))/(2**.5))
            print(Go, jake.ycor())
            if Go != 0:
                jake.forward(random.randrange(-Go,Go))
            else:
                jake.up()#jake.goto(random.randrange(-300,300),random.randrange(-300,300))
                jake.home()#jake.stamp()
                jake.down()
    elif Choice == 2:
        #jake.begin_fill()
        jake.left(90)#(random.randrange(180))
        if abs(jake.xcor()) > abs(jake.ycor()):
            go = int((299 - abs(jake.xcor()))/(2**.5))
            print(go, jake.xcor())
            if go != 0:
                jake.forward(random.randrange(-go,go))
            else:
                jake.up()#jake.goto(random.randrange(-300,300),random.randrange(-300,300))
                jake.home()#jake.stamp()
                jake.down()
        else:
            Go = int((299 - abs(jake.ycor()))/(2**.5))
            print(Go, jake.ycor())
            if Go != 0:
                jake.forward(random.randrange(-Go,Go))
            else:
                jake.up()#jake.goto(random.randrange(-300,300),random.randrange(-300,300))
                jake.home()#jake.stamp()
                jake.down()
    else:
        #jake.end_fill()
        if abs(jake.xcor()) > abs(jake.ycor()):
            go = int((299 - abs(jake.xcor()))/(2**.5))
            print(go, jake.xcor())
            if go != 0:
                jake.forward(random.randrange(-go,go))
            else:
                jake.up()#jake.goto(random.randrange(-300,300),random.randrange(-300,300))
                jake.home()#jake.stamp()
                jake.down()
        else:
            Go = int((299 - abs(jake.ycor()))/(2**.5))
            print(Go, jake.ycor())
            if Go != 0:
                jake.forward(random.randrange(-Go,Go))
            else:
                jake.up()#jake.goto(random.randrange(-300,300),random.randrange(-300,300))
                jake.home()#jake.stamp()
                jake.down()
                


