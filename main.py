
"""
1. 2D Library
2. Dibujar un cuadrado vacio
3. Dibujar el puntaje actual y el tiempo
4. Crear un contador
5. Incrementar el puntaje por cada bicho atrapado
6. Calcular la velocidad segun el puntaje
7. Generar un bloque al azar dentro del mapa
8. Generar una serpiente de 3 bloques
9. Programar el movimiento hacia arriba
10. Programar el movimiento hacia abajo
11. Programar el movimienzo hacia izquierda y derecha
12. Detectar cuando la serpiente toca el objeto
13. Desaparecer el objeto cuando toca la serpiente
14. Incrementar el tamanno de la serpiente
15. Ajustar la velocidad de la serpiente a la velocidad
16. Detectar cuando la serpiente colisiona con una pared
17. Detectar cuando la serpiente colisiona contra si misma
18. Al detectar colision mostrar un mensaje con el puntaje
19. Reiniciar el juego
"""

import pygame
from snake import Snake, Block
from controls import actions, snake_can_move
from game import Game
from configs import background_color, inverse_color, font_alert_size, font_hud_size


def init_game(game: Game):
    pygame.init()

    display_screen = pygame.display.set_mode(game.screen_size)

    font_message = pygame.font.SysFont('', font_alert_size)
    font_hud = pygame.font.SysFont('', font_hud_size)
    clock = pygame.time.Clock()

    pygame.display.update()

    pygame.display.set_caption('Snake en Sea of Silver')

    game.display = display_screen
    game.font_message = font_message
    game.font_hud = font_hud
    game.clock = clock


def close_game():
    pygame.quit()
    quit()


def should_close_game(event) -> bool:
    has_clicked_quit = event.type == pygame.QUIT
    has_pressed_esc = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

    return has_clicked_quit or has_pressed_esc


def handle_keys_down(event, snake: Snake, game: Game) -> bool:
    if event.key in actions:
        actions[event.key](snake)
        return True
    elif event.key == pygame.K_q:
        game.add_points()

    return False


def set_main_message(game: Game, msg: str, color: (int, int, int)):
    message = game.font_message.render(msg, True, color)

    message_x = game.screen_x() / 2 - message.get_width() / 2
    message_y = game.screen_y() / 2 - message.get_height()

    game.display.blit(message, [message_x, message_y])


def draw_points_message(game: Game, snake: Snake):
    message_color = inverse_color(snake.color)
    message = game.font_hud.render(f"Points: {game.points} - {snake.get_position()}", True, message_color)

    game.display.blit(message, [game.pixel_size] * 2)


def handle_pygame_events(game: Game, snake: Snake):
    for event in pygame.event.get():
        if should_close_game(event):
            game.set_game_running(False)
        elif event.type == pygame.KEYDOWN:
            handle_keys_down(event, snake, game)


def handle_snake_movement(game: Game, snake: Snake):
    if snake_can_move(snake, game.pixel_size, *game.screen_size):
        snake.move()
    else:
        snake.set_random_color()
        set_main_message(game, f"You crashed at {snake.get_position()}", snake.color)

    pygame.draw.rect(game.display, snake.color, [*snake.get_position(), *([game.pixel_size] * 2)])


def handle_interaction_between_snake_and_block(game: Game, snake: Snake, block: Block):
    if snake.get_position() == block.get_position():
        game.add_points(5)
        block.move_to_random_coords()

    block_x = block.position_x + game.pixel_size / 2
    block_y = block.position_y + game.pixel_size / 2

    pygame.draw.circle(game.display, block.color, [block_x, block_y], game.pixel_size / 2)


def run_game(game: Game):
    snake = Snake(3, game.pixel_size, *game.screen_center_rounded())

    block = Block(inverse_color(snake.color), game.pixel_size, game.screen_x(), game.screen_y())

    while game.get_game_running():
        handle_pygame_events(game, snake)

        game.display.fill(background_color)

        handle_snake_movement(game, snake)

        handle_interaction_between_snake_and_block(game, snake, block)

        draw_points_message(game, snake)

        pygame.display.update()

        game.clock.tick(game.get_level())


if __name__ == '__main__':
    current_game = Game()
    init_game(current_game)
    run_game(current_game)
    close_game()
