import random

FPS = 60
CELL_SIZE = 200
WINDOW_WIDTH, WINDOW_HEIGHT = CELL_SIZE * 3, CELL_SIZE * 3

PIECE_FONT_SIZE = 128

BG_COLOR = "#A0B2A6"
PRIMARY_COLOR = (64, 61, 88)
HOVER_BG_COLOR = "#61988E"


def print_sep():
    print("-" * 30)


def get_random_row_col() -> tuple:
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    return row, col
        

def is_pos_empty(board: list[list[str]], row: int, col: int):
    return board[row][col] == " "


def print_board(board: list[list[str]]) -> None:
    for row in board:
        print("|".join(row), end="")
        print()


def is_board_filled(board: list[list[str]]) -> bool:
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def place_piece(board: list[list[str]], piece: str, row: int, col: int) -> None:
    board[row][col] = piece


def check_win(board: list[list[str]]) -> tuple:
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True, row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True, board[0][2]

    return False, None


def get_valid_pos_input():
    try:
        user_input = int(input("Enter a number between 1 and 9: "))
        if 1 <= user_input <= 9:
            return user_input
        else:
            print("Please enter a number between 1 and 9.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


def get_row_col_from_pos(pos: int) -> tuple:
    row = 0
    col = 0
    if pos <= 3:
        row = 0
        col = pos - 1
    elif pos <= 6:
        row = 1
        col = pos - 3 - 1
    else:
        row = 2
        col = pos - 6 - 1

    return row, col


def handle_game_result(board):
    is_winner, winner_piece = check_win(board)
    if is_winner:
        return f"Winner: {winner_piece}"
    elif is_board_filled(board):
        return "It's a tie."
    return ""
