# Set N = 4 for 4-Queens, or change to 8 for 8-Queens
N = 4

def is_safe(board, row, col):
    # Check all previously placed queens (in previous columns)
    for prev_col in range(col):
        prev_row = board[prev_col]
        
        # Constraint 1: Same row check
        # Constraint 2: Diagonal check (absolute difference in rows == difference in columns)
        if prev_row == row or abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def solve_n_queens(col, board):
    # Base case: If all queens are placed successfully
    if col == N:
        return True

    # Try every row in the current column
    for row in range(N):
        if is_safe(board, row, col):
            board[col] = row  # Assign value (CSP assignment)
            
            # Recursive step: Move to the next column
            if solve_n_queens(col + 1, board):
                return True
            
            # Backtrack if assignment doesn't lead to a solution
            board[col] = -1 

    return False

# Initialize board: board[col] stores the row index of the queen in that column
board = [-1] * N

if solve_n_queens(0, board):
    print(f"--- {N}-Queens Solution Found! ---\n")
    print(f"Queen positions per column: {board}\n")
    
    # Print the board visually
    for r in range(N):
        row_str = ""
        for c in range(N):
            if board[c] == r:
                row_str += " Q "
            else:
                row_str += " . "
        print(row_str)
else:
    print(f"No solution exists for {N}-Queens.")