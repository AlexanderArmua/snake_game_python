
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
from snake import Snake
from controls import actions, snake_can_move
from game import Game


def init_game(game):
    pygame.init()

    display_screen = pygame.display.set_mode(game.screen_size)

    font_message = pygame.font.SysFont('', 50)
    font_hud = pygame.font.SysFont('', 24)

    pygame.display.update()

    pygame.display.set_caption('Snake en Sea of Silver')

    game.display = display_screen
    game.font_message = font_message
    game.font_hud = font_hud


def close_game():
    pygame.quit()
    quit()


def should_close_game(event) -> bool:
    has_clicked_quit = event.type == pygame.QUIT
    has_pressed_esc = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE

    return has_clicked_quit or has_pressed_esc


def handle_keys_down(event, snake, game) -> bool:
    if event.key in actions:
        actions[event.key](snake)
        return True
    elif event.key == pygame.K_q:
        game.add_points()

    return False


def set_main_message(game, msg, color):
    message = game.font_message.render(msg, True, color)

    message_x = game.screen_x() / 2 - message.get_width() / 2
    message_y = game.screen_y() / 2 - message.get_height()

    game.display.blit(message, [message_x, message_y])


def set_points_message(game, color):
    message = game.font_hud.render(f"Points: {game.points}", True, color)

    message_x = game.pixel_size * 2
    message_y = game.pixel_size * 2

    game.display.blit(message, [message_x, message_y])


def draw_snake(game, display_screen, snake):
    set_points_message(game, snake.color)
    pygame.draw.rect(display_screen, snake.color, [*snake.get_position(), game.pixel_size, game.pixel_size])
    pygame.display.update()


def run_game(game):
    snake = Snake(3, game.pixel_size, 50, 50)

    clock = pygame.time.Clock()

    while game.get_game_running():
        for event in pygame.event.get():
            if should_close_game(event):
                game.set_game_running(False)
            elif event.type == pygame.KEYDOWN:
                handle_keys_down(event, snake, game)

        game.display.fill((0, 0, 0))

        if snake_can_move(snake, game.pixel_size, *game.screen_size):
            snake.move()
        else:
            snake.set_random_color()
            set_main_message(game, f"You crashed at {snake.get_position()}", snake.color)

        draw_snake(game, game.display, snake)
        timer = game.get_level()
        clock.tick(timer)


if __name__ == '__main__':
    current_game = Game()
    init_game(current_game)
    run_game(current_game)
    close_game()
