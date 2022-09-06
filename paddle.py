from turtle import Turtle


# creating Paddle class by taking all Turtle attributes
class Paddle(Turtle):
    # position is going to tell where each paddle goes to according to the position addressed in main.py under
    # l_paddle, and r_paddle...position here is the input and the coordinates in main.py is the output
    def __init__(self, position):
        # when taking from a parent have to add super class
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        # to get 20 width x 100 length, all turtles start off 20 x 20 so stretch width by 5 and length by 1 to make
        # it 100 x 20
        self.shapesize(stretch_wid=5, stretch_len=1)
        # position starts at x=0 and y=0 so goto is to get it to move to the position you of 350 on x-axis and 0 on
        # y-axis
        self.goto(position)

    # creating up and down motion, x-axis will stay at 0 because we are only moving up and down y-axis
    def go_up(self):
        # getting new y coordinate going up by 20
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # same thing as go_up except you are going down which will be in negatives, so you subtract 20
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




