import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()
def move():
    timmy.forward(10)
def turn_right():
    timmy.heading()
    timmy.setheading(timmy.heading() + 10)
def turn_left():
    timmy.heading()
    timmy.setheading( timmy.heading() - 10)




screen.onkey(move, "space")
screen.onkey(fun = turn_left, key = "Up" )
screen.onkey(fun = turn_right, key = "Down")
screen.listen()









screen.exitonclick()