from turtle import Turtle,Screen
screen = Screen()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.x_mov = 10
        self.y_mov = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_mov *= -1

    def bounce_back(self):
        self.x_mov *= -1

    def detect_coli_wall(self):
        if self.xcor() > 650 or self.xcor() < -650 or self.ycor() > 360 or self.ycor() < -300:
            return True

    def reset(self):
        self.goto(0, 0)
        self.bounce_back()
        self.bounce()

    def speed_up(self):
        self.ball_speed *= 0.09
