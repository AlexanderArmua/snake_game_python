import pygame
from snake import Snake
from configs import DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_UP


def snake_can_go_back(snake: Snake, new_direction: (int, int)):
    if len(snake.tail) == 1:
        return True
    elif tuple(map(sum, zip(snake.direction, new_direction))) == (0, 0):
        return False

    return True


snake_movement = {
    'move_up': lambda snake: snake.move_up() if snake_can_go_back(snake, DIRECTION_UP) else None,
    'move_down': lambda snake: snake.move_down() if snake_can_go_back(snake, DIRECTION_DOWN) else None,
    'move_right': lambda snake: snake.move_right() if snake_can_go_back(snake, DIRECTION_RIGHT) else None,
    'move_left': lambda snake: snake.move_left() if snake_can_go_back(snake, DIRECTION_LEFT) else None
}

actions = {
    pygame.K_UP: snake_movement['move_up'],
    pygame.K_w: snake_movement['move_up'],
    pygame.K_DOWN: snake_movement['move_down'],
    pygame.K_s: snake_movement['move_down'],
    pygame.K_RIGHT: snake_movement['move_right'],
    pygame.K_r: snake_movement['move_right'],
    pygame.K_LEFT: snake_movement['move_left'],
    pygame.K_l: snake_movement['move_left']
}


def snake_can_move(snake: Snake, pixel_size: int, screen_x: int, screen_y: int) -> bool:
    next_y = snake.position_y + pixel_size
    next_x = snake.position_x + pixel_size

    if snake.direction == (0, -1):
        return next_y > 0 + pixel_size
    elif snake.direction == (0, 1):
        return (next_y + pixel_size) <= screen_y
    elif snake.direction == (-1, 0):
        return next_x > 0 + pixel_size
    elif snake.direction == (1, 0):
        return (next_x + pixel_size) <= screen_x
