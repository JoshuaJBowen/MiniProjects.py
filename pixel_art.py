#pixel_art
#Josh Bowen
#3/26/2021

import turtle

wn = turtle.Screen()
wn.setup(width=450, height=450, startx=None, starty=None)
wn.bgcolor("yellow")


pic = turtle.Turtle()
pic.ht()
pic.speed(0)

def pix(x, y, color, turtle):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color("black", color)
    turtle.begin_fill()
    for s in range(4):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()

def nose(x,y,color, turtle):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    for s in range(36):
        turtle.forward(1)
        turtle.left(10)
    turtle.end_fill()


for n in range(4):
    pix(-200+n*10, -200, "green", pic)
for n in range(5):
    pix(-160+n*10, -200, "white", pic)
for n in range(11):
    pix(-110+n*10, -200, "green", pic)
for n in range(5):
    pix(0+n*10, -200, "white", pic)
for n in range(15):
    pix(50+n*10, -200, "green", pic)

    
for n in range(4):
    pix(-200+n*10, -190, "green", pic)
for n in range(5):
    pix(-160+n*10, -190, "white", pic)
for n in range(2):
    pix(-110+n*10,-190, "green", pic)
for n in range(6):
    pix(-90+n*10, -190, "pink", pic)
for n in range(3):
    pix(-30+n*10, -190, "green", pic)
for n in range(5):
    pix(0+n*10, -190, "white", pic)
for n in range(15):
    pix(50+n*10, -190, "green", pic)

    
for n in range(4):
    pix(-200+n*10, -180, "green", pic)
for n in range(6):
    pix(-160+n*10, -180, "white", pic)
for n in range(8):
    pix(-100+n*10, -180, "pink", pic)
for n in range(7):
    pix(-20+n*10, -180, "white", pic)
for n in range(15):
    pix(50+n*10, -180, "green", pic)


for n in range(4):
    pix(-200+n*10, -170, "green", pic)
for n in range(3):
    pix(-160+n*10, -170, "brown", pic)
for n in range(18):
    pix(-130+n*10, -170, "white", pic)
for n in range(15):
    pix(50+n*10, -170, "green", pic)

    
for n in range(4):
    pix(-200+n*10, -160, "green", pic)
for n in range(5):
    pix(-160+n*10, -160, "brown", pic)
for n in range(14):
    pix(-110+n*10, -160, "white", pic)
for n in range(2):
    pix(30+n*10, -160, "brown", pic)
for n in range(15):
    pix(50+n*10, -160, "green", pic)


for n in range(4):
    pix(-200+n*10, -150, "skyblue", pic)
for n in range(6):
    pix(-160+n*10, -150, "brown", pic)
for n in range(3):
    pix(-100+n*10, -150, "white", pic)
for n in range(3):
    pix(-70+n*10, -150, "brown", pic)
for n in range(5):
    pix(-40+n*10, -150, "white", pic)
for n in range(4):
    pix(10+n*10, -150, "brown", pic)
for n in range(15):
    pix(50+n*10, -150, "skyblue", pic)
    

for n in range(4):
    pix(-200+n*10, -140, "skyblue", pic)
for n in range(6):
    pix(-160+n*10, -140, "brown", pic)
for n in range(3):
    pix(-100+n*10, -140, "white", pic)
for n in range(4):
    pix(-70+n*10, -140, "brown", pic)
for n in range(3):
    pix(-30+n*10, -140, "white", pic)
for n in range(5):
    pix(0+n*10, -140, "brown", pic)
for n in range(15):
    pix(50+n*10, -140, "skyblue", pic)


for n in range(4):
    pix(-200+n*10, -130, "skyblue", pic)
for n in range(5):
    pix(-160+n*10, -130, "brown", pic)
for n in range(5):
    pix(-110+n*10, -130, "white", pic)
for n in range(3):
    pix(-60+n*10, -130, "brown", pic)
for n in range(3):
    pix(-30+n*10, -130, "white", pic)
for n in range(5):
    pix(0+n*10, -130, "brown", pic)
