import turtle
import random
import wk3_gameClass
## import gameClass

# variables that will make our lives easier
bLength = 600
bHeight = 600
maxInvader = 10
maxVelocity = 10
invaders = [ ]

# the instances we are creating! 
wn =  turtle.Screen()
logan = wk3_gameClass.Player("blue","square", bLength, bHeight)
border = wk3_gameClass.Border("blue", bLength, bHeight, 3)

# create instances in an array
#for i in range(maxInvader):
 #   invaders.append(wk3_gameClass.Invader("red", "triangle", random.randint(-290, 290), random.randint(-290, 290), bLength, bHeight, 3))

# all our window stuff
wn.title("Space Invaders!!!")
## Background Images!!!!

# all our border stuff
border.drawBorder()

# all our player control stuff
turtle.listen()
turtle.onkey(logan.turnLeft,"Left")
turtle.onkey(logan.turnRight,"Right")
turtle.onkey(logan.speedUp,"Up")
turtle.onkey(logan.slowDown,"Down")

## this is going to be our game loop.... its never gonna end until we end it!
while True:
    wn.update()
    logan.move()

    
##compagnb@gmail.com
