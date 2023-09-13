import tkinter as tk
from tkinter import messagebox

# Định nghĩa biến toàn cục
board_size = 9
board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
player_turn = 'X'

def print_board():
    for i in range(board_size):
        for j in range(board_size):
            button_grid[i][j].config(text=board[i][j])

def check_win(player):
    for i in range(board_size):
        for j in range(board_size):
            if i + 4 < board_size and all(board[i + k][j] == player for k in range(5)):
                return True
            if j + 4 < board_size and all(board[i][j + k] == player for k in range(5)):
                return True
            if i + 4 < board_size and j + 4 < board_size and all(board[i + k][j + k] == player for k in range(5)):
                return True
            if i + 4 < board_size and j - 4 >= 0 and all(board[i + k][j - k] == player for k in range(5)):
                return True
    return False

def is_full():
    return all(cell != ' ' for row in board for cell in row)

def on_click(i, j):
    global player_turn
    if board[i][j] == ' ':
        board[i][j] = player_turn
        print_board()
        if check_win(player_turn):
            messagebox.showinfo("Kết quả", f"Người chơi {player_turn} thắng!")
        elif is_full():
            messagebox.showinfo("Kết quả", "Hòa!")
        else:
            player_turn = 'O' if player_turn == 'X' else 'X'

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Caro 9x9 (2 Người chơi)")

button_grid = [[None for _ in range(board_size)] for _ in range(board_size)]

for i in range(board_size):
    for j in range(board_size):
        button_grid[i][j] = tk.Button(root, text=' ', font=('normal', 20), width=2, height=1,
                                      command=lambda i=i, j=j: on_click(i, j))
        button_grid[i][j].grid(row=i, column=j)

root.mainloop()
