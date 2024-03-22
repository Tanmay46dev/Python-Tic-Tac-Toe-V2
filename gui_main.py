import pygame
from utils import *
import os


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("TicTacToe!")
        self.clock = pygame.time.Clock()
        self.board = [[" " for _ in range(3)] for _ in range(3)]


        self.click_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "click.wav"))
        self.x_image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "X.png")), (160, 160))
        self.o_image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "O.png")), (160, 160))

        self.piece_font = pygame.font.SysFont("", PIECE_FONT_SIZE)

        self.result_font = pygame.font.SysFont("", 100)
        self.result_text = ""
        self.result_popped_up = False

        # When a cell is hovered over draw this rect at that pos
        self.highlighted_rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.result_popped_up = False
        self.result_text = ""


    def draw_lines(self):
        # Vertical lines
        for i in range(CELL_SIZE, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, PRIMARY_COLOR, (i, 0), (i, WINDOW_HEIGHT), 2)

        for i in range(CELL_SIZE, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, PRIMARY_COLOR, (0, i), (WINDOW_WIDTH, i), 2)

    def draw_pieces(self):
        for row in range(3):
            for col in range(3):
                CELL_IMAGE_SIZE_DIFF = CELL_SIZE - self.x_image.get_size()[0]
                x_center = (col * CELL_SIZE) + (CELL_IMAGE_SIZE_DIFF // 2)
                y_center = (row * CELL_SIZE) + (CELL_IMAGE_SIZE_DIFF // 2)
                
                piece = self.board[row][col]
                if piece == "X":
                    self.screen.blit(self.x_image, (x_center, y_center))
                elif piece == "O":
                    self.screen.blit(self.o_image, (x_center, y_center))



    def draw(self):
        self.screen.fill(BG_COLOR)
        pygame.draw.rect(self.screen, HOVER_BG_COLOR, self.highlighted_rect)
        self.draw_lines()
        self.draw_pieces()
        if self.result_text:
            # self.screen.fill(BG_COLOR)
            self.screen.blit(self.result_font.render(self.result_text, True, "#26408B"), (150, 220))
            self.result_popped_up = True
        pygame.display.update()


    def play_move(self, row, col):
        if is_pos_empty(self.board, row, col):
            place_piece(self.board, "X", row, col)
            self.result_text = handle_game_result(self.board)
            if not self.result_text:
                while True:
                    row2, col2 = get_random_row_col()
                    if is_pos_empty(self.board, row2, col2):
                        place_piece(self.board, "O", row2, col2)
                        self.result_text = handle_game_result(self.board)
                        break

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                
                # Get mouse position and highlight the cell that is hovered over currently
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // CELL_SIZE
                col = mouse_x // CELL_SIZE
                self.highlighted_rect.left = col * CELL_SIZE
                self.highlighted_rect.top = row * CELL_SIZE

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Game logic
                        self.click_sound.play()
                        if not self.result_popped_up:
                            self.play_move(row, col)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
            self.draw()
            


if __name__ == '__main__':
    Game().run()
