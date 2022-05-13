from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.color("red")


    def go_up(self):
        self.forward(MOVE_DISTANCE)
        print(self.pos())

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            print("reached 280+ ycor = finish line")
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
