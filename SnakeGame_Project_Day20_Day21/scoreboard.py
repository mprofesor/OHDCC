from turtle import Turtle

class ScoreBoard:
    def __init__(self):
        self.num_score = 0
        self.text = "Score: "
        self.points = []
        with open("highscores.txt", mode="r") as hs:
            self.highscore = int(hs.read())
        #self.highscore = 0
        self.text_highscore = "Highscore: "

    def create_scoreboard(self):
        new_scoreboard = Turtle()
        new_scoreboard.hideturtle()
        new_scoreboard.setposition(0, 350)
        new_scoreboard.penup()
        new_scoreboard.color("white")
        self.points.append(new_scoreboard)
        self.points[0].write(f"{self.text}{self.num_score}  {self.text_highscore}{self.highscore}", False, align="center", font=('Arial', 12, 'bold'))


    def add_point(self):
        self.num_score += 1
        if self.num_score >= self.highscore:
            self.highscore = self.num_score
        self.points[0].clear()
        self.points[0].write(f"{self.text}{self.num_score}  {self.text_highscore}{self.highscore}", False, align="center", font=('Arial', 12, 'bold'))

    def reset(self):
        self.save_highscore()
        self.num_score = 0
        self.points[0].clear()
        self.create_scoreboard()

    def save_highscore(self):
        with open("highscores.txt", mode="w") as hs:
            hs.write(str(self.highscore))


