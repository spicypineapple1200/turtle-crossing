import turtle as t
import car_manager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("black")
        self.goto(0, -280)

    def movement(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def game_win(self):
        if self.ycor() > FINISH_LINE_Y:
            global MOVE_DISTANCE
            MOVE_DISTANCE += 10
            self.goto(0, -280)