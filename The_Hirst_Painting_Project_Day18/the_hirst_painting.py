import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('TheHirst.jpg', 90)
timmy = Turtle()
screen = Screen()
list_of_colors = []
for color in colors:
    rgb = color.rgb
    list_of_colors.append(rgb)
screen.colormode(255)

timmy.pensize(3)
timmy.penup()
timmy.speed(60)


def make_hirst_dots(size_of_dot, n_row_dots, n_col_dots):
    """
    This function creates the Hirst's like dot painting
    size_of_dot(int), n_row_dots(int) - number of dots in row,
    n_col_dots(int) - number of dots in one column
    """
    for x in range(-size_of_dot*n_row_dots, size_of_dot*n_row_dots, size_of_dot * 2):
        timmy.setx(x)
        for y in range (-size_of_dot*n_col_dots, size_of_dot*n_col_dots, size_of_dot * 2):
            timmy.sety(y)
            timmy.dot(size_of_dot, random.choice(list_of_colors))

make_hirst_dots(50, 2, 1)


screen.exitonclick()


