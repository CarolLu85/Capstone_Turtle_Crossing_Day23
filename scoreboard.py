from turtle import Turtle
FONT = ('Arial', 12, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-260, 260)
        self.point = 0
        self.scores()
        self.over = Turtle()

    def scores(self):
        self.write(f"level: {self.point} ", False, "center", FONT)


    def score_update(self):
        self.clear()
        self.point += 1
        self.write(f"level: {self.point} ", False, "center", FONT)



