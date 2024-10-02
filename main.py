from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle1 = Paddle(-350)
paddle2 = Paddle(350)
ball1 = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(paddle1.start_moving_up, "w")
screen.onkeyrelease(paddle1.stop_moving_up, "w")
screen.onkeypress(paddle1.start_moving_down, "s")
screen.onkeyrelease(paddle1.stop_moving_down, "s")

screen.onkeypress(paddle2.start_moving_up, "Up")
screen.onkeyrelease(paddle2.stop_moving_up, "Up")
screen.onkeypress(paddle2.start_moving_down, "Down")
screen.onkeyrelease(paddle2.stop_moving_down, "Down")

def move():
    paddle1.move()
    paddle2.move()
    screen.ontimer(move, 50)

move()

while True:
    if (ball1.xcor() > 400 or ball1.xcor() < -400):
        if(ball1.xcor() > 400):
            scoreboard.increase_l_score()
        else:
            scoreboard.increase_r_score()
        ball1.reset_position()
    if (ball1.ycor() > 280 or ball1.ycor() < -280):
        ball1.wallBounce()
    if ((ball1.distance(paddle1) < 50 and ball1.xcor() < -320) or 
        (ball1.distance(paddle2) < 50 and ball1.xcor() > 320)):
        ball1.paddleBounce()
    ball1.move()
    






screen.exitonclick()