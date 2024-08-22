from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,  position):
        super().__init__()
        self.create_paddle()
        self.goto(position)

    # Creating the Paddle
    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)


    # Moving the first paddle up (right one)
    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def up1(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down1(self):
        self.goto(self.xcor(), self.ycor() - 20)
