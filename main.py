from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score



screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()





screen.listen()
screen.onkey(key="Up", fun=r_paddle.up_move)
screen.onkey(key="Down", fun=r_paddle.d_move)
screen.onkey(key="w", fun=l_paddle.up_move)
screen.onkey(key="s", fun=l_paddle.d_move)




game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()
    ball.b_moving()

    # detecting the bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_bounce()


#     detecting the bounce with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 315 or ball.distance(l_paddle) < 50 and ball.xcor() < -315:
        ball.x_bounce()

    # when right misses ball
    if ball.xcor() > 390:
        ball.reset_ball()
        score.left_score()


# left paddle miss
    if ball.xcor() < -380:
        ball.reset_ball()
        score.right_score()


screen.exitonclick()