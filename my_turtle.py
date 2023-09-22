from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(5)


    def reset_position(self):
        self.goto(0, -280)
