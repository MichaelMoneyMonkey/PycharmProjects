from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    # def create_car(self):
    #     new_car = Turtle("square")
    #     self.cars.append(new_car)
    #
    def create_car(self):

        new_car = Turtle("square")
        new_car.shapesize(1, 2)


        self.all_cars.append(new_car)