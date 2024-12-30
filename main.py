import time
from turtle import Screen

from ball import Ball
from paddles import Paddle
from scoreboard import ScoreBored

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-280,0))
right_paddle = Paddle((280,0))
ball = Ball()
score = ScoreBored()

screen.listen()
screen.onkeypress(fun=right_paddle.go_up,key="Up")
screen.onkeypress(fun=right_paddle.go_down,key="Down")
screen.onkeypress(fun=left_paddle.go_up,key="w")
screen.onkeypress(fun=left_paddle.go_down,key="s")

# game_on = True
# while game_on:
#     if left_paddle.ycor() < 280 or right_paddle.ycor() > -280:

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 260 or ball.distance(left_paddle) < 50 and ball.xcor() > -260:
        ball.ball_bounce_x()
    if ball.xcor() >280:
        ball.reset_game()
        score.left_s()

    if ball.xcor() < -280:
        ball.reset_game()
        score.right_s()


screen.exitonclick()