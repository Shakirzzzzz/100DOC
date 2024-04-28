# import colorgram
#
# colours = colorgram.extract('hearst.jpg', 25)
# rgb_list = []
# for i in range(0, 25):
#     color = colours[i].rgb
#     r = color.r
#     g = color.g
#     b = color.b
#     my_tuple = (r, g, b)
#     rgb_list.append(my_tuple)
# print(rgb_list)
import random
import turtle
from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()
turtle.colormode(255)
color_pallet = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181)]

#
for i in range(0, 10):
    timmy.setposition(0.00, i* 40)

    for j in range(0,10):
        timmy.penup()
        timmy.dot(20, random.choice(color_pallet) )

        timmy.forward(60)






screen.exitonclick()