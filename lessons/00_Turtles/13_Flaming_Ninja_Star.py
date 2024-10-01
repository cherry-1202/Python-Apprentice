"""Flaming Ninja Star

This program already works; run it to see what it does. 
Then change it to make it draw a different pattern. 
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["pink", "blue", "cyan", "purple", "white"]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup (width=600, height=600) 
window = turtle.Screen()

baseSize = 200  # the size of the black part of the star
flameSize = 100  # the length of the flaming arms

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(90) 

for i in range(150):
    t.pencolor(getRandomColor())

    t.fillcolor(getRandomColor()) 
   
    t.begin_fill()

    t.forward(100) 

    t.left(100) 

    t.forward(flameSize) 

    t.right(200) 

    t.forward(flameSize) 

    t.right(62) 

    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() 

turtle.done() 
