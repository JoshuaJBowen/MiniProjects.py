#RecursiveTree.py
#Josh Bowen
#5/14/2021

#Please make sure to run this a few times to see the randomness come into play.
#I made the angles random, the branchLen random, the recursive subtracted value random,
#and, for small end pieces, I made the turtle draw thick, green lines to represent leaves.

import turtle
import random

def tree(branchLen,t):
    ang = random.randrange(10,30)
    minus = random.randrange(5,25)
    if branchLen > 5:
        if branchLen < 20:
            t.color("green")
            t.width(4)
        t.forward(branchLen)
        t.right(ang)
        tree(branchLen-minus,t)
        t.left(ang*2)
        tree(branchLen-minus,t)
        t.right(ang)
        if branchLen >= 20:
            t.color("brown")
            t.width(2)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("green")
    t.width(2)
    tree(random.randrange(30,100),t)
    myWin.exitonclick()

main()


