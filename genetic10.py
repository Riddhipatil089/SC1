import random

# -------------------------------
# PARAMETERS
# -------------------------------
TARGET = "HELLO WORLD"       # target string to evolve
POP_SIZE = 100               # number of individuals in population
MUTATION_RATE = 0.05         # probability of mutating a character
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "   # allowed characters

# -------------------------------
# FUNCTION: Create random string
# -------------------------------
def random_string(length):
    return "".join(random.choice(CHARACTERS) for _ in range(length))

# -------------------------------
# FUNCTION: Fitness = number of matching characters
# -------------------------------
def fitness(individual):
    return sum(1 for i in range(len(individual)) if individual[i] == TARGET[i])

# -------------------------------
# FUNCTION: Crossover between two parents
# -------------------------------
def crossover(p1, p2):
    cut = random.randint(0, len(TARGET)-1)
    return p1[:cut] + p2[cut:]

# -------------------------------
# FUNCTION: Mutation
# -------------------------------
def mutate(individual):
    letters = list(individual)
    for i in range(len(letters)):
        if random.random() < MUTATION_RATE:
            letters[i] = random.choice(CHARACTERS)
    return "".join(letters)

# -------------------------------
# MAIN GA LOOP
# -------------------------------
population = [random_string(len(TARGET)) for _ in range(POP_SIZE)]

generation = 0
best = ""

while best != TARGET:
    # Sort by fitness
    population = sorted(population, key=fitness, reverse=True)
    best = population[0]

    print(f"Gen {generation} → {best} | Fitness: {fitness(best)}")

    # Selection (top 20 survive)
    parents = population[:20]

    # Reproduction
    children = []
    for _ in range(POP_SIZE):
        p1 = random.choice(parents)
        p2 = random.choice(parents)
        child = mutate(crossover(p1, p2))
        children.append(child)

    population = children
    generation += 1
