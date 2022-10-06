#Clock.py
#Josh Bowen
#3/24/2021

import turtle

desired_time = int(input("How long do you want to time yourself for?"))

turtle.mode("logo")
wn = turtle.Screen()
wn.title("Welcome to my stop watch!")
wn.register_shape("Pointer", ((0,-7), (-5,0), (0,100), (5,0)))

clock = turtle.Turtle()
clock.width(3)
clock.ht()
clock.speed(0)

for n in range(12):
    clock.up()
    clock.forward(110)
    clock.down()
    clock.forward(15)
    clock.up()
    clock.home()
    clock.right((n+1)*30)

tik = turtle.Turtle()
tik.shape("Pointer")
tik.speed(0)

def go():
    n = 1
    time = 0
    while time != desired_time:
        wn.ontimer(tik.seth(n*6), 910) #the vaule 910 is less than one second
        time = time + 1                #Because the computer needs time to compute
        n = n + 1

go()

