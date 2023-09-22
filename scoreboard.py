from turtle import Turtle
FONT = ('Courier', 12, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-250, 260)
        self.point = 0
        self.scores()



    def scores(self):
        self.write(f"Score: {self.point} ", False, "center", FONT)
    #
    #
    def score_update(self):
        self.clear()
        self.point += 1
        self.scores()
    #
    #
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
#    without a clear() method, this "GAME OVER" will just go to the coordinates assigned to it with the "Score:" left on the left corner
#   of the screen.
