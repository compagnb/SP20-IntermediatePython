import turtle
import random
import math
import wk3_gameClass
## import gameClass

# variables that will make our lives easier
bLength = 600
bHeight = 600
maxInvader = 10
maxVelocity = 10
invaders = [ ]
count = 0

# the instances we are creating! 
wn =  turtle.Screen()
wn.bgcolor("grey")
# Background pictures should be gifs & pngs
# wn.bgpic("")
wn.tracer(0)
logan = wk3_gameClass.Player("blue","square", bLength, bHeight)
border = wk3_gameClass.Border("blue", bLength, bHeight, 3)
scoreObj = wk3_gameClass.Score("blue", bLength, bHeight)

# create instances in an array
for i in range(maxInvader):
    if count %2 == 0:
        invaders.append(wk3_gameClass.Invader("red", "triangle", random.randint(-290, 290), random.randint(-290, 290), bLength, bHeight, 3))
    else:
        invaders.append(wk3_gameClass.Invader("purple", "triangle", random.randint(-290, 290), random.randint(-290, 290), bLength, bHeight, 3))
    count= count +1
    
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

# all our collision detection stuff
# a2 +b2 = c2
def isCollision(t1, t2):
    a = t1.ycor() - t2.ycor()
    b = t1.xcor() - t2.xcor()
    aSquared = math.pow(a, 2)
    bSquared = math.pow(b, 2)
    cSquared = aSquared + bSquared
    c= math.sqrt(cSquared)
    if  c < 20:
        # there is a collision!!!
        return True
    else:
        # there is no collision!!!!!
        return False


## this is going to be our game loop.... its never gonna end until we end it!
while True:
    wn.update()

    logan.move()

    for invader in invaders:
        invader.move()
        
        if isCollision(logan, invader):
            # if isCollision is true do this!
            # logan.setposition(0,0)
            invader.setposition(random.randint(-290, 290),random.randint(-290, 290))
            if invader.inColor == "purple":
                scoreObj.changeScore(100)
            else:
               scoreObj.changeScore(10)               









    




    
##compagnb@gmail.com
