import random

# Item weights and values
weights = [2, 3, 4, 5, 6]
values = [20, 30, 40, 50, 60]

capacity = 10

# Calculate fitness
def fitness(chromosome):
    total_weight = sum(
        chromosome[i] * weights[i] for i in range(5)
    )

    total_value = sum(
        chromosome[i] * values[i] for i in range(5)
    )

    if total_weight > capacity:
        return 0

    return total_value

# Initial population
population = [
    [random.randint(0, 1) for _ in range(5)]
    for _ in range(10)
]

# Genetic Algorithm
for generation in range(100):

    population.sort(key=fitness, reverse=True)

    new_population = population[:5]

    while len(new_population) < 10:

        p1, p2 = random.sample(population[:5], 2)

        child = p1[:2] + p2[2:]

        if random.random() < 0.2:
            i = random.randint(0, 4)
            child[i] = 1 - child[i]

        new_population.append(child)

    population = new_population

# Best solution
best = max(population, key=fitness)

print("Best Selection:", best)
print("Maximum Value:", fitness(best))

print("Total Weight:",
      sum(best[i] * weights[i] for i in range(5)))