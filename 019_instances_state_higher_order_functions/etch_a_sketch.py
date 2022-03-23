from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()

# Use function as input


def move_forwards():
    jim.forward(10)


def move_backwards():
    jim.backward(10)


def turn_left():
    jim.left(10)


def turn_right():
    jim.right(10)


def clear():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()


screen.listen()
# Use keyword arguments when you are using methods that you didn't create yourself.
screen.onkey(key='w', fun=move_forwards)  # When a function is used as argument, do not add () at the end.
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
