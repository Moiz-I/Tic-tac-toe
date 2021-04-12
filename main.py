my_board = [
	["1", "2", "X"],
	["4", "5", "6"],
	["7", "8", "9"]
]

            
def print_board(board):
    print("|-------------|")
    print("| Tic Tac Toe |")
    print("|-------------|")
    print("|             |")
    print("|    " + board[0][0] + " " + board[0][1] + " " + board[0][2] + "    |")
    print("|    " + board[1][0] + " " + board[1][1] + " " + board[1][2] + "    |")
    print("|    " + board[2][0] + " " + board[2][1] + " " + board[2][2] + "    |")
    print("|             |")
    print("|-------------|")
    print()

print_board(my_board)

def game(print_board,board):
  game_finished = False
  while game_finished == False:
    x_move = input("where to put X: ")
    theBoard[x_move] = "X"
    print_board(theBoard)

    o_move = input("where to put O: ")
    theBoard[o_move] = "O"
    print_board(theBoard)
    


#def available_moves()

#def has_won()

#game(print_board,theBoard)