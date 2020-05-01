import turtle
import random
import wk3_gameClass
## import gameClass

wn =  turtle.Screen()
wn.title("Space Invaders!!!")
## Background Images!!!!

logan = wk3_gameClass.Player("blue","square")

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
