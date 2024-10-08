"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')
tina.speed(2)

tina.pencolor('blue')
tina.left(180)

tina.pencolor('red')
tina.forward(100)
tina.right(72)

tina.pencolor('purple')
tina.forward(100)
tina.right(72)

tina.pencolor('green')
tina.forward(100)
tina.right(72)

tina.pencolor('yellow')
tina.forward(100)
tina.right(72)

tina.pencolor('black')
tina.forward(100)
tina.right(72)




# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here

turtle.exitonclick()                    # Close the window when we click on it
