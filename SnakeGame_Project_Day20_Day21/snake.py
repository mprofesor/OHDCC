from turtle import Turtle

class Snake:
    def __init__(self):
        self.length = 3
        self.seg_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
        self.hatch()

    def hatch(self):
        """
        This function should be called once per object
        and it's called from __init__(self) function
        """
        self.snake = []
        for segment in range(0, self.length):
            snake_seg = Turtle()
            snake_seg.penup()
            snake_seg.color("white")
            snake_seg.shape("square")
            snake_seg.setpos(self.seg_positions[segment])
            self.snake.append(snake_seg)

    # This function is adding one segment to the snake
    # (it's important to move(take a step) the snake for it to work properly)
    def add_segment(self):
        """This function is used to add new segment to the existing snake"""
        snake_seg = Turtle()
        snake_seg.penup()
        snake_seg.color("white")
        snake_seg.shape("square")
        snake_seg.setpos(self.seg_positions[self.length - 1])
        self.snake.append(snake_seg)
        self.length += 1
    
    def step(self):
        for segment in range(self.length, 0, -1):
            #print(self.seg_positions) # Debug
            #print(f"Call number: {segment}")
            old_position = self.seg_positions[self.length]
            if segment != 0:
                new_position = self.seg_positions[segment - 1]
                self.seg_positions[segment] = new_position
            
            for segment in range(1, self.length):
                self.snake[segment].setpos(self.seg_positions[segment])
            
        self.snake[0].forward(20)
        self.seg_positions[0] = (int(round(self.snake[0].pos()[0])), int(round(self.snake[0].pos()[1])))
        if len(self.seg_positions) < 90:
            self.seg_positions.append(old_position)
        #print(self.seg_positions)

    def turn_right(self):
        self.snake[0].right(90)

    def turn_left(self):
        self.snake[0].left(90)

    def reset(self):
        for segment in range(0, self.length):
            self.snake[segment].setpos(1000, 1000)

        for i in range(self.length - 3):
            self.snake.pop()
            self.length = self.length - 1
        
        self.snake.clear()
        self.length = 3
        self.seg_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
        self.hatch()


        



