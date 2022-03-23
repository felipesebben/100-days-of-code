from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game Strikes Back!")
screen.tracer(0)
# 1. Create snake body.
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#2. Move the snake.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# 3. Control the Snake









screen.exitonclick()
