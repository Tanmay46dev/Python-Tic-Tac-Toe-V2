from utils import *


def main():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    print("Welcome to a game of TicTacToe. You are 'X'. Enjoy!")
    print("Here is your TicTacToe board. Start playing!")

    while True:
        print_board(board)
        # User move
        while True:
            pos = get_valid_pos_input()
            row, col = get_row_col_from_pos(pos)
            if is_pos_empty(board, row, col):
                break
            else:
                print("Position is already filled. Please enter a valid position!")
        place_piece(board, "X", row, col)

        result = handle_game_result(board)
        if result:
            print(result)
            break

        # Computer move
        while True:
            row, col = get_random_row_col()
            if is_pos_empty(board, row, col):
                place_piece(board, "O", row, col)
                break

        result = handle_game_result(board)
        if result:
            print(result)
            break

    print_sep()


if __name__ == '__main__':
    main()
