from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import  ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup( 800,  600)
screen.title("Pong")

screen.tracer(0)
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))



ball = Ball()
scoreboard = ScoreBoard()



screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(paddle1) < 50 and ball.xcor() >320 or ball.distance(paddle2) <50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed += 20
    if ball.xcor() >380:
        ball.setposition(0,0)
        ball.x *= -1

        scoreboard.l_score += 1
        scoreboard.update_score()
    if ball.xcor() < -380:
        ball.setposition(0,0)
        scoreboard.r_score += 1
        ball.x *= -1
        scoreboard.update_score()





    ball.move_ball()












screen.exitonclick()


