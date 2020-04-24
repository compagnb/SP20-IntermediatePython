import turtle
import random

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

invaders = [] 
maxInvaders = 10

for count in range(maxInvaders):
    if count % 2 == 0:
        invaders.append(Invader('red', random.randint(-300, 300),random.randint(-300, 300)))
    else:
        invaders.append(Invader('blue', random.randint(-300, 300),random.randint(-300, 300)))

## infiniate Loop
while True:
    for invader in invaders:
        invader.move()
    
