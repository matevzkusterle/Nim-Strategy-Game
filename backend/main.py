from game import *
from bottle import route, run, template, static_file, redirect, get, post, request, response
from uuid import uuid4
from tinydb import TinyDB, Query
import os


def better_static_file(filename, root, obj):
  with open(os.path.join(root,filename), "r") as f:
    f = f.read()
    for k in obj.keys():
      f = f.replace("{{"+k+"}}", obj[k])
    return f
   
ROOT = "D:\Matevz\Desktop\projekt\src"

# init database
db = TinyDB("../../db.json")
print("db init done")

# handle main page
@get('/')
def index():
    return static_file("frontend/index.html", root=ROOT)

# handle new game
@route('/new')
def new_game():
    # zgeneriri unikatn game ID 
    uuid = str(uuid4())
    # začni igro z tem IDjem
    game = Game()
    # shrani to igro v bazo
    db.insert({'id': uuid, 'game': game.game_state_to_JSON()})
    # preusmeri userja na stran z igro z idjem
    redirect("/game/{}".format(uuid))

# handle existing game
@get('/game/<uuid>')
def new_game(uuid):
    # preberi igro iz baze
    # game = Game()
    game_state = db.search(Query().id == uuid)
    if(len(game_state) == 0):
        return "Game does not exist"

    curr_game =json.loads(str( game_state[0]['game']))
    game = Game()
    game.game_state_from_data(curr_game["board"],curr_game["player"] )

    if game.is_done():
        return("konec lonec")

    # pripravi podatke za template
    template = {
      "id":uuid,
      "first":" [] " * game.board[0],
      "second":" [] " * game.board[1],
      "third":" [] " * game.board[2],
      "kljuc": "PRAVILA IGRE: Igralca izmenično odstranjujeta žetone. Igralec lahko vzame poljublno mnogo žetenov, vendar le iz ene vrstice. Zmagovalec je tisti, ki prepusti nasprotniku zadnji žeton (torej zgubi tisti, ki mu ostane zadnji žeton)."
    }
    return better_static_file("frontend/game.html", ROOT, template)

    print()

# handle move
@post('/move/<uuid>')
def make_move(uuid):
    row = request.forms.get('row')
    count = request.forms.get('count')

    # preberi igro iz baze
    game_state = db.search(Query().id == uuid)
    if(len(game_state) == 0):
        return "Game does not exist"
    
    curr_game =json.loads(str( game_state[0]['game']))
    game = Game()
    game.game_state_from_data(curr_game["board"],curr_game["player"] )

    # make moves
    if(game.make_move(int(row), int(count))):
        # shrani novo stanje igre v bazo
        db.update({'game': game.game_state_to_JSON()}, Query().id == uuid)
        # preusmeri userja na stran z igro z idjem
        redirect("/game/{}".format(uuid))
    else:
        return "Illegal move"


run(host='0.0.0.0', port=8000)