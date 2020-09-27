from service.Board import Board
from enum import Enum


class Player(Enum):
    YELLOW = 1
    RED = 2


class Game:

    def __init__(self, id):
        self.id = id
        self.board = Board()
        self.turn = Player.YELLOW

    def play(self, col):
        winning_move = self.board.play_and_check_win(col, self.turn.value)
        if winning_move:
            return winning_move, self.turn
        if self.turn == Player.YELLOW:
            self.turn = Player.RED
        else:
            self.turn = Player.YELLOW
        return winning_move, None

    def print_state(self):
        return self.board.get_board()
