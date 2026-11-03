import time

start = (1, 2, 3, 
         4, 0, 5, 
         7, 8, 6)

target = (1, 2, 3, 
          4, 5, 6, 
          7, 8, 0)

def heuristic_misplaced_tiles(state, goal):
    # Counts how many tiles are out of place (ignoring the blank tile 0)
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def heuristic_manhattan(state, goal):
    # Sum of Manhattan distances for each tile
    dist = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            curr_r, curr_c = i // 3, i % 3
            target_idx = goal.index(tile)
            target_r, target_c = target_idx // 3, target_idx % 3
            dist += abs(curr_r - target_r) + abs(curr_c - target_c)
    return dist

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    r, c = zero_idx // 3, zero_idx % 3
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero_idx = nr * 3 + nc
            state_list = list(state)
            state_list[zero_idx], state_list[new_zero_idx] = state_list[new_zero_idx], state_list[zero_idx]
            neighbors.append(tuple(state_list))
            
    return neighbors

def a_star_search(start, target, heuristic_func, name):
    start_time = time.time()
    h_start = heuristic_func(start, target)
    queue = [(h_start, 0, start, [start])]
    vis = {start}
    states_explored = 0
    found = False
    final_path = []

    while queue:
        queue.sort(reverse=True)
        curr_f, curr_g, curr_state, path = queue.pop()
        states_explored += 1
        
        if curr_state == target:
            found = True
            final_path = path
            break

        for neighbor in get_neighbors(curr_state):
            if neighbor not in vis:
                vis.add(neighbor)
                g_neighbor = curr_g + 1
                f_neighbor = g_neighbor + heuristic_func(neighbor, target)
                queue.append((f_neighbor, g_neighbor, neighbor, path + [neighbor]))

    elapsed_time = time.time() - start_time
    print(f"--- {name} ---")
    print(f"States Explored: {states_explored}")
    print(f"Solution Steps: {len(final_path) - 1 if found else 'N/A'}")
    print(f"Time Taken: {elapsed_time:.4f} seconds\n")

# Run both comparisons
a_star_search(start, target, heuristic_misplaced_tiles, "Heuristic 1: Misplaced Tiles")
a_star_search(start, target, heuristic_manhattan, "Heuristic 2: Manhattan Distance")