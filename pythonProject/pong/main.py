from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
l_paddle = Paddle((-450, 0))
r_paddle = Paddle((450, 0))



screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
screen.onkey(l_paddle.go_up, key="z")
screen.onkey(l_paddle.go_down, key="s")

screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")















screen.exitonclick()
screen.exitonclick()