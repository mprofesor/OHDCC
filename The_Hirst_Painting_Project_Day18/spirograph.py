from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.color("black")
screen.colormode(255)
timmy_the_turtle.pensize(2)
timmy_the_turtle.speed(60)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    random_rgb_color = (r, g, b)

    return random_rgb_color

def draw_spirograph(size_of_gap, radius):
    for steps in range(int(360 / size_of_gap)):
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.circle(radius)
        timmy_the_turtle.left(size_of_gap)

draw_spirograph(10, 100)


screen.exitonclick()