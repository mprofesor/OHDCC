from turtle import Turtle

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.setposition(position)
        self.color("white")
        self.dir_x = "left"
        self.dir_y = "down"
        self.speed = 10

    def movement(self):
        if self.dir_x == "left":
            new_x = self.xcor() - (1 * self.speed)
            self.goto(new_x, self.ycor())
        elif self.dir_x == "right":
            new_x = self.xcor() + (1 * self.speed)
            self.goto(new_x, self.ycor())
        
        if self.dir_y == "up":
            new_y = self.ycor() + (1 * self.speed)
            self.goto(self.xcor(), new_y)
        elif self.dir_y == "down":
            new_y = self.ycor() - (1 * self.speed)
            self.goto(self.xcor(), new_y)
    
    def detect_collision(self):
        if self.ycor() > 270:
            self.dir_y = "down"
        elif self.ycor() < -270:
            self.dir_y = "up"
        
        if self.xcor() > 370:
            self.dir_x = "left"
        elif self.xcor() < -370:
            self.dir_x = "right"
        
    def paddle_collision(self):
        if self.dir_x == "left":
            self.dir_x = "right"
        elif self.dir_x == "right":
            self.dir_x = "left"
    
    def increase_speed(self):
        self.speed += 1

    def reset_speed(self):
        self.speed = 10

        # Debug
        #print(self.ycor())
        #print(self.xcor())
        #print(self.dir_x)
        #print(self.dir_y)


