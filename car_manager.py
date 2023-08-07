import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLORS[random.randint(0, 5)])
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(300, random.randint(-250, 250))

    def car_movement(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def car_speedup(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT