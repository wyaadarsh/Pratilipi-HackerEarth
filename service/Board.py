from utils.exceptions import *

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = [[0 for j in range(COLUMN_COUNT)] for i in range(ROW_COUNT)]
    return board


class Board:

    def __init__(self, board_state=None):
        if board_state:
            self.board = board_state
        else:
            self.board = create_board()

    def play(self, col, piece):
        if self.is_valid_location(col):
            row = self.get_next_open_row(col)
            self.drop_piece(row, col, piece)
        else:
            raise InvalidMoveException

    def play_and_check_win(self, col, piece):
        self.play(col, piece)
        return self.winning_move(piece)

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[ROW_COUNT - 1][col] == 0

    def get_next_open_row(self, col):
        for r in range(ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def print_board(self):
        print(self.board[::-1])

    def get_board(self):
        return self.board[::-1]

    def winning_move(self, piece):
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece and \
                        self.board[r][c + 1] == piece and \
                        self.board[r][c + 2] == piece and \
                        self.board[r][c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == piece and \
                        self.board[r + 1][c] == piece and \
                        self.board[r + 2][c] == piece and \
                        self.board[r + 3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == piece and \
                        self.board[r + 1][c + 1] == piece and \
                        self.board[r + 2][c + 2] == piece and \
                        self.board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if self.board[r][c] == piece and \
                        self.board[r - 1][c + 1] == piece and \
                        self.board[r - 2][c + 2] == piece and \
                        self.board[r - 3][c + 3] == piece:
                    return True

        return False


if __name__ == "__main__":
    b = Board()
    turn = 0
    while True:
        try:
            b.get_board()
            col = int(input())
            b.play(col, turn + 1)
            if b.winning_move(turn + 1):
                print("{} Won".format(turn + 1))
                break
            turn += 1
            turn = turn % 2
        except:
            print("Invalid move")
