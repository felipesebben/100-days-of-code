import turtle as turtle_module
from main import color_list
from random import choice

color_list = [(239, 242, 247), (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91),
              (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89),
              (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22),
              (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162),
              (105, 44, 39), (164, 209, 187), (151, 206, 220)]
turtle_module.colormode(255)
jim = turtle_module.Turtle()
jim.speed('fastest')

jim.hideturtle()
jim.setheading(225)

jim.penup()
jim.forward(300)
jim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    jim.dot(20, choice(color_list))
    jim.penup()
    jim.forward(50)

    if dot_count % 10 == 0:
        jim.setheading(90)
        jim.forward(50)
        jim.setheading(180)
        jim.forward(500)
        jim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
