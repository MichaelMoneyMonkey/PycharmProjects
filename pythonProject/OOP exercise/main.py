# https://pynative.com/python-object-oriented-programming-oop-exercise/


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(300, 9000)
print(modelX.max_speed, modelX.mileage)






















class Grade:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

stud_1 = Grade("Alfons", 95)
print(stud_1.name, stud_1.grade)



#
# class Employee:
#
#     def __init__(self, name, id, years):
#         self.name = name
#         self.id = id
#         self.years = years
#
# employee_1 = Employee("Alfred", "005", 6)
#
# print(employee_1.name + " jaar in dienst: " + str(employee_1.years))
#





class Employee:

    def __init__(self, name, id, years):
        self.name = name
        self.id = id
        self.years = years

employee1 = Employee("alfred", "005", 18)

print(employee1.years)












# Class Employee
# naam
# id
# jaren in diesnt













