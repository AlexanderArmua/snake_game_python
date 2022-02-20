import pygame
from snake import Snake

snake_movement = {
    'move_up': lambda snake: snake.move_up(),
    'move_down': lambda snake: snake.move_down(),
    'move_right': lambda snake: snake.move_right(),
    'move_left': lambda snake: snake.move_left()
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
