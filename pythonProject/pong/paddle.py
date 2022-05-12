from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        # x=400 should be end of screen
        self.goto(position)
        self.shapesize(1, 5)
        self.left(90)

    def go_up(self):
        self.forward(100)

    def go_down(self):
        self.backward(100)
