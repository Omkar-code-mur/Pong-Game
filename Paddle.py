from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.new_y = 0
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.forward(20)
        self.goto(x=x_pos, y=0)

    def paddle_up(self):
        if self.ycor() < 330:
            self.new_y = self.ycor() + 20
            self.goto(self.xcor(), self.new_y)

    def paddle_down(self):
        if self.ycor() > -330:
            self.new_y = self.ycor() - 20
            self.goto(self.xcor(), self.new_y)
