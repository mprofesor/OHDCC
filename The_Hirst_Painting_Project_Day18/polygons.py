from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()
#timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("black")

sides = 3
r_color = 0
g_color = 0
b_color = 0
timmy_the_turtle.pensize(3)

for i in range(10):
    r_color = random.randint(0, 255)
    g_color = random.randint(0, 255)
    b_color = random.randint(0, 255)

    screen.colormode(255)
    timmy_the_turtle.pencolor(r_color, g_color, b_color)
    for j in range(sides):
        timmy_the_turtle.forward(50) 
        timmy_the_turtle.right(180 - ((sides - 2) * 180) / sides)
    sides += 1
    



screen.exitonclick()