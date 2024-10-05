from game import *
from bottle import route, run, template, static_file, redirect, get, post, request
from uuid import uuid4
from tinydb import TinyDB, Query
import os
import json



@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')
   
SERVER_PORT = int(os.environ.get('BOTTLE_PORT', 8080))
RELOADER = os.environ.get('BOTTLE_RELOADER', True)

# Initialize database
db = TinyDB("../db.json")
print("db init done")

# Handle main page
@get('/')
def index():
    return template('index.html')

# Handle new game against a friend
@route('/play/friend')
def new_game():
    # Generate a unique game ID
    uuid = str(uuid4())
    # Start a new game with this ID
    game = Game()
    # Save this game to the database
    db.insert({'id': uuid, 'game': game.game_state_to_JSON()})
    # Redirect the user to the game page with the ID
    redirect("/game/{}".format(uuid))

# Handle existing game
@get('/game/<uuid>')
def existing_game(uuid):
    # Read game from the database
    game_state = db.search(Query().id == uuid)
    if(len(game_state) == 0):
        return "Game does not exist"

    curr_game = json.loads(str(game_state[0]['game']))
    game = Game()
    game.game_state_from_data(curr_game["board"], curr_game["player"])

    if game.is_done():
        return "Game over"

    # Prepare data for the template
    template_data = {
        "id": uuid,
        "first": " [] " * game.board[0],
        "second": " [] " * game.board[1],
        "third": " [] " * game.board[2],
        "kljuc": game.player
    }
    return template("game.html", **template_data)

# Handle move
@post('/move/<uuid>')
def make_move(uuid):
    row = request.forms.get('row')
    count = request.forms.get('count')

    # Read game from the database
    game_state = db.search(Query().id == uuid)
    if(len(game_state) == 0):
        return "Game does not exist"
    
    curr_game = json.loads(str(game_state[0]['game']))
    game = Game()
    game.game_state_from_data(curr_game["board"], curr_game["player"])

    # Make the move
    if(game.make_move(int(row), int(count))):
        # Save the new game state in the database
        db.update({'game': game.game_state_to_JSON()}, Query().id == uuid)
        # Redirect the user to the game page with the ID
        redirect("/game/{}".format(uuid))
    else:
        return template('illegal_move.html')
       #return "Illegal move"

@get('/game-state/<uuid>')
def game_state(uuid):
    game_state = db.search(Query().id == uuid)
    if len(game_state) == 0:
        return {"updated": False}
    
    curr_game = json.loads(str(game_state[0]['game']))
    return {
        "updated": True,
        "first": " [] " * curr_game["board"][0],
        "second": " [] " * curr_game["board"][1],
        "third": " [] " * curr_game["board"][2]
    }

# Run the server on the given port, e.g., http://localhost:8080/
if __name__ == "__main__":
    run(host='localhost', port=SERVER_PORT, reloader=RELOADER)
