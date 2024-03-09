from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        # X axis speed
        self.x_move = 1
        # Y axis speed
        self.y_move = 1

    def bounce(self, direction):
        """Reverse the direction of the ball depending on the direction of the bounce"""
        if direction == "y":
            self.y_move *= -1
        if direction == "x":
            self.x_move *= -1
    
    def move(self):
        """Main move method direction is dictated by the value of the x_move and y_move variables"""
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def increase_speed(self):
        """Increase the speed of the ball"""
        self.x_move += 0.02 if self.x_move > 0 else -0.02
        self.y_move += 0.02 if self.y_move > 0 else -0.02

    def restart(self):
        """Restart the position of the ball and reverse its x direction"""
        self.goto(0,0)
        self.bounce('x')
        