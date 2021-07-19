from Paddle import Paddle
from ball import Ball
from turtle import Screen
from scoreboard import ScoreBoard, divider

import time

divider.goto(0, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1.0, height=1.0)

screen.tracer(0)
time.sleep(0.3)
l_paddle = Paddle(-650)

r_paddle = Paddle(650)
scoreboard = ScoreBoard()

screen.update()
ball = Ball()
screen.listen()
screen.onkeypress(fun=l_paddle.paddle_up, key="w")
screen.onkeypress(fun=l_paddle.paddle_down, key="s")
screen.onkeypress(fun=r_paddle.paddle_up, key="Up")
screen.onkeypress(fun=r_paddle.paddle_down, key="Down")
screen.update()


game_is_on = True
while game_is_on:
    time.sleep(0.03)
    ball.move()
    # Detect collision with the wall
    if ball.detect_coli_wall():
        ball.bounce()
        screen.update()

    if ball.xcor() < -650:
        scoreboard.r_point()
        screen.update()
        ball.reset()

    if ball.xcor() > 650:
        scoreboard.l_point()
        screen.update()
        ball.reset()
    # Detect collision with the wall
    if ball.xcor() > 630 and ball.distance(r_paddle) < 50:
        scoreboard.r_point()
        ball.speed_up()
        ball.bounce_back()
    if ball.xcor() < -630 and ball.distance(l_paddle) < 50:
        scoreboard.l_point()
        ball.speed_up()
        ball.bounce_back()

    screen.update()

screen.exitonclick()
