# Capstone_Turtle_Crossing_Day23
below is a new point：
    def create_cars(self):
# via putting below two lines, when i call this method in main.py inside the loop, everytime, only 1/5 chance that a new car gets created.
# it perfectly controls the traffic volume.
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

# i also need to focus on using constance when creating new classes.