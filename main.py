from turtle import Turtle,Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600 , height = 600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up , "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_generation()
    car_manager.move_cars()
   #detect collision 
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

    # detect a succefull crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        score_board.update_level()


screen.exitonclick()


    


