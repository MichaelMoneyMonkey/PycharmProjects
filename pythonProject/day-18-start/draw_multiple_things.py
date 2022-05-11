from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red", "green")

# # draw square
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)


# # draw dashed line
# for i in range(20):
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)


# draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# triangle = 360 / 3 = 120
# square = 360 / 4 = 90
# pentagon = 360 / 5 = 72

# # move to start position
timmy.left(120)
timmy.penup()
timmy.forward(400)
timmy.right(120)
timmy.forward(200)
timmy.pendown()

def move():
    angle = 360 / num_times
    for i in range(num_times):
        timmy.right(angle)
        timmy.forward(100)

# triangle
timmy.color("black")
num_times = 3
move()

# square
timmy.color("red")
num_times = 4
move()

# pentagon
timmy.color("black")
num_times = 5
move()

# hexagon
timmy.color("red")
num_times = 6
move()

# heptagon
timmy.color("black")
num_times = 7
move()

# octagon
timmy.color("red")
num_times = 8
move()

# nonagon
timmy.color("black")
num_times = 9
move()

# decagon
timmy.color("red")
num_times = 10
move()






screen = Screen()
screen.exitonclick()
