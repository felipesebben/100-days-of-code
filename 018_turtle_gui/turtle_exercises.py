import turtle as t
import random

jim = t.Turtle()
t.colormode(255)
t.bgcolor('black')
jim.pensize(2)
jim.shape('turtle')
jim.color('midnight blue')
jim.speed('fastest')


def random_pencolor():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


colors = ['white smoke', 'gainsboro', 'dim gray', 'black', 'dodger blue', 'spring green', 'cyan',
          'lime green', 'dark green', 'lime', 'medium spring green', 'dark red', 'rosy brown',
          'dark orchid', 'dark magenta', 'purple', 'red', 'orange', 'sandy brown']


# Make Jim draw a square with a for loop.
# for _ in range(4):
#     jim.forward(100)
#     jim.right(90)


# Make Jim draw a dashed line.
# for _ in range(15):
#     jim.pencolor('blue')
#     jim.forward(10)
#     jim.pencolor('white')
#     jim.forward(10)


# def draw_shapes(shp1, shp_n):
#     angles = 360 / shp1
#     while not shp1 == shp_n:
#         random_pencolor()
#         for _ in range(shp1):
#             jim.forward(100)
#             jim.right(angles)
#         shp1 += 1
#
#
# draw_shapes(3, 10)

# Draw a random walk
# directions = [0, 90, 180, 270]


# for _ in range(200):
#     jim.color(random_pencolor())
#     jim.forward(30)
#     jim.setheading(random.choice(directions))

# Draw a spirograph.
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        jim.color(random_pencolor())
        jim.circle(100)
        jim.setheading(jim.heading() + size_of_gap)
    jim.hideturtle()


draw_spirograph(5)

# Create screen object to keep window open. Keep this code at the very bottom.
screen = t.Screen()
screen.exitonclick()
