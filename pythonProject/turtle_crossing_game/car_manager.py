from turtle import Turtle
import random


COLORS = ["white"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)

    def create_new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            # no cars should be generated in the top and bottom 40px of the screen
            # randrange = randint but in randrange u can add steps
            new_car.goto(280, random.randrange(-240, 240, 20))
            self.all_cars.append(new_car)
