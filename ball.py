from turtle import Turtle

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_xco = self.xcor()+ self.x_move
        new_yco = self.ycor()+ self.y_move
        self.goto(new_xco,new_yco)

    def ball_bounce_y(self):
        self.y_move *=-1


    def ball_bounce_x(self):
        self.x_move *=-1
        self.ball_speed *= 0.9
    def reset_game(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.ball_bounce_x()
