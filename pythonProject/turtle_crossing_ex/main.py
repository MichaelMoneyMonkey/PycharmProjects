from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
player = Player()
car_manager = CarManager
scoreboard = Scoreboard

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()