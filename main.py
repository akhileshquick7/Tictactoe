import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("O-X Game - Akhilesh")

current_player = "X"
board = [""] * 9

def check_winner():
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for i,j,k in win_combos:
        if board[i] == board[j] == board[k] != "":
            return True
    return False

def click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            root.quit()
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", width=8, height=3, font=("Arial", 24),
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()

