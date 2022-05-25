from turtle import Turtle

# Constants = CAPITAL letters
STARTING_POSITIONS = [(-10, 0), (-30, 0), (-50, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        # create new attribute self.head which equals self.segments[0]
        self.head = self.segments[0]
        self.heading = 0


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # [-1] takes the last list item in a list
        self.add_segment(self.segments[-1].position())

    def move(self):
        # for loop: to make the last segment (1 single snake cube) move to the position of the next segment
        # len(segments) because the list (when the snake catches food) will get bigger
        # range -> start from len(segments), stop at 0, step for -1
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # new_x = last seg_num out of self.segments list - 1 (so second last)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # last seg_num (cube) out of segment list .goto(new coordinates)
            # aka move the last cube to the position of the second last cube
            self.segments[seg_num].goto(new_x, new_y)
        # get the first segment and make it move forward (so that the rest can follow)
        self.head.forward(MOVE_DISTANCE)
        self.heading = self.head.heading()

    def up(self):
        if self.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.heading != LEFT:
            self.head.setheading(RIGHT)

