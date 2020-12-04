#!/usr/bin/env python
# encoding: utf-8

"""
Service interface for Connect4 - Pratilipi
"""

import settings
from flask import (Flask, request, make_response, render_template)
from service.rest_util import *
from utils.exceptions import InvalidMoveException

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('README.html')


@app.route('/START/', methods=['POST'])
def start_new_game():
    try:
        game_id = create_new_game()
    except:
        return make_response({"success": False, "error_code": 400})
    return make_response({"status": "READY", "id": game_id})


@app.route('/game/', methods=['POST'])
def play_game():
    try:
        game_data = request.json
        game_id = game_data['id']
        col = game_data['col']
        return_obj = play(game_id, col)
        return_obj["success"] = True
    except InvalidMoveException:
        return make_response({"success": False, "error_code": 400, "message": "Invalid Move"})
    except:
        return make_response({"success": False, "error_code": 410, "message": "Insufficient Payload"})
    return make_response(return_obj)


@app.route('/game2/<id>/<col>', methods=['GET'])
def play_game2(id, col):
    try:
        game_data = request.json
        game_id = game_data['id']
        col = game_data['col']
        return_obj = play(game_id, col)
        return_obj["success"] = True
    except InvalidMoveException:
        return make_response({"success": False, "error_code": 400, "message": "Invalid Move"})
    except:
        return make_response({"success": False, "error_code": 410, "message": "Insufficient Payload"})
    return make_response(return_obj)


@app.route('/game/<id>/', methods=['GET'])
def get_game(id):
    try:
        current_state, move_history = get_game_state(id)
    except:
        return make_response({"success": False, "error_code": 410, "message": "Invalid Argument/Game Not Found"})
    return make_response({"success": True, "current_state": current_state, "move_history": move_history})


if __name__ == '__main__':
    app.run(
        host=settings.SERVICE_IP,
        port=settings.SERVICE_PORT
    )
