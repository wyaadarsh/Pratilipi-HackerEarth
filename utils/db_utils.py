from settings import *
from pymongo import MongoClient
from utils.exceptions import IDNeededException, InvalidGameIDException
from utils.singleton_util import SingletonFactory


class MongoAccess(metaclass=SingletonFactory):

    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[PRATILIPI_DB]


class SessionManager:
    pass


class GameModel:

    def __init__(self):
        self.client = MongoAccess()
        self.GAME_TABLE = self.client.db[GAME_TABLE]

    def insert(self, game_id, board_state, next_turn=1):
        game_object = {
            "_id": game_id,
            "board_state": board_state,
            "moves": [],
            "next_turn": next_turn,
            "moves_count": 0
        }
        self.GAME_TABLE.insert(game_object)

    def update(self, game_id, board_state, move, next_turn, winner=None, game_over=False):
        game_object = {
            "_id": game_id
        }
        update_object = {
            "$addToSet": {"moves": move},
            "$set": {
                "board_state": board_state,
                "next_turn": next_turn,
                "winner": winner,
                "game_over": game_over
            },
            "$inc": {"moves_count": 1}
        }
        self.GAME_TABLE.update(game_object, update_object)
        pass

    def get_game_state(self, game_id):
        res = self.GAME_TABLE.find({"_id": game_id})
        if not res:
            raise InvalidGameIDException
        for r in res:
            return r.get('board_state'), r.get('moves'), r.get('next_turn'), r.get('moves_count')
