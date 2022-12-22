from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.color("white")
        self.goto(pos)

    def up_move(self):
        new_y = self.ycor() + 10
        self.goto(x=self.xcor(), y=new_y)


    def d_move(self):
        new_y = self.ycor() - 10
        self.goto(x=self.xcor(), y=new_y)



