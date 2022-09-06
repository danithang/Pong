from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# turns off animation, then after paddle class gets created, then a while loop to update screen so you won't see
# paddle move over
screen.tracer(0)

# getting both paddles in right positions, either 350 or -350 on x-axis and 0 on y-axis
# this is a tuple which is why its double parenthesis...
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

# assigning the keys to move the paddles up and down
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_on = True
while game_on:
    # get screen to update only for paddle
    screen.update()
    # getting the move_speed from ball class to start
    time.sleep(ball.move_speed)
    # calling move_ball() from ball.py to get the ball to constantly move while the game is still on
    ball.move_ball()
    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with r_paddle and l_paddle in order for it to bounce the ball...if ball distance is 50 pixels
    # from right or left paddle and the ball coordinate is either greater than or less than the x-axis coordinates
    # depending on positive or negative hence 320 and -320
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detecting if ball coordinates go past the x-axis either way signaling a loss...if ball goes out on left side
    # then right side gets the point and vice versa
    if ball.xcor() < -380:
        score.right_increase_score()
        score.update_scoreboard()
        ball.reset_position()

    if ball.xcor() > 380:
        score.left_increase_score()
        score.update_scoreboard()
        ball.reset_position()


screen.exitonclick()
