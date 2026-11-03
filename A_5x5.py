# 5x5 Maze: 0 = Open path, 1 = Wall/Obstacle
maze = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0]
]

start = (0, 0)  # Top-left corner
target = (4, 4) # Bottom-right corner

def heuristic(pos, goal):
    # Manhattan distance heuristic
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

# Queue stores: (f_value, g_value, current_position, path_so_far)
h_start = heuristic(start, target)
queue = [(h_start, 0, start, [start])]
vis = {start}
res = []
found = False
final_path = []

while queue:
    # Reverse sort allows pop() to efficiently remove the item with the lowest f_value
    queue.sort(reverse=True)
    curr_f, curr_g, curr_ver, path = queue.pop()
    res.append(curr_ver)
    
    if curr_ver == target:
        found = True
        final_path = path
        print("Goal Found!")
        break

    # 4 possible directions: Down, Up, Right, Left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dr, dc in directions:
        neighbor = (curr_ver[0] + dr, curr_ver[1] + dc)
        r, c = neighbor
        
        # Check grid boundaries and obstacles
        if 0 <= r < 5 and 0 <= c < 5 and maze[r][c] == 0:
            if neighbor not in vis:
                vis.add(neighbor)
                g_neighbor = curr_g + 1 # Uniform step cost of 1
                f_neighbor = g_neighbor + heuristic(neighbor, target)
                queue.append((f_neighbor, g_neighbor, neighbor, path + [neighbor]))

if not found:
    print("Goal Not Found!")

print("\nTraversal Order (res):", res)
print("Final Shortest Path:", final_path)