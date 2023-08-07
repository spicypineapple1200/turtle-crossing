import time
import turtle
import turtle as t
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_turtle = Player()
screen.listen()
score = Scoreboard()
screen.onkeypress(game_turtle.movement, "Up")
loop = 1

cars = []

BIG_TIME = 0.1

game_is_on = True
while game_is_on:
    loop -= 1
    time.sleep(BIG_TIME)
    screen.update()
    if loop == 0:
        car = CarManager()
        cars.append(car)
        loop = 6

    for car in cars:
        car.car_movement()
        if car.distance(game_turtle) < 20:
            game_is_on = False
            score.game_over()
    if game_turtle.ycor() > 280:
        score.level_up()
        BIG_TIME *= 0.9
        game_turtle.goto(0, -280)


screen.exitonclick()