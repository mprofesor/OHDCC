from turtle import Turtle

class Wall:
    def __init__(self):
        self.wall = []

    def build(self):
        for x in range(-300, 301, 10):
            for y in range(-300, 301, 10):
                if y == -300 or y == 300 or x == -300 or x == 300:
                    new_brick = Turtle()
                    new_brick.penup()
                    new_brick.color("white")
                    new_brick.shape("square")
                    new_brick.setposition(x, y)
                    self.wall.append(new_brick)