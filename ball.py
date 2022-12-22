from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        # self.goto(x= 0, y= 0)
        self.y_move = 1
        self.x_move = 1


    def b_moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.x_bounce()

    def rigt_reset_ball(self):
        self.goto(0, 0)
        self.y_bounce()


