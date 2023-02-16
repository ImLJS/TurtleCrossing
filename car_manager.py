from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.rand_x = 320
        self.rand_y = random.randint(-230, 230)
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.pu()
        self.goto(self.rand_x, 100)
        while self.rand_x != 0:
            self.rand_x -= STARTING_MOVE_DISTANCE
            self.goto(self.rand_x,100)




