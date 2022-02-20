
import math

black_color = (0, 0, 0)
background_color = black_color
white_color = (255, 255, 255)

font_alert_size = 50
font_hud_size = 24

initial_snake_direction = (0, -1)


def inverse_color(colors: (int, int, int)) -> (int, int, int):
    return tuple([255 - color for color in colors])


def get_safe_screen_coord(value: float, safe_value: int):
    return math.floor(value / safe_value) * safe_value
