import turtle
import random
maxVelocity = 10

## Score
class Score(turtle.Turtle):
    def __init__(self, sColor, bLength, bHeight):
        turtle.Turtle.__init__(self)
        self.color(sColor)
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(bLength/2 -80, bHeight/2 +10)
        self.score =0
    def updateScore(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="left", font=("Neue Display", 14, "normal"))
    def changeScore(self, points):
        self.score = self.score + points
        self.updateScore()
    def playSound(self):
        pass       

## Border
class Border(turtle.Turtle):
    def __init__(self, bColor, bLength, bHeight, bThickness):
        turtle.Turtle.__init__(self)
        self.color(bColor)
        self.pensize(bThickness)
        self.speed(0)
        self.bLength = bLength
        self.bHeight = bHeight
        self.penup()
        self.hideturtle()
    def drawBorder(self):
        self.setposition(-1*self.bLength/2, self.bHeight/2)
        self.pendown()
        for s in range(4):
            if s % 2 == 0:
                self.forward(self.bHeight)  
            else:
                self.forward(self.bLength)
            self.right(90)
            
## Player
class Player(turtle.Turtle):
    ## Player Image!!!
    def __init__(self, plColor, plShape, bLength, bHeight):
        turtle.Turtle.__init__(self)
        self.up()
        self.speed(0)
        self.color(plColor)
        self.shape(plShape)
        self.bLength = bLength
        self.bHeight = bHeight
        self.velocity = 1
    def move(self):
        self.forward(self.velocity)
        #Boundary Check on the X axis
        if self.xcor() > self.bLength/2-10 or self.xcor() < (self.bLength/2-10)*-1:
            self.right(180)
        #Boundary Check on the Y axis
        if self.ycor() > self.bHeight/2-10 or self.ycor() < (self.bHeight/2 -10)*-1:
           self.right(180)                  
    def turnLeft(self):
        self.left(30)
    def turnRight(self):
        self.right(30)
    def speedUp(self):
        if self.velocity >= maxVelocity:
            self.velocity = maxVelocity
        else:
            self.velocity= self.velocity +1
    def slowDown(self):
        if self.velocity <= 0:
            self.velocity=0
        else: 
            self.velocity=self.velocity -1

## Space Invader
class Invader(turtle.Turtle):
    def __init__(self, inColor, inShape, xPos, yPos, bLength, bHeight, inVel):
        turtle.Turtle.__init__(self)
        self.color(inColor)
        self.inColor = inColor
        self.shape(inShape)
        self.bLength = bLength
        self.bHeight = bHeight
        self.up()
        self.goto(xPos, yPos)
        self.speed(0)
        self.setheading(random.randint(0, 360))
        self.velocity = inVel
    def move(self):
        self.forward(1)
        #Boundary Check on the X axis
        if self.xcor() > self.bLength/2-10 or self.xcor() < (self.bLength/2-10)*-1:
            self.right(180)
        #Boundary Check on the Y axis
        if self.ycor() > self.bHeight/2-10 or self.ycor() < (self.bHeight/2 -10)*-1:
           self.right(180) 
    def shoot(self):
        pass
    

## Quidditch
class teamPlayer(turtle.Turtle):
    def __init__(self, inColor, inShape, xPos, yPos, bLength, bHeight, inVel):
        turtle.Turtle.__init__(self)
        self.color(inColor)
        self.shape(inShape)
        self.bLength = bLength
        self.bHeight = bHeight
        self.up()
        self.goto(xPos, yPos)
        self.speed(0)
        self.velocity = inVel
    def move(self):
        self.forward(1)
        #Boundary Check on the X axis
        if self.xcor() > self.bLength/2-10 or self.xcor() < (self.bLength/2-10)*-1:
            self.right(180)
        #Boundary Check on the Y axis
        if self.ycor() > self.bHeight/2-10 or self.ycor() < (self.bHeight/2 -10)*-1:
           self.right(180) 
    def shoot(self):
        pass
