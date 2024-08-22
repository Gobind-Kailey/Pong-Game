# Importing files
from turtle import Turtle, Screen
from Scoreboard_pong import Scoreboard
from pong_paddles import Paddle
from ball_pong import Ball
import time


# Setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game- Gobind Kailey")
screen.tracer(0)

# Creating objects
scoreboard = Scoreboard()

paddle_l = Paddle((-370, 0))
paddle_r = Paddle((370, 0))
ball = Ball()

# Getting the screen to listen to our clicks.
screen.listen()
# Right paddle
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

# Left paddle
screen.onkey(paddle_l.up1, "w")
screen.onkey(paddle_l.down1, "s")

# Notice that by placing the screen.update inside the while loop, the screen updates everytime something happens
continue_game = True
while continue_game:
    screen.update()
    time.sleep(ball.move_speed)

    ball.random_corner()
    # if the wall collides with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision_wall()

    # Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 350 and ball.xcor() < 370:
        ball.collision_paddle()

    elif ball.distance(paddle_l) < 50 and ball.xcor() < -350 and ball.xcor() > -370:
        ball.collision_paddle()

    # This checks if the paddles have missed the ball.
    if ball.xcor() >= 390:
        scoreboard.score_point1()
        ball.home()
        ball.change_direction()

    if ball.xcor() <= -390:
        scoreboard.score_point2()
        ball.home()
        ball.change_direction()

screen.exitonclick()