from turtle import Turtle
import random

CAR_COLOR = ["green", "pink", "red", "orange", "blue", "yellow"]
CAR_SPEED = 3
SPEED_UP = 10
FONT = ('Arial', 12, 'normal')
class Car():
    def __init__(self):
        self.car_list = []
        self.car_speed = CAR_SPEED

    def create_cars(self):
        number_of_cars = random.randint(1, 6)
        if number_of_cars == 1:
            for i in range(1, number_of_cars + 1):
                car = Turtle("square")
                car.shapesize(1, 1.5)
                car.color(random.choice(CAR_COLOR))
                car.penup()
                car.setheading(180)
                car.goto(300, random.randint(-260, 260))
                self.car_list.append(car)

    def car_move(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += SPEED_UP

    def game_over(self):
        over = Turtle()
        over.hideturtle()
        over.color("black")
        over.penup()
        over.goto(0, 0)
        over.write("GAME OVER", False, "center", FONT)