import random
from configs import initial_snake_direction, get_safe_screen_coord

DIRECTION_UP = (0, -1)
DIRECTION_DOWN = (0, 1)
DIRECTION_RIGHT = (1, 0)
DIRECTION_LEFT = (-1, 0)


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
        self.direction = initial_snake_direction
        self.color = None
        self.set_random_color()

    def move(self):
        self.position_x += self.direction[0] * self.speed
        self.position_y += self.direction[1] * self.speed

    def move_up(self): self.direction = DIRECTION_UP
    def move_down(self): self.direction = DIRECTION_DOWN
    def move_right(self): self.direction = DIRECTION_RIGHT
    def move_left(self): self.direction = DIRECTION_LEFT

    def get_length(self):
        return self.length

    def increase_speed(self, new_speed: int):
        self.speed += new_speed

    def set_new_color(self, color: (int, int, int)):
        self.color = color

    def set_random_color(self):
        self.set_new_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


class Block(Positionable):
    def __init__(self, color: (int, int, int), pixel_size: int, max_x: int, max_y: int):
        Positionable.__init__(self, 0, 0)
        self.pixel_size = pixel_size
        self.max_x = max_x
        self.max_y = max_y
        self.color = color
        self.move_to_random_coords()

    def set_color(self, color: (int, int, int)):
        self.color = color

    def move_to_random_coords(self):
        self.position_x = get_safe_screen_coord(random.randint(0, self.max_x - self.pixel_size), self.pixel_size)
        self.position_y = get_safe_screen_coord(random.randint(0, self.max_y - self.pixel_size), self.pixel_size)

