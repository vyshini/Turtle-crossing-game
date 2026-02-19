from turtle import Turtle

STARTING_POSITION = (0,-250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(10)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y :
            return True
        else:
            return False
        
    def goto_start(self):
        self.goto(STARTING_POSITION)

