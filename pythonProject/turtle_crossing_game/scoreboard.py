from turtle import Turtle
FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.goto(x=-180, y=250)
        self.hideturtle()
        self.update_scoreboard()
        self.move_speed = 0.1



    def update_scoreboard(self):
        self.write(f"LEVEL = {self.level}",  align="center", font=('Courier', 25, "bold"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
        self.move_speed *= 0.5

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=(FONT))
        self.move_speed = 0.1