for n in range(15):
    pix(50+n*10, -130, "skyblue", pic)


for n in range(4):
    pix(-200+n*10, -120, "skyblue", pic)
for n in range(3):
    pix(-160+n*10, -120, "brown", pic)
for n in range(12):
    pix(-130+n*10, -120, "white", pic)
for n in range(6):
    pix(-10+n*10, -120, "brown", pic)
for n in range(15):
    pix(50+n*10, -120, "skyblue", pic)


for n in range(4):
    pix(-200+n*10, -110, "skyblue", pic)
for n in range(16):
    pix(-160+n*10, -110, "white", pic)
for n in range(2):
    pix(0+n*10, -110, "brown", pic)
for n in range(10):
    pix(20+n*10, -110, "pink", pic)
for n in range(8):
    pix(120+n*10, -110, "skyblue", pic)


pix(-200, -100, "skyblue", pic)
for n in range(6):
    pix(-190+n*10, -100, "white", pic)
for n in range(5):
    pix(-130+n*10, -100, "brown", pic)
for n in range(7):
    pix(-80+n*10, -100, "white", pic)
for n in range(16):
    pix(-10+n*10, -100, "pink", pic)
for n in range(5):
    pix(150+n*10, -100, "skyblue", pic)


for n in range(2):
    pix(-200+n*10, -90, "white", pic)
for n in range(2):
    pix(-180+n*10, -90, "skyblue", pic)
for n in range(9):
    pix(-160+n*10, -90, "brown", pic)
for n in range(5):
    pix(-70+n*10, -90, "white", pic)
for n in range(18):
    pix(-20+n*10, -90, "pink", pic)
for n in range(4):
    pix(160+n*10, -90, "skyblue", pic)




pix(-200, -80, "white", pic)
for n in range(4):
    pix(-190+n*10, -80, "skyblue", pic)
for n in range(11):
    pix(-150+n*10, -80, "brown", pic)
pix(-40, -80, "white", pic)
for n in range(20):
    pix(-30+n*10, -80, "pink", pic)
for n in range(3):
    pix(170+n*10, -80, "skyblue", pic)


pix(-200, -70, "white", pic)
for n in range(3):
    pix(-190+n*10, -70, "brown", pic)
for n in range(2):
    pix(-160+n*10, -70, "skyblue", pic)
for n in range(11):
    pix(-140+n*10, -70, "brown", pic)
for n in range(20):
    pix(-30+n*10, -70, "pink", pic)
for n in range(3):
    pix(170+n*10, -70, "skyblue", pic)


for n in range(5):
    pix(-200+n*10, -60, "brown", pic)
for n in range(3):
    pix(-150+n*10, -60, "skyblue", pic)
for n in range(9):
    pix(-120+n*10, -60, "brown", pic)
pix(-30, -60, "white", pic)
for n in range(18):
    pix(-20+n*10, -60, "pink", pic)
pix(160, -60, "white", pic)
for n in range(3):
    pix(170+n*10, -60, "skyblue", pic)


for n in range(5):
    pix(-200+n*10, -50, "brown", pic)
for n in range(12):
    pix(-150+n*10, -50, "skyblue", pic)
for n in range(3):
    pix(-30+n*10, -50, "white", pic)
for n in range(14):
    pix(0+n*10, -50, "pink", pic)
for n in range(3):
    pix(140+n*10, -50, "white", pic)
for n in range(3):
    pix(170+n*10, -50, "skyblue", pic)


pix(-200, -40, "skyblue", pic)
for n in range(4):
    pix(-190+n*10, -40, "brown", pic)
for n in range(12):
    pix(-150+n*10, -40, "skyblue", pic)
for n in range(6):
    pix(-30+n*10, -40, "white", pic)
for n in range(8):
    pix(30+n*10, -40, "pink", pic)
for n in range(6):
    pix(110+n*10, -40, "white", pic)
for n in range(3):
    pix(170+n*10, -40, "skyblue", pic)


for n in range(4):
    pix(-200+n*10, -30, "skyblue", pic)
