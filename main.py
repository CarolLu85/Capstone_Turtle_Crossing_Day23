from turtle import Turtle, Screen
import time
import car
from my_turtle import MyTurtle
from car import Car
from scoreboard import ScoreBoard


# create objects
player = MyTurtle()
cars = Car()
screen = Screen()
scoreboard = ScoreBoard()

# setup the screen
screen.bgcolor("white")
screen.setup(600, 600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

player_score = 0
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    cars.create_cars()
    cars.car_move()
    if player.ycor() > 280:
        player.reset_position()
        player_score = scoreboard.score_update()
        cars.speed_up()

    for car_object in cars.car_list:
        if player.distance(car_object) <= 23:
            game_on = False
            cars.game_over()
            print("Over")

screen.exitonclick()
