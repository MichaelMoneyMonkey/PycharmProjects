from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
# not screen.screensize(800, 600)
# The screensize() method sets the amount of area the turtle can roam,
# but doesn't change the screen size (despite the name), just the scrollable area.
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
# to remove starting animation
screen.tracer(0)


# double parentheses because the position is a tuple
# (the inner parentheses are from the tuple)
# (the outer from the function)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(l_paddle.go_up, key="z")
screen.onkey(l_paddle.go_down, key="s")

screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    # 300 - 20(size of ball) = 280
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("ball collision with paddle")
        ball.bounce_x()

    # detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()
