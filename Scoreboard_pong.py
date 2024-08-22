from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 50, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1 = 0
        self.p2 = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.create_line_middle()
        self.score_board1()
        self.score_board2()

    def create_line_middle(self):
        line_middle = Turtle()
        line_middle.hideturtle()
        line_middle.color('white')
        line_middle.penup()
        line_middle.goto(0, -290)
        line_middle.left(90)
        for i in range(30):
            line_middle.pendown()
            line_middle.forward(10)
            line_middle.penup()
            line_middle.forward(10)

    # Creating scoreboards
    def score_board1(self):
        self.goto(-40, 220)
        self.write(arg= f"{self.p1}", align= ALIGNMENT , font= FONT )

    def score_board2(self):
        self.goto(40, 220)
        self.write(arg= f"{self.p2}", align= ALIGNMENT , font= FONT )

    # Incrementing the score when a point is scored.
    def score_point1(self):
        self.p1 += 1
        self.clear()
        self.score_board1()
        self.score_board2()

    def score_point2(self):
        self.p2 += 1
        self.clear()
        self.score_board1()
        self.score_board2()





