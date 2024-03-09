import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

# Objects initialization
player_left = Paddle((-350,0))
player_right = Paddle((350,0))
ball = Ball()
score = ScoreBoard()

screen.listen()

# Left player keys
screen.onkeypress(player_left.move_up, "w")
screen.onkeypress(player_left.move_down, "s")

# Right player keys
screen.onkeypress(player_right.move_up, "Up")
screen.onkeypress(player_right.move_down, "Down")

screen.onkey(screen.bye, "Escape")

while True:
    time.sleep(0.005)
    screen.update()
    ball.move()

    # Check for collision with the top and bottom walls and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")

    # Check for collision with the players and bounce
    if ball.distance(player_right) < 50 and ball.xcor() > 330 or ball.distance(player_left) < 50 and ball.xcor() < -330:
        ball.bounce("x")

    # Check for scoring a point
    elif ball.xcor() > 400 or ball.xcor() < -400:
        score.add_point(ball.xcor())
        ball.increase_speed()
        ball.restart()