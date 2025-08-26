from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

# Create window
window = Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Code here
#    vvv

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

window.listen()
window.onkey(r_paddle.go_up,"Up")
window.onkey(r_paddle.go_down, "Down")
window.onkey(l_paddle.go_up,"w")
window.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    if ball.xcor() >= r_paddle.xcor() - 20 and ball.ycor() <= r_paddle.ycor() + 50 and ball.ycor() >= r_paddle.ycor() - 50:
        ball.paddle_collision()
        ball.increase_speed()

    if ball.xcor() <= l_paddle.xcor() + 20 and ball.ycor() <= l_paddle.ycor() + 50 and ball.ycor() >= l_paddle.ycor() - 50:
        ball.paddle_collision() 
        ball.increase_speed()

    ball.detect_collision()
    ball.movement()
    scoreboard.update()
    window.update()
    sleep(0.1)
    
    # Game over condition
    # If the right paddle misses
    if ball.xcor() > 370:
        ball.setx(0)
        ball.sety(0)
        ball.reset_speed()
        scoreboard.pointup_l()
        #print(scoreboard.l_score)
        scoreboard.update()
        window.update()
        sleep(1)

    # If the left paddle misses
    elif ball.xcor() < -370:
        ball.setx(0)
        ball.sety(0)
        ball.reset_speed()
        scoreboard.pointup_r()
        #print(scoreboard.r_score)
        scoreboard.update()
        window.update()
        sleep(1)
        

window.exitonclick()