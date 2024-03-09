from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the scoreboard, set 2 counters on the right and left side for both players"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def add_point(self, xcor):
        """Add a point, if xcor > 0 - ball went over the right side - left player won
        if xcor < 0 ball wend over the left side - right player won.
        Then update the scoreboard"""
        if xcor > 0:
            self.l_score += 1
        else:
            self.r_score += 1
        self.update_scoreboard()