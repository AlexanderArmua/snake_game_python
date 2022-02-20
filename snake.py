import random

class Positionable:
    def __init__(self, position_x: int = 0, position_y: int = 0):
        self.position_x = position_x
        self.position_y = position_y

    def get_position(self) -> (int, int):
        return self.position_x, self.position_y


class Snake(Positionable):
    def __init__(self, length: int, speed: int, position_x: int = 0, position_y: int = 0):
        Positionable.__init__(self, position_x, position_y)
        self.length = length
        self.speed = speed
        self.direction = (0, -1)
        self.color = (0, 0, 255)

    def move(self):
        self.position_x += self.direction[0] * self.speed
        self.position_y += self.direction[1] * self.speed

    def move_up(self): self.direction = (0, -1)
    def move_down(self): self.direction = (0, 1)
    def move_left(self): self.direction = (-1, 0)
    def move_right(self): self.direction = (1, 0)

    def get_length(self):
        return self.length

    def increase_speed(self, new_speed):
        self.speed += new_speed

    def set_new_color(self, color):
        self.color = color

    def set_random_color(self):
        self.set_new_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


class Block(Positionable):
    def __init__(self, position_x: int = 0, position_y: int = 0):
        Positionable.__init__(self, position_x, position_y)
