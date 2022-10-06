#RecursiveShapes.py
#Josh Bowen
#5/20/2021

def drawpoly(num_side, len_side, red, green, blue, tur):
    turn = 360/num_side
    if red > 255:
        red = 255
    if red < 0:
        red = 0
    if blue > 255:
        blue = 255
    if blue < 0:
        blue = 0
    if green > 255:
        green = 255
    if green < 0:
        green = 0
    
    tur.fillcolor(red,green,blue)
    tur.begin_fill()
    for n in range(num_side):
        tur.fd(len_side)
        tur.left(turn)
    tur.end_fill()
    if num_side > 2:
        drawpoly(num_side-1, len_side, red+10, green+25, blue+35, tur)
    tur.ht()

def main():

    Red = int(input("How much red do you want to start with?"))
    Green = int(input("How much green do you want to start with?"))
    Blue = int(input("How much blue do you want to start with?"))
    Sides = int(input("How many sides do you want to start with?"))
    Length = int(input("How long do you want your sides?"))
    
    import turtle

    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor("magenta")

    jake = turtle.Turtle()
    jake.speed(0)
    jake.color("black")

    drawpoly(Sides, Length, Red, Green, Blue, jake)
    
main()

