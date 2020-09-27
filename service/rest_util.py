import json

from service.game import Game
from uuid import uuid4

from utils.db_utils import GameModel
from utils.exceptions import InvalidArgumentException

game = {}


def create_new_game():
    game_id = str(uuid4())
    game_obj = Game(game_id)
    game[str(game_id)] = game_obj
    GameModel().insert(game_id, game_obj.board.board, game_obj.turn)
    return game_id


def play(game_id, col):
    game_state, _, next_turn, moves_count = GameModel().get_game_state(game_id)
    game_obj = Game(game_id, board_state=game_state, turn=next_turn)
    winning_move, next_player, winner = game_obj.play(col)
    moves = "Move: {}, COL: {}  PLAYED BY: {}".format(moves_count+1, col, "YELLOW" if next_turn == 1 else "RED")
    GameModel().update(game_id, game_obj.board.board, moves, next_player, winner, winning_move)
    return winning_move, winner


def get_game_state(game_id):
    game_state, moves, _, _ = GameModel().get_game_state(game_id)
    game_obj = Game(game_id, board_state=game_state)
    return json.dumps(game_obj.print_state()), moves