COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager():
    def __init__(self,):
        self.starting_speed = STARTING_MOVE_DISTANCE

        self.cars = []



    def generate_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250,250))
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)
    def move_car(self):
        for i in self.cars:
            i.forward(self.starting_speed)

    def increase_speed(self):
        self.starting_speed += MOVE_INCREMENT





