import time
import os

print ("hello")
board = "1|2|3\n4|5|6\n7|8|9"

board2 = [
  [None, None, None],
  [None, None, None],
  [None, None, None]
]

def gameplay(board): 
  while "|" in board:
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(board)
    player_1_move = input("Player 1's move") 
    if player_1_move in board:
      board = board.replace(player_1_move, "X")
    else:
      print ("Can't go there")
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(board)
    player_2_move = input("Player 2's move")
    if player_2_move in board:
      board = board.replace(player_2_move, "O")
    else:
      print ("Can't go there")

gameplay(board)

#newnew