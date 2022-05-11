from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
    t.forward(10)

def move_down():
    t.backward(10)

def move_left():
    t.left(10)

def move_right():
    t.right(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkeypress(fun=move_forward, key="Up")
screen.onkeypress(fun=move_down, key="Down")
screen.onkeypress(fun=move_left, key="Left")
screen.onkeypress(fun=move_right, key="Right")

screen.onkeypress(fun=clear_screen, key="c")






screen.exitonclick()