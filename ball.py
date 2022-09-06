from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        # creating variables to move ball 10 pixels
        self.x_move = 10
        self.y_move = 10
        # have the ball starting off at 0.1 speed
        self.move_speed = 0.1

    # moving ball from position it starts and adding 10 pixels and telling the ball to always go to new position with
    # while loop
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # getting it to bounce off the ycor only...if new_y is moving the ball by adding 10 pixels then when it
    # bounces off the wall, the ball needs to do the opposite of -10...10 is being added to ycor then ball
    # is moving upward, multiplying y_move by -1 reverses the direction(same as saying adding -10 to the ycor...
    # multiplying -1 10 times
    def bounce_y(self):
        self.y_move *= -1

    # bouncing off of the paddles and increasing the speed each time paddles hit ball
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # resetting the position to (0, 0) when it goes out of bounds to restart the game within the loop
    def reset_position(self):
        self.goto(0, 0)
        # setting move_speed back to 0.1 when someone doesn't hit the paddle
        self.move_speed = 0.1
        # reversing on the x-axis when ball goes out of bounds instead of starting the same way everytime
        self.bounce_x()
