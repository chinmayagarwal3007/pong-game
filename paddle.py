from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x, 0)
        self.moving_up = False
        self.moving_down = False

    def start_moving_up(self):
        self.moving_up = True

    def stop_moving_up(self):
        self.moving_up = False

    def start_moving_down(self):
        self.moving_down = True

    def stop_moving_down(self):
        self.moving_down = False

    def move(self):
        if self.moving_up:
            self.goto(self.xcor(), self.ycor() + 20)  # Adjust speed as needed
        if self.moving_down:
            self.goto(self.xcor(), self.ycor() - 20)  # Adjust speed as needed