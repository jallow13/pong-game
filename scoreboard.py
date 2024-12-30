from turtle import Turtle

class ScoreBored(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.score_track()

    def score_track(self):
        self.clear()
        self.goto(-60, 220)
        self.write(self.left_score, align="center", font=("Curie", 50, "normal"))
        self.goto(60, 220)
        self.write(self.right_score, align="center", font=("Curie", 50, "normal"))

    def left_s(self):
        self.left_score+=1
        self.score_track()
    def right_s(self):
        self.right_score+=1
        self.score_track()

