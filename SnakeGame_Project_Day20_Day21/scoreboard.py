from turtle import Turtle

class ScoreBoard:
    def __init__(self):
        self.num_score = 0
        self.text = "Score: "
        self.points = []

    def create_scoreboard(self):
        new_scoreboard = Turtle()
        new_scoreboard.hideturtle()
        new_scoreboard.setposition(0, 350)
        new_scoreboard.penup()
        new_scoreboard.color("white")
        self.points.append(new_scoreboard)
        self.points[0].write(f"{self.text}{self.num_score}", False, align="center", font=('Arial', 12, 'bold'))


    def add_point(self):
        self.num_score += 1
        self.points[0].clear()
        self.points[0].write(f"{self.text}{self.num_score}", False, align="center", font=('Arial', 12, 'bold'))


