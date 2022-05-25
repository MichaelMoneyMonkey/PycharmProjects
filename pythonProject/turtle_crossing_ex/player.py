from turtle import Turtle
START_POSITION = -280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.goto(0, START_POSITION)
        self.left(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
