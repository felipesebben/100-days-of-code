# import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen
from prettytable import PrettyTable

jimmy = Turtle()
print(jimmy)
jimmy.shape('turtle')  # Changes Jimmy's shape into a turtle
jimmy.color('blue')
jimmy.forward(100)  # Make Jimmy move forward by 100 paces.
# Prints an actual object. What can we do with it?
# We can access its attributes - i.e., what it has.
# Screen object - represents window in which the turtle will show up.

my_screen = Screen()
# print(my_screen.canvheight)
# Printed the height (300) of the canvas for the created screen.
# Screen is the object, while height is its attribute.

# Methods are things the object can do. Basically, they are functions associated to real-life
# Representations, ie. objects.
# my_screen.exitonclick()  # Will allow the program to continue running until clicking on screen.

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'], align='l')
table.add_column('Type', ['Electric', 'Water', 'Fire'], align='l')
print(table)
