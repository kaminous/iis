# 0 represents the blank space
# Example solvable start state and target goal state
start = (1, 2, 3, 
         4, 0, 5, 
         7, 8, 6)

target = (1, 2, 3, 
          4, 5, 6, 
          7, 8, 0)

def heuristic(state, goal):
    # Manhattan distance heuristic for 8-puzzle
    dist = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            # Current row and column of the tile
            curr_r, curr_c = i // 3, i % 3
            # Target row and column of the tile
            target_idx = goal.index(tile)
            target_r, target_c = target_idx // 3, target_idx % 3
            dist += abs(curr_r - target_r) + abs(curr_c - target_c)
    return dist

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    r, c = zero_idx // 3, zero_idx % 3
    
    # 4 possible directions for the blank tile: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        # Check if the move is within the 3x3 grid boundaries
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero_idx = nr * 3 + nc
            # Swap the blank space with the neighboring tile
            state_list = list(state)
            state_list[zero_idx], state_list[new_zero_idx] = state_list[new_zero_idx], state_list[zero_idx]
            neighbors.append(tuple(state_list))
            
    return neighbors

# Queue stores: (f_value, g_value, current_state, path_so_far)
h_start = heuristic(start, target)
queue = [(h_start, 0, start, [start])]
vis = {start}
res = []
found = False
final_path = []

while queue:
    # Reverse sort allows pop() to efficiently remove the item with the lowest f_value
    queue.sort(reverse=True)
    curr_f, curr_g, curr_state, path = queue.pop()
    res.append(curr_state)
    
    if curr_state == target:
        found = True
        final_path = path
        print("Goal State Found!")
        break

    for neighbor in get_neighbors(curr_state):
        if neighbor not in vis:
            vis.add(neighbor)
            g_neighbor = curr_g + 1 # Each move has a cost of 1
            f_neighbor = g_neighbor + heuristic(neighbor, target)
            queue.append((f_neighbor, g_neighbor, neighbor, path + [neighbor]))

if not found:
    print("Goal Not Found!")

print(f"\nTotal states explored: {len(res)}")
print(f"Total steps to solve: {len(final_path) - 1}\n")

# Print the sequence of board configurations to reach the goal
print("--- Solution Path ---")
for step, s in enumerate(final_path):
    print(f"Step {step}:")
    print(f" {s[0]} {s[1]} {s[2]} ")
    print(f" {s[3]} {s[4]} {s[5]} ")
    print(f" {s[6]} {s[7]} {s[8]} ")
    print("-" * 9)