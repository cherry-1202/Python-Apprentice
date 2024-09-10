
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 





sides=4
angle = 360/sides                    
for i in range(sides):
    tina.pendown()
    tina.forward(50)
    tina.left(angle)
                         

sides=5
angle = 360/sides                    
for i in range(sides):
    tina.pendown()
    tina.forward(50)
    tina.left(angle)


sides=6
angle = 360/sides                    
for i in range(sides):
    tina.pendown()
    tina.forward(50)
    tina.left(angle)







turtle.exitonclick()                     # Close the window when we click on it
