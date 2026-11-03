# Tic-Tac-Toe Board (9 spots, initially empty)
board = [' ' for _ in range(9)]

def print_board(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]} ")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]} \n")

def check_winner(b, player):
    # All possible winning combinations (rows, columns, diagonals)
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]            # Diagonals
    ]
    return any(all(b[i] == player for i in condition) for condition in wins)

def is_board_full(b):
    return ' ' not in b

# Minimax Algorithm
def minimax(b, is_maximizing):
    # Base Cases: Score the terminal states
    if check_winner(b, 'O'):  # AI wins
        return 1
    if check_winner(b, 'X'):  # Human wins
        return -1
    if is_board_full(b):      # Tie
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'       # Try move
                eval_val = minimax(b, False)
                b[i] = ' '       # Undo move
                max_eval = max(max_eval, eval_val)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'       # Try move
                eval_val = minimax(b, True)
                b[i] = ' '       # Undo move
                min_eval = min(min_eval, eval_val)
        return min_eval

# Find the best move for the AI ('O')
def find_best_move(b):
    best_val = -float('inf')
    best_move = -1
    
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            move_val = minimax(b, False)
            b[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

# --- Example Demonstration ---
# Let's set up a scenario where Human ('X') made a move, and it's AI's turn to find the best response.
board[3] = 'X'  # Human plays top-left
print("Board after Human ('X') plays at position 3:")
print_board(board)

# AI calculates the best move
ai_move = find_best_move(board)
board[ai_move] = 'O'

print(f"AI ('O') chooses optimal position: {ai_move}")
print_board(board)