# difference between tuple and list:
# tuples are immutable(unchanging over time or unable to be changed) objects the lists are mutable


# args = ARGumentS
def add(*args):
    print(type(args))
    print(args[0], args[5])
    sum = 0
    for i in args:
        sum += i

    return sum

print(add(5,5,5,6,8,7,4))


# dictionary of KeyWord ARGuments
def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])

    n += kwargs["add"]
    print(f"n += add = {n}")
    n *= kwargs["multiply"]
    print(f"n *= multiply = {n}")


calculate(n=2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # kwargs.get("make") instead of kwargs["make"]:
        # because my_car2 would otherwise give an error because it doesn't has a make=""
        # written like this: kwargs.get("make") -> makes it optional
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="GT-R")
my_car2 = Car(model="Supra")
print(my_car.make, my_car.model)
print(my_car2.make)
