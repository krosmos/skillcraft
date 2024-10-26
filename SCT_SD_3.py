import customtkinter as ctk
import threading

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# app window
root = ctk.CTk()
root.geometry("620x750")
root.title("Sudoku Solver")

# Title text
title_frame = ctk.CTkFrame(master=root)
title_frame.grid(row=0, column=0, pady=5, padx=35, sticky="nsew")
app_title = ctk.CTkLabel(master=title_frame, text="Sudoku Solver", font=("HP Simplified", 27))
app_title.grid(row=0, column=0, padx=12, pady=8)

# Dictionary to store the entry widgets
entries = {}

# Main app frame
frame = ctk.CTkFrame(master=root)
frame.grid(row=1, column=0, pady=5, padx=35, sticky="nsew")

for i in range(3):
    for j in range(3):
        box = ctk.CTkFrame(master=frame)
        box.grid(row=i, column=j, pady=3, padx=3, sticky="nsew")
        
        for m in range(3):
            for n in range(3):
                row = i * 3 + m
                col = j * 3 + n
                
                entry = ctk.CTkEntry(master=box, width=28, justify="center")
                entry.grid(row=m, column=n, pady=1, padx=1)
                
                # Store the entry in the dictionary with (row, col) as the key
                entries[(row, col)] = entry

# Function to clear the grid
def clr_btn():
    for i in range(9):
        for j in range(9):
            entries[(i, j)].delete(0, "end")
    status_label.configure(text="")

# Function to check if it's safe to place a number
def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    return all(board[i + start_row][j + start_col] != num for i in range(3) for j in range(3))

# Function to solve the Sudoku using backtracking with constraint propagation
def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty
    possibilities = [num for num in range(1, 10) if is_safe(board, row, col, num)]
    for num in possibilities:
        board[row][col] = num
        if solve_sudoku(board):
            return True
        board[row][col] = 0
    return False

# Function to find an empty location on the board
def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

# Function to read the board from the UI
def get_board():
    board = []
    for row in range(9):
        board_row = []
        for col in range(9):
            val = entries[(row, col)].get()
            if val == '':
                board_row.append(0)
            else:
                board_row.append(int(val))
        board.append(board_row)
    return board

# Function to set the solved board back into the UI
def set_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                entries[(row, col)].delete(0, "end")
                entries[(row, col)].insert(0, str(board[row][col]))

# Function to solve the puzzle when the button is pressed
def solve_btn():
    status_label.configure(text="Solving...")
    board = get_board()

    def run_solver():
        if solve_sudoku(board):
            set_board(board)
            status_label.configure(text="Solution found!")
        else:
            status_label.configure(text="No solution exists.")

    # Run the solver in a separate thread
    solver_thread = threading.Thread(target=run_solver)
    solver_thread.start()

# Button container
btn_div = ctk.CTkFrame(master=root)
btn_div.grid(row=2, column=0, pady=5, padx=35, sticky="nsew")

# Solve Button
solve_button = ctk.CTkButton(master=btn_div, text="Solve", command=solve_btn)
solve_button.grid(row=0, column=0, pady=4)

# Clear Button
clr_button = ctk.CTkButton(master=btn_div, text="Clear", command=clr_btn)
clr_button.grid(row=0, column=1, pady=4, padx=4)

# Status label to indicate solving state
status_label = ctk.CTkLabel(master=root, text="", font=("HP Simplified", 16))
status_label.grid(row=3, column=0, pady=10, padx=35)

root.mainloop()
