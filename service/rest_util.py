import json

from service.game import Game
from uuid import uuid4

from utils.exceptions import InvalidArgumentException

game = {}


def create_new_game():
    game_id = uuid4()
    game[str(game_id)] = Game(game_id)
    return game_id


def play(game_id, col):
    return game[game_id].play(col)


def get_game_state(game_id):
    if game_id not in game:
        raise InvalidArgumentException
    return json.dumps(game[game_id].print_state()), None