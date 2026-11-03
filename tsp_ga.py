import random

# Distance between 4 cities
#5x5
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Calculate total distance
def fitness(route):
    total = 0

    for i in range(len(route)):
        a = route[i]
        b = route[(i + 1) % len(route)]
        total += dist[a][b]

    return total

# Generate initial population
population = [
    random.sample(range(4), 4) #(5), 5
    for _ in range(10)
]

# Genetic Algorithm
for generation in range(100):

    # Sort routes based on distance
    population.sort(key=fitness)

    # Select best 5 routes
    new_population = population[:5]

    # Crossover and mutation
    while len(new_population) < 10:

        p1, p2 = random.sample(population[:5], 2)

        child = p1[:2] + [x for x in p2 if x not in p1[:2]] #:3

        if random.random() < 0.2:
            i, j = random.sample(range(4), 2) #(5), 2
            child[i], child[j] = child[j], child[i]

        new_population.append(child)

    population = new_population

# Find best route
best = min(population, key=fitness)

print("Shortest Path:")
print(" -> ".join("ABCD"[i] for i in best) + " -> " + "ABCD"[best[0]]) #ABCDE

print("Minimum Distance:", fitness(best))