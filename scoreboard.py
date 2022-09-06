from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


# defining a class to keep score, making sure score goes to top (with goto) center and the color can be seen
# identifying that the score is zero at first and writing it as such
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        # establishing the left and right score starts at 0
        self.r_score = 0
        self.l_score = 0
        # putting the function update_scoreboard in the __init__ gives the scoreboard all the turtle properties
        # already established above so it will show up on screen
        self.update_scoreboard()

    # adding the scores to the top of page with the coordinates given
    def update_scoreboard(self):
        self.goto(-100, 250)
        self.write(f"Score: {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(f"Score: {self.r_score}", align=ALIGNMENT, font=FONT)

    # defining increase score so the score can add 1 when ball goes past paddle, clear the previous score to write
    # new score
    def left_increase_score(self):
        self.l_score += 1
        self.clear()

    def right_increase_score(self):
        self.r_score += 1
        self.clear()


