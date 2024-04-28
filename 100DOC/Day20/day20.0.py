from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time



screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")


screen.tracer(0)

scoreboard = ScoreBoard()

snake = Snake()
food = Food()


game_is_on = True

while game_is_on:
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    screen.update()

    time.sleep(0.1)

    snake.move()

    if snake.snake_head.distance(food) < 15:

        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.refresh()
        snake.reset()

    for segment in snake.segments[1:]:

        if  snake.snake_head.distance(segment) < 10:
            scoreboard.refresh()
            snake.reset()




































screen.exitonclick()