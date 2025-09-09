import random
import copy

goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

def heuristic(state):
    manhattan_distance = 0
    goal_positions = {}
    for r in range(3):
        for c in range(3):
            goal_positions[goal_state[r][c]] = (r, c)

    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_r, goal_c = goal_positions[tile]
                manhattan_distance += abs(i - goal_r) + abs(j - goal_c)
    return manhattan_distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def hill_climbing(initial_state):
    current = initial_state
    current_h = heuristic(current)
    steps = 0

    print(f"Step {steps}:")
    for row in current:
        print(row)
    print(f"Heuristic value: {current_h}\n")

    while True:
        neighbors = get_neighbors(current)
        if not neighbors:
            return current, steps, current_h

        neighbor = min(neighbors, key=heuristic)
        neighbor_h = heuristic(neighbor)

        if neighbor_h >= current_h:
            if current_h > 0 and neighbors:
                current = random.choice(neighbors)
                current_h = heuristic(current)
                print(f"Step {steps + 1}: (Random Jump)")
                for row in current:
                    print(row)
                print(f"Heuristic value: {current_h}\n")
                continue
            return current, steps, current_h

        current, current_h = neighbor, neighbor_h
        steps += 1

        print(f"Step {steps}:")
        for row in current:
            print(row)
        print(f"Heuristic value: {current_h}\n")


        if current_h == 0:
            return current, steps, current_h

if __name__ == "__main__":
    initial_state = [[2, 8, 3],
                     [1, 6, 4],
                     [7, 0, 5]]

    print("Initial State:")
    for row in initial_state:
        print(row)

    solution, steps, h_val = hill_climbing(initial_state)

    print("\nFinal State after Hill Climbing:")
    for row in solution:
        print(row)
    print(f"Total steps taken: {steps}")
    print(f"Final heuristic value: {h_val}")
