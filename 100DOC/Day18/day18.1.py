import turtle
from turtle import  Turtle, Screen
import random
timmy = Turtle()

screen = Screen()

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple
timmy.shape('arrow')
timmy.color('red')
timmy.speed('fastest')

for i in range(100):
    timmy.color(random_color())
    timmy.circle(40)
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 10)









screen.exitonclick()
