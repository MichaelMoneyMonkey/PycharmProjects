from turtle import Turtle, Screen, colormode
import random
from random import randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red", "green")

# random color
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color
print(random_color())

timmy.speed(0)

# 72 * 5 = 360
for i in range(72):
    timmy.pencolor(random_color())
    timmy.circle(100)
    timmy.left(5)



screen = Screen()
screen.exitonclick()
