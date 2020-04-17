import turtle

def drawSquare(t1, x, y, length, filled):
      t1.up()
      t1.goto(x,y)
      t1.down()
      if filled == True:
            t1.begin_fill()
      for x in range(0,4):
            t1.forward(length)
            t1.right(90)
      if filled == True:
            t1.end_fill()                      
                        
def drawCircle(t1, x, y, diameter, filled):
      t1.up()
      t1.goto(x,y)
      t1.down()
      if t1 == True:
            t1.begin_fill()
      t1.circle(diameter)
      if filled == True:
            t1.end_fill()

def drawStar(t1, x, y, length, points, filled):
      t1.up()
      t1.goto(x,y)
      t1.down()
      if filled == True:
            t1.begin_fill()
      for x in range(points):
            t1.forward(length)
            if x % 2 == 0:
                  t1.left(175)
            else:
                  t1.left(225)
      if filled == True:
            t1.end_fill() 



rectTurtle = turtle.Pen()
rectTurtle.color("red")

circleTurtle = turtle.Pen()
circleTurtle.color("#00FF00")

starTurtle = turtle.Pen()
starTurtle.color("blue")

drawSquare(rectTurtle, 100,0, 100, True)
drawCircle(circleTurtle, 0,100, 100, True)
drawStar(starTurtle, 0, 0, 100, 19, True)



