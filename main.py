def print_board(board):
  for row in board:
      print(" | ".join(row))
      print("-" * 9)

def check_winner(board, player):
  for row in board:
      if all(cell == player for cell in row):
          return True

  for col in range(3):
      if all(board[row][col] == player for row in range(3)):
          return True

  if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
      return True

  return False

def tic_tac_toe():
  board = [[" " for _ in range(3)] for _ in range(3)]
  player = "X"

  for _ in range(9):
      print_board(board)
      while True:
          try:
              row = int(input(f"Player {player}, enter row number (0-2): "))
              col = int(input(f"Player {player}, enter column number (0-2): "))
              if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                  break
              else:
                  print("Invalid input or cell already taken. Try again.")
          except ValueError:
              print("Invalid input. Please enter numbers (0-2) for row and column.")

      board[row][col] = player

      if check_winner(board, player):
          print_board(board)
          print(f"Player {player} wins!")
          break

      player = "O" if player == "X" else "X"
  else:
      print_board(board)
      print("It's a tie!")

if __name__ == "__main__":
  tic_tac_toe()