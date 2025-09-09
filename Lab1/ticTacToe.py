board = ["-"]*9
def print_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

def play_turn(player):
  pos = int(input(" Enter the position : "))
  pos = pos-1
  while(board[pos] != "-"):
    pos = int(input("Already Taken, choose another"))
  board[pos] = player

def decide():
  if((board[0] == board[1] == board[2] != "-") or 
  (board[3] == board[4] == board[5] != "-") or 
  (board[6] == board[7] == board[8] != "-") or 
  (board[0] == board[4] == board[8] != "-") or 
  (board[2] == board[4] == board[6] != "-") or 
  (board[0] == board[3] == board[6] != "-") or 
  (board[1] == board[4] == board[7] != "-") or 
  (board[2] == board[5] == board[8] != "-")):
    return "Win";
  elif("-" not in board):
    return "Tie"
  else:
    return "play"

def play_game():
  print_board()
  player = "X"
  gameOver = False
  while True:
    print(player,"'s turn")
    play_turn(player)
    print_board()
    decision = decide()
    if(decision == "Win"):
      print(player," wins!")
      break
    elif(decision == "Tie"):
      print("It's a Tie!")
      break
    else:
      if player == "X" :
        player = "O"
      else:
        player = "X"

play_game()
