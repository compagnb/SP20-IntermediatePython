import turtle
import random
maxVelocity = 10

## Player
class Player(turtle.Turtle):
                def __init__(self, plColor, plShape):
                                 turtle.Turtle.__init__(self)
                                 self.up()
                                 self.speed(0)
                                 self.color(plColor)
                                 self.shape(plShape)
                                 self.velocity = 1
                def move(self):
                                self.forward(self.velocity)
                def turnLeft(self):
                                self.left(30)
                def turnRight(self):
                                self.right(30)
                def speedUp(self):
                               if self.velocity >= maxVelocity:
                                               self.Velocity = maxVelocity
                                else:
                                                self.velocity= self.velocity +1
                def slowdown(self):
                                if self.velocity <= 0:
                                                self.velocity=0
                                else: 
                                                self.velocity=self.velocity -1
                                
                                 


logan = Player("blue", "square")



                    

## Space Invader
class Invader(turtle.Turtle):
    def __init__(self, color, xPos, yPos):
        turtle.Turtle.__init__(self)
        self.color(str(color))
        self.up()
        self.goto(xPos, yPos);
        self.speed(0)
    def move(self):
        self.forward(1)
    def shoot(self):
        pass
    

## Quidditch
class teamPlayer(turtle.Turtle):
    def __init__(self, color, xPos, yPos):
        turtle.Turtle.__init__(self)
        self.color(str(color))
        self.up()
        self.goto(xPos, yPos);
    def move(self):
        pass
    def shoot(self):
        pass
