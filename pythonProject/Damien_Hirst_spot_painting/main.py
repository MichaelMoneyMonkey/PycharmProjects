# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg.webp',30)
#
# print(colors)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


from turtle import Turtle as T, Screen
import random


t = T()
screen = Screen()
screen.colormode(255)


color_list = [(43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50),
              (228, 120, 147), (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139),
              (55, 176, 110), (116, 168, 37), (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108),
              (154, 222, 193), (181, 170, 221), (30, 163, 170), (84, 35, 39), (40, 46, 80), (233, 167, 180),
              (237, 172, 162), (76, 40, 39), (154, 208, 221), (115, 46, 43)]


# requirements
# 10 X * 10 Y
# dots 20 size spaced 50

# move to bottom right of screen
t.hideturtle()
t.penup()
t.goto(-250, -250)
t.pendown()
t.showturtle()
t.speed(0)
t.hideturtle()


def draw_line():
    for i in range(10):
        # take random color out of list
        random.choice(color_list)
        # draw dots
        t.dot(25, random.choice(color_list));
        # move 50 without drawing line
        t.penup()
        t.forward(50)
        t.pendown()


def line_up():

    t.penup()
    t.left(180)
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.pendown()


for i in range(10):
    draw_line()
    line_up()



screen.exitonclick()


