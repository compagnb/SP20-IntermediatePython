import turtle

class Shapes(turtle.Turtle):
            def __init__(self, rColor, bColor, gColor):
                        turtle.Turtle.__init__(self)
                        self.color(rColor, bColor, gColor)

            def drawSquare(self, x, y, length, filled):
                        self.up()
                        self.goto(x,y)
                        self.down()
                        if filled == True:
                                    self.begin_fill()
                        for x in range(0,4):
                                    self.forward(length)
                                    self.right(90)
                        if filled == True:
                                    self.end_fill()                      
                        
            def drawCircle(self, x, y, diameter, filled):
                        self.goto(x,y)
                        if filled == True:
                                    self.begin_fill()
                        self.circle(diameter)
                        if filled == True:
                                    self.end_fill()

            def drawStar(self, x, y, length, points, filled):
                        self.up()
                        self.goto(x,y)
                        self.down()
                        if filled == True:
                                    self.begin_fill()
                        for x in range(points):
                                    self.forward(length)
                                    if x % 2 == 0:
                                        self.left(175)
                                    else:
                                        self.left(225)
                        if filled == True:
                                    self.end_fill() 


#squ = Shapes(1, 0, 0)
#squ.drawSquare(100,0, 100, True)
#squ.drawSquare(0,100, 100, True)
#squ.drawStar(0, 0, 100, 19, True)



