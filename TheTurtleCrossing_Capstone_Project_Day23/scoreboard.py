from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0

    def update(self):
        self.clear()
        self.goto(-250, 250)
        self.write(self.score, align="center", font=FONT)

    def pointup(self):
        self.score += 1
        self.update()

    def show_gameover(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
    