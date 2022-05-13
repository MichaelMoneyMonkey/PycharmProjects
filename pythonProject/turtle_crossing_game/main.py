import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import threading

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# Tracer is used to turn the animation on-off and also set a delay for updating our drawing objects
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    # whatever you put in this while loop will be refreshed every x sec time.sleep(x)
    time.sleep(scoreboard.move_speed)
    screen.update()

    car_manager.move_cars()
    car_manager.create_new_car()

    # detect player at finnish line
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    # if scoreboard.level() == 2:
    #     print("ish")



screen.exitonclick()