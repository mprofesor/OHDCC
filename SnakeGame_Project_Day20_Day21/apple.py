from turtle import Turtle
import random

class Apple:
    def __init__(self):
        self.rand_position = (0, 0)
        self.basket = []

    def grow(self):
        apple = Turtle()
        apple.shapesize(0.5, 0.5, 0.5)
        #print(apple)
        self.rand_position = self.set_random_position()
        apple.penup()
        apple.shape("circle")
        apple.color("red")
        apple.setposition(self.rand_position)
        self.basket.append(apple)

    def set_random_position(self):
        return (random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)
    
    def move(self):
        self.rand_position = self.set_random_position()
        self.basket[0].setposition(self.rand_position)
