"""
Main module
Classic Tetris game with play area made out of 10 x 20 square grid
Typical shapes: I, o, L, T, S, Z coded in the model
"""

import pygame
import game.model
import game.window
import game.mechanics


pygame.font.init()


def main():
    """Main function"""
    change_piece: bool = False
    play_game: bool = True
    current_piece = game.model.get_shape()
    next_piece = game.model.get_shape()
    clock = pygame.time.Clock()
    fall_time: int = 0
    score: int = 0
    fall_speed: float = 0.27

    while play_game:

        game.window.GRID = game.window.create_grid(game.window.locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
        # falling piece logic
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y_coordinate += 1
            if not (game.mechanics.valid_space(
                    current_piece, game.window.GRID)) and current_piece.y_coordinate > 0:
                current_piece.y_coordinate -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x_coordinate -= 1
                    if not game.mechanics.valid_space(current_piece, game.window.GRID):
                        current_piece.x_coordinate += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x_coordinate += 1
                    if not game.mechanics.valid_space(current_piece, game.window.GRID):
                        current_piece.x_coordinate -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not game.mechanics.valid_space(current_piece, game.window.GRID):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y_coordinate += 1
                    if not game.mechanics.valid_space(current_piece, game.window.GRID):
                        current_piece.y_coordinate -= 1

                if event.key == pygame.K_SPACE:
                    while game.mechanics.valid_space(current_piece, game.window.GRID):
                        current_piece.y_coordinate += 1
                    current_piece.y_coordinate -= 1

        shape_pos = game.mechanics.convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x_coordinate, y_coordinate = shape_pos[i]
            if y_coordinate > -1:
                game.window.GRID[y_coordinate][x_coordinate] = current_piece.color

        # dropped piece
        if change_piece:
            for pos in shape_pos:
                position = (pos[0], pos[1])
                game.window.locked_positions[position] = current_piece.color
            current_piece = next_piece
            next_piece = game.model.get_shape()
            change_piece = False
            fall_speed -= 0.002
            # call four times to check for multiple clear rows
            score += game.mechanics.clear_rows(game.window.GRID, game.window.locked_positions) * 15

        game.window.draw_window(win, score)
        game.window.draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check if user lost
        if game.mechanics.check_lost(game.window.locked_positions):
            play_game = False

    game.window.draw_text_middle("GAME OVER", 40, game.model.white, win)
    pygame.display.update()
    pygame.time.delay(3000)
    game.window.locked_positions = {}  # reset the grid from the pieces from previous game


def main_menu(window):
    """Display main menu"""
    play_game = True
    while play_game:
        window.fill(game.model.black)
        game.window.draw_text_middle('Press any key to begin.', 60, game.model.white, window)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False

            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()


win = pygame.display.set_mode((game.window.window_width, game.window.window_height))
pygame.display.set_caption('Tetris1.0')

main_menu(win)  # start game
