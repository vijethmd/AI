import random
import math


def compute_cost(state):
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            # Same row
            if state[i] == state[j]:
                cost += 1

            # Same diagonal
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost



def get_random_neighbor(state):
    n = len(state)
    new_state = state[:]

    col = random.randint(0, n - 1)          
    row = random.randint(1, n)              

    new_state[col] = row
    return new_state


def simulated_annealing(initial_state):
    current = initial_state
    current_cost = compute_cost(current)

    T = 30               
    Tmin = 0.1           
    alpha = 0.95         

    while T > Tmin and current_cost != 0:

       
        next_state = get_random_neighbor(current)
        next_cost = compute_cost(next_state)

        deltaE = next_cost - current_cost

        
        if deltaE < 0:
            current = next_state
            current_cost = next_cost
        else:
            prob = math.exp(-deltaE / T)
            if random.random() < prob:
                current = next_state
                current_cost = next_cost

        
        T *= alpha

    return current, current_cost



if __name__ == "__main__":
   
    initial_state = [random.randint(1, 8) for _ in range(8)]

    print("Initial State:", initial_state)
    final_state, final_cost = simulated_annealing(initial_state)

    print("\nFinal State:", final_state)
    print("Final Heuristic (0 means success):", final_cost)

    if final_cost == 0:
        print("\nSolution FOUND!")
    else:
        print("\nStopped at local minimum / annealing ended.")