pix(-160, -30, "brown", pic)
for n in range(13):
    pix(-150+n*10, -30, "skyblue", pic)
for n in range(4):
    pix(-20+n*10, -30, "white", pic)
pix(20, -30, "black", pic)
for n in range(8):
    pix(30+n*10, -30, "white", pic)
pix(110, -30, "black", pic)
for n in range(4):
    pix(120+n*10, -30, "white", pic)
for n in range(4):
    pix(160+n*10, -30, "skyblue", pic)


for n in range(18):
    pix(-200+n*10, -20, "skyblue", pic)
for n in range(4):
    pix(-20+n*10, -20, "white", pic)
pix(20, -20, "black", pic)
for n in range(8):
    pix(30+n*10, -20, "white", pic)
pix(110, -20, "black", pic)
for n in range(4):
    pix(120+n*10, -20, "white", pic)
for n in range(4):
    pix(160+n*10, -20, "skyblue", pic)


for n in range(19):
    pix(-200+n*10, -10, "skyblue", pic)
for n in range(3):
    pix(-10+n*10, -10, "white", pic)
pix(20, -10, "black", pic)
for n in range(8):
    pix(30+n*10, -10, "white", pic)
pix(110, -10, "black", pic)
for n in range(3):
    pix(120+n*10, -10, "white", pic)
for n in range(5):
    pix(150+n*10, -10, "skyblue", pic)


for n in range(19):
    pix(-200+n*10, 0, "skyblue", pic)
for n in range(16):
    pix(-10+n*10, 0, "white", pic)
for n in range(5):
    pix(150+n*10, 0, "skyblue", pic)


for n in range(20):
    pix(-200+n*10, 10, "skyblue", pic)
for n in range(9):
    pix(0+n*10, 10, "white", pic)
for n in range(5):
    pix(90+n*10, 10, "brown", pic)
for n in range(6):
    pix(140+n*10, 10, "skyblue", pic)


for n in range(20):
    pix(-200+n*10, 20, "skyblue", pic)
for n in range(8):
    pix(0+n*10, 20, "white", pic)
for n in range(6):
    pix(80+n*10, 20, "brown", pic)
for n in range(6):
    pix(140+n*10, 20, "skyblue", pic)


for n in range(17):
    pix(-200+n*10, 30, "skyblue", pic)
for n in range(3):
    pix(-30+n*10, 30, "brown", pic)
for n in range(6):
    pix(0+n*10, 30, "white", pic)
for n in range(11):
    pix(60+n*10, 30, "brown", pic)
for n in range(3):
    pix(170+n*10, 30, "skyblue", pic)


for n in range(16):
    pix(-200+n*10, 40, "skyblue", pic)
for n in range(5):
    pix(-40+n*10, 40, "brown", pic)
for n in range(5):
    pix(10+n*10, 40, "white", pic)
for n in range(12):
    pix(60+n*10, 40, "brown", pic)
for n in range(2):
    pix(180+n*10, 40, "skyblue", pic)


for n in range(16):
    pix(-200+n*10, 50, "skyblue", pic)
for n in range(5):
    pix(-40+n*10, 50, "brown", pic)
for n in range(5):
    pix(10+n*10, 50, "white", pic)
for n in range(12):
    pix(60+n*10, 50, "brown", pic)
for n in range(2):
    pix(180+n*10, 50, "skyblue", pic)


for n in range(22):
    pix(-200+n*10, 60, "skyblue", pic)
for n in range(4):
    pix(20+n*10, 60, "white", pic)
for n in range(5):
    pix(60+n*10, 60, "brown", pic)
for n in range(9):
    pix(110+n*10, 60, "skyblue", pic)


for n in range(24):
    pix(-200+n*10, 70, "skyblue", pic)
for n in range(6):
    pix(40+n*10, 70, "white", pic)
for n in range(10):
    pix(100+n*10, 70, "skyblue", pic)


for i in range(13):
    for n in range(40):
        pix(-200+n*10, 80+i*10, "skyblue", pic)


nose(30, -75, "black", pic)
nose(110, -75, "black", pic)
