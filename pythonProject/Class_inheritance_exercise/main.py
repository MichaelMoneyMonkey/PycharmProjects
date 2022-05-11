# TODO
#   - class animal
#   - num_eyes 2
#   - function breath with print statement ("inhale, exhale")

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")

tiger = Animal()
# tiger.breathe()

print(tiger.num_eyes)

# TODO 2
#   - class fish with inheritance of animal class
#   - function swim with print statement ("moving in water")
#   - add print statement to function breathe ("doing this underwater")
#   - make nemo a fish in Fish() class
#   - make nemo swim and breathe in terminal


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving underwater")

    def breathe(self):
        super().breathe()
        print("doing this underwater")


nemo = Fish()
nemo.breathe()



# TODO
#   - class animal
#   - num_eyes 2
#   - function breath with print statement ("inhale, exhale")




# TODO 2
#   - class fish with inheritance of animal class
#   - function swim with print statement ("moving in water")
#   - add print statement to function breathe ("doing this underwater")
#   - make nemo a fish in Fish() class
#   - make nemo swim and breathe in terminal







