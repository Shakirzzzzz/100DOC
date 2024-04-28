import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move_player, "w")

track_loop = 0
game_is_on = True
while game_is_on:

    car_manager.generate_car()

    car_manager.move_car()
    for i in car_manager.cars:

        if player.distance(i) < 20:
            game_is_on = False
        if player.ycor() == 280:
            player.goto(0, -280)
            car_manager.increase_speed()





    time.sleep(0.1)
    screen.update()

