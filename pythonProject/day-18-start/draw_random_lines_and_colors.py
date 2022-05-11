from turtle import Turtle, Screen, colormode
import random
from random import randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red", "green")



# tasks
# 1.random movement
# 2.random colors
# 3.thick lines
# 4.speed up

timmy.pensize(10)
timmy.speed(0)

colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color



for i in range(200):
    # generate random color
    # random_color = ["beige", "khaki", "tan", "saddle brown", "rosy brown"]
    # color = random.choice(random_color)

    timmy.color(random_color())

    # move random distance
    random_distance = random.randint(1, 100)

    timmy.forward(random_distance)

    # generate random turn
    possible_turns = [0, 90, 180, 270]
    turn = random.choice(possible_turns)

    timmy.left(turn)





screen = Screen()
screen.exitonclick()
