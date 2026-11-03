
import random

# Grid size
SIZE = 4

start = (0, 0)
goal = (3, 3)

obstacles = [(1, 1), (2, 1)]

# Actions: Up, Down, Left, Right
actions = [0, 1, 2, 3]

moves = {
    0: (-1, 0),   # Up
    1: (1, 0),    # Down
    2: (0, -1),   # Left
    3: (0, 1)     # Right
}

# Q-table: one row per cell, four actions per cell
Q = [[0.0] * 4 for _ in range(SIZE * SIZE)]

# Parameters
alpha = 0.1
gamma = 0.9
epsilon = 0.2
episodes = 1000


# Convert grid position to Q-table index
def get_state(pos):
    return pos[0] * SIZE + pos[1]


# Perform an action
def step(pos, action):
    dr, dc = moves[action]

    r = pos[0] + dr
    c = pos[1] + dc

    # Stay in place if outside the grid
    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return pos, -5, False

    new_pos = (r, c)

    # Penalty for hitting an obstacle
    if new_pos in obstacles:
        return pos, -5, False

    # Reward for reaching the goal
    if new_pos == goal:
        return new_pos, 10, True

    # Small penalty for each ordinary move
    return new_pos, -1, False


# Training
for episode in range(episodes):
    pos = start

    for _ in range(50):
        state = get_state(pos)

        # Epsilon-greedy action selection
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(actions, key=lambda a: Q[state][a])

        next_pos, reward, done = step(pos, action)
        next_state = get_state(next_pos)

        # Q-learning update
        Q[state][action] += alpha * (
            reward
            + gamma * max(Q[next_state])
            - Q[state][action]
        )

        pos = next_pos

        if done:
            break


# Display the learned path
pos = start
path = [pos]
visited = {pos}

for _ in range(50):
    state = get_state(pos)
    action = max(actions, key=lambda a: Q[state][a])

    next_pos, reward, done = step(pos, action)

    if next_pos == pos or next_pos in visited:
        print("Could not find a complete path.")
        break

    pos = next_pos
    path.append(pos)
    visited.add(pos)

    if done:
        print("Goal reached!")
        break

else:
    print("Step limit reached.")

print("Learned path:", path)

# Display the grid
for r in range(SIZE):
    row = []

    for c in range(SIZE):
        cell = (r, c)

        if cell == start:
            row.append("S")
        elif cell == goal:
            row.append("G")
        elif cell in obstacles:
            row.append("#")
        elif cell in path:
            row.append("*")
        else:
            row.append(".")

    print(" ".join(row))

