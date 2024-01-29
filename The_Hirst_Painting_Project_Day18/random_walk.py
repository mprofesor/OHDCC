from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.color("black")
screen.colormode(255)

rgb_color = (0, 0, 0)
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed(30)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    random_rgb_color = (r, g, b)

    return random_rgb_color

for i in range(2000):
    turn = random.randint(0, 3)
    left_or_right = random.randint(1, 2)

    timmy_the_turtle.pencolor(random_color())
    timmy_the_turtle.forward(30)
    if left_or_right == 1:
        timmy_the_turtle.left(turn * 90)
    elif left_or_right == 2:
        timmy_the_turtle.right(turn * 90)

screen.exitonclick()