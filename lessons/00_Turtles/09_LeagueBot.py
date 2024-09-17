""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()

import turtle

t.penup()
t.shape("turtle")
t.color('blue')


sides=6
angle=360/sides
for i in range(sides):
    t.pendown()
    t.forward(50)
    t.left(angle)



turtle.exitonclick()   
