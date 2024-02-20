from turtle import Screen
import snake
import apple
import scoreboard
import wall
import time

# Create a window
game_window = Screen()
game_window.title("Snake The Game")
game_window.screensize(60, 60, "black")




new_snake = snake.Snake()
new_apple = apple.Apple()
game_on = True
game_window.tracer(0)
new_wall = wall.Wall()
new_wall.build()
new_scoreboard = scoreboard.ScoreBoard()
new_scoreboard.create_scoreboard()

while game_on:
    game_window.update()
    time.sleep(0.1)
    new_snake.step()
    game_window.listen()
    game_window.onkey(new_snake.turn_right, "Right")
    game_window.onkey(new_snake.turn_left, "Left")
    if len(new_apple.basket) == 0:
        new_apple.grow()

    # Eating apple
    if int(round(new_snake.snake[0].pos()[0])) == int(round(new_apple.basket[0].pos()[0])) and int(round(new_snake.snake[0].pos()[1])) == int(round(new_apple.basket[0].pos()[1])):
        new_apple.move()
        new_snake.add_segment()
        new_scoreboard.add_point()

    # Head position at the moment
    x_snake_head = int(round(new_snake.snake[0].pos()[0]))
    y_snake_head = int(round(new_snake.snake[0].pos()[1]))

    # Hitting wall
    if x_snake_head == -300 or x_snake_head == 300 or y_snake_head == -300 or y_snake_head == 300:
        print("Game over you've hit the wall!")
        game_on = False
    
    # Eating tail
    for l in range(1, new_snake.length):
        if x_snake_head == int(round(new_snake.snake[l].pos()[0])) and y_snake_head == int(round(new_snake.snake[l].pos()[1])):
            print("You've eaten your own tail!")
            game_on = False
    

         












game_window.exitonclick()