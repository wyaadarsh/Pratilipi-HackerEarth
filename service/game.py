from service.Board import Board
from enum import Enum
from utils.db_utils import GameModel


class Player(Enum):
    YELLOW = 1
    RED = 2


class Game:

    def __init__(self, id, board_state=None, turn=Player.YELLOW.value):
        self.id = id
        self.board = Board(board_state)
        self.turn = turn

    def play(self, col):
        # return: winning_move, next_player, winner
        winning_move = self.board.play_and_check_win(col, self.turn)
        current_player = self.turn
        if self.turn == Player.YELLOW.value:
            self.turn = Player.RED.value
        else:
            self.turn = Player.YELLOW.value
        if winning_move:
            return winning_move, self.turn, current_player
        return winning_move, self.turn, None

    def print_state(self):
        return self.board.get_board()
