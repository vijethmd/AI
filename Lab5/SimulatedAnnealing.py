import math
import random

def simulated_annealing(initial_state, cost_function, neighbour_function,
                        T_start=1000, T_end=1e-6, alpha=0.99):

    current = initial_state
    T = T_start

    while T > T_end:
        next_state = neighbour_function(current)
        current_cost = cost_function(current)
        next_cost = cost_function(next_state)
        dE = current_cost - next_cost

        if dE > 0:
            current = next_state
        else:
            p = math.exp(dE / T)
            if random.random() < p:
                current = next_state

        T *= alpha

    return current


def cost(x):
    return x * x

def neighbour(x):
    return x + random.uniform(-1, 1)

best = simulated_annealing(
    initial_state=random.uniform(-10, 10),
    cost_function=cost,
    neighbour_function=neighbour,
    T_start=1000,
    T_end=1e-6,
    alpha=0.995
)

print("Best solution found:", best)
print("Cost:", cost(best))
