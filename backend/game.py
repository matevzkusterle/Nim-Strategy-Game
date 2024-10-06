import json

class Game:
  board = [3,5,7]
  player = 0 #ga samo spreminjaš iz 0 na 1, kdo je na vrsti

  def __init__(self):
    print("initing")

  def is_legal_move(self, row, count):
    # precekiraj ce je ok vrsitca
    if row < 0 or row > 2:
      return False

    # precekirej ce je dost listkov v vrstici da jih odstejes
    if self.board[row] < count:
      return False
    
    # ok je
    return True

  def make_move(self,row, count):
    if(self.is_legal_move(row, count)):
      self.board[row] -= count
      self.player = (self.player + 1) % 2  #premetavanje iz 0 na 1 in obratno
      return True
    return False
  
  def is_done(self):
    """
    preveri ce je igra koncana
    """
    if (sum(self.board) == 1):
      return True
    return False

  def game_state_to_JSON(self):
    """
    vrni JSON string, ki predstavlja trenutno stanje igre
    """
    state = {
      "board": self.board,
      "player": self.player
    }
    return json.dumps(state)  #returni json strig ane

  def game_state_from_data(self, board, player):
    """
    nastavi stanje igre iz podatkov
    """
    try:
      self.board = board
      self.player = player
      return True
    except:
      return False

  def get_best_move(self):
    """
    vrni najboljšo legalno potezo
    """
    #make a copy of the board
    cp = self.board[:]

    for row in range(3):
      for count in range(1, cp[row] + 1):
        
        if cp[row] < count:
          continue
        cp[row] -= count

        res = cp[0] ^ cp[1] ^ cp[2]  # XOR operacija

        if res == 0:  # popravljeno, da preveri, če je res == 0
          return (row, count)

        cp[row] += count

    #če ni nobene take poteze, vzemi eno iz neprazne vrstice
    for row in range(3):
      if cp[row] > 0:
        return (row, 1)
  #     
  #   če pa pač ni nobene take ki bi bila == 0, pa samo iz ene neprazne vzami enega

  def __repr__(self):
    """
    vrni string, ki predstavlja class Game
    """
    out = ""
    out += "Fist line" + "\n"
    out += (" [] "*self.board[0]) + "\n"
    out += "Second line" + "\n"
    out += (" [] "*self.board[1]) + "\n"
    out += "Third line" + "\n"
    out += (" [] "*self.board[2])
    return(out)

if __name__ == "__main__":
  game = Game()
  print(game)

  while  not game.is_done():
    row = int(input("Vnesi vrstico: "))
    count = int(input("Vnesi stevilo listkov: "))
    game.make_move(row, count)
    print(game)
    print("-----------------")

    print("\n enemy \n")
    # enemy move
    row, count = game.get_best_move()
    game.make_move(row, count)
    print(game)
    print("-----------------")
