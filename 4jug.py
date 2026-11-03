from collections import deque

def water_jug_bfs(cap1, cap2, target):
    # Queue stores: (jug1_amount, jug2_amount, path_history)
    queue = deque([(0, 0, [(0, 0)])])
    visited = {(0, 0)}
    
    while queue:
        j1, j2, path = queue.popleft()
        
        # Check if the target is reached in either jug
        if j1 == target or j2 == target:
            return path
        
        # Possible actions (Next states)
        next_states = [
            (cap1, j2),                                           # 1. Fill Jug 1
            (j1, cap2),                                           # 2. Fill Jug 2
            (0, j2),                                              # 3. Empty Jug 1
            (j1, 0),                                              # 4. Empty Jug 2
            # 5. Pour Jug 1 -> Jug 2
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),
            # 6. Pour Jug 2 -> Jug 1
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))
        ]
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [state]))
                
    return None

# --- Run the Program ---
capacity_1 = 4  # 4-liter jug
capacity_2 = 3  # 3-liter jug
target_amount = 2  # Target is 2 liters

solution = water_jug_bfs(capacity_1, capacity_2, target_amount)

print("--- Water Jug Problem Solution (BFS) ---")
if solution:
    print(f"Goal reached in {len(solution) - 1} steps:\n")
    for step, (j1, j2) in enumerate(solution):
        print(f"Step {step}: [Jug 1: {j1}L, Jug 2: {j2}L]")
else:
    print("No solution possible.")