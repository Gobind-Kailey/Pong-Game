from turtle import Turtle
import random

# POSITION= [(380,280), (-380, 280), (380, -280), (-380, -280)]
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def create_ball(self):
        self.shape("circle")
        self.color("white")


    def random_corner(self):
        # Moves the ball to a random corner
        self.penup()
        # random_position = random.choice(POSITION)
        x_value = self.xcor() + self.x_move
        y_value = self.ycor() + self.y_move
        self.goto(x_value, y_value)

    def collision_wall(self):
        self.y_move *= -1

    def collision_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # This will change the direction of the ball.
    def change_direction(self):
        self.x_move *= -1
        self.y_move *= -1
        self.move_speed = 0.08
