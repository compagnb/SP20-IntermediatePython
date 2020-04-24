import turtle
import random

class Shapes(turtle.Turtle):
    def __init__(self, rColor, gColor, bColor):
        turtle.Turtle.__init__(self)
        self.color(rColor, gColor, bColor)

    def drawSquare(self, x, y, length, filled):
        self.up()
        self.goto(x,y)
        self.down()
        if filled == True:
            self.begin_fill()
        for x in range(4):
            self.forward(length)
            self.right(90)
        if filled == True:
            self.end_fill()


s1 = Shapes(1, 0, 1)
s1.drawSquare(100, 100, 200, True)
