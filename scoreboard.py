from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=-330)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, move=False, align="right", font=("arial", 50, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, move=False, align="right", font=("arial", 50, "bold"))
        self.goto(-40, -360)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


divider = Turtle()
divider.penup()
divider.hideturtle()
divider.color("white")
divider.goto(x=0, y=-340)
divider.write("""|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|""", move=False, font=("ariel", 30, "bold"), align="center")
