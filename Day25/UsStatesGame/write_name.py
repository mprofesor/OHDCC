from turtle import Turtle
        
def name_on_screen(x, y, name):
    new_scoreboard = Turtle()
    new_scoreboard.hideturtle()
    new_scoreboard.penup()
    new_scoreboard.setposition(x, y)
    new_scoreboard.color("black")
    new_scoreboard.write(name)