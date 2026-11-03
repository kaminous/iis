import random

# Fitness function
def fitness(x):
    return x * x

# Initial population (5-bit chromosomes)
population = [
    [random.randint(0, 1) for _ in range(5)]
    for _ in range(6)
]

# Convert binary chromosome to decimal
def decode(chromosome):
    return int("".join(map(str, chromosome)), 2)

# Genetic Algorithm
for generation in range(20):
    population.sort(key=lambda c: fitness(decode(c)), reverse=True)

    new_population = population[:2]

    while len(new_population) < 6:
        p1, p2 = random.sample(population[:3], 2)

        point = random.randint(1, 4)
        child = p1[:point] + p2[point:]

        if random.random() < 0.1:
            i = random.randint(0, 4)
            child[i] = 1 - child[i]

        new_population.append(child)

    population = new_population

# Best solution
best = max(population, key=lambda c: fitness(decode(c)))
x = decode(best)

print("Best x:", x)
print("Maximum f(x):", fitness(x))