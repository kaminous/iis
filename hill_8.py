import random

def get_heuristic(state):
    """Calculates the number of attacking pairs of queens."""
    attacking_pairs = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Same row or same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

def get_best_neighbor(state):
    """Generates all neighbors and picks the one with the lowest heuristic value."""
    n = len(state)
    current_h = get_heuristic(state)
    best_state = list(state)
    best_h = current_h
    
    # Try moving each queen to every possible row in its column
    for col in range(n):
        original_row = state[col]
        for row in range(n):
            if row == original_row:
                continue
            
            # Create neighbor state
            neighbor = list(state)
            neighbor[col] = row
            neighbor_h = get_heuristic(neighbor)
            
            # Keep track of the best local neighbor
            if neighbor_h < best_h:
                best_h = neighbor_h
                best_state = neighbor
                
    return best_state, best_h

def hill_climbing_n_queens(n=8):
    """Solves N-Queens using Hill Climbing search."""
    # Generate a random initial state (one queen per column)
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_h = get_heuristic(current_state)
    
    steps = [list(current_state)]
    
    while True:
        best_neighbor, best_h = get_best_neighbor(current_state)
        
        # If no neighbor yields a strictly better cost, we are stuck (Local Minima)
        if best_h >= current_h:
            if current_h == 0:
                print(f"Goal State Found in {len(steps)} steps!")
                return current_state, True
            else:
                print(f"Stuck in a Local Minimum/Plateau at heuristic cost: {current_h}")
                return current_state, False
        
        current_state = best_neighbor
        current_h = best_h
        steps.append(list(current_state))

# Try solving 8-Queens
n = 8
solution, success = hill_climbing_n_queens(n)
print("Final State Representation (Rows for columns 0 to 7):", solution)
