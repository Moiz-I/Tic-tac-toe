my_board = [
	["1", "2", "X"],
	["4", "5", "6"],
	["7", "8", "9"]
]


class Tictactoe():
  def __init__(self, board):
    self.board = board
  
  def print_board(self):
    print("|-------------|")
    print("| Tic Tac Toe |")
    print("|-------------|")
    print("|             |")
    print("|    " + self.board[0][0] + " " + self.board[0][1] + " " + self.board[0][2] + "    |")
    print("|    " + self.board[1][0] + " " + self.board[1][1] + " " + self.board[1][2] + "    |")
    print("|    " + self.board[2][0] + " " + self.board[2][1] + " " + self.board[2][2] + "    |")
    print("|             |")
    print("|-------------|")
    print()

  def available_moves(self):
    moves = []
    for row in self.board:
      for col in row:
        if col != "X" and col != "O":
          moves.append(int(col))
    return moves

  def select_space(self, move, turn):
    row = (move-1)//3
    col = (move-1)%3
    self.board[row][col] = "{}".format(turn)

  def has_won(self, player):
    for row in self.board:
        if row.count(player) == 3:
            return True
    for i in range(3):
        if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
            return True
    if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
        return True
    if self.board[0][2] == player and self.board[1][1] == player and board[2][0] == player:
        return True
    return False
  
  def game_over(self):
    self.available_moves()
    if self.has_won("X") or self.has_won("O") or len(self.available_moves()) ==0:
      return True
    else:
      return False

  def get_player_move(self, turn):
    move = int(input("Player {player} make your turn: ".format(player=turn)))
    self.available_moves()
    while move not in range (1,10) or move not in self.available_moves():
      move = int(input("Invalid move, try again: "))
    return move
      

     
def game(board):
  tictactoe = Tictactoe(my_board)
  while not tictactoe.game_over():
    tictactoe.print_board()
    x_move = tictactoe.get_player_move("X")
    tictactoe.select_space(x_move,"X")
    tictactoe.print_board()
    if tictactoe.game_over():
      break

    o_move = tictactoe.get_player_move("O")
    tictactoe.select_space(o_move,"O")
  if tictactoe.has_won("X"):
    print("X wins")
  elif tictactoe.has_won("O"):
    print("O wins")
  else:
    print("tie")



game(my_board)
