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
# for i in range(0, 4):
#     timmy.forward(100)
#     timmy.right(90)


colours = ['red', 'green', 'blue', 'purple', 'black', 'pink', 'white']




angles = [90, 180, 270, 0]
timmy.pensize(8)
timmy.speed(8)

for i in range(100):
    timmy.pencolor(random_color())
    timmy.forward(15)
    timmy.setheading(random.choice(angles))




# for i in range(3,11):
#     for x in range(1, i + 1 ):
#
#         timmy.forward(100)
#         timmy.right(360/i)






















screen.exitonclick()
