from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game Strikes Back!")
screen.tracer(0)

# 1. Create snake body.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 2. Move the snake.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # 3. Control the Snake
    snake.move()

    # 4. Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 5. Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        scoreboard.reset()
        snake.reset()

    # 6. Detect collision with tail.
    # If head collides with any snake segment in the tail:
    # Trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
