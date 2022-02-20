import math
from configs import get_safe_screen_coord


class Game:
    def __init__(self):
        self.points = 30
        self.game_running = True
        self.game_closed = False
        self.pixel_size = 30
        self.screen_size = (640, 480)
        self.increase_level_every_n_points = 5
        self.display = None
        self.font_message = None
        self.font_hud = None
        self.clock = None

    def get_game_running(self): return self.game_running

    def set_game_running(self, game_running: bool): self.game_running = game_running

    def get_level(self):
        return math.ceil(max(self.points, 1) / self.increase_level_every_n_points)

    def add_points(self, points: int = 1):
        self.points += points

    def screen_x(self):
        return self.screen_size[0]

    def screen_y(self):
        return self.screen_size[1]

    def screen_center_rounded(self):
        screen_x_half = get_safe_screen_coord(self.screen_x() / 2, self.pixel_size)
        screen_y_half = get_safe_screen_coord(self.screen_y() / 2, self.pixel_size)

        return screen_x_half, screen_y_half
