import copy
import heapq

goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other): 
        return self.f < other.f

    def __hash__(self):
        return hash(str(self.state))

def heuristic(state, goal):
    goal_positions = {}
    for r in range(3):
        for c in range(3):
            goal_positions[goal[r][c]] = (r, c)
    manhattan_distance = 0
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

def get_neighbors(node):
    state = node.state
    neighbors = []
    x, y = find_blank(state)
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(Node(new_state, node))
    return neighbors

def distance(node1, node2):
    return 1

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path

def a_star(start_state, goal_state):
    start_node = Node(start_state)
    goal_node = Node(goal_state)

    open_list = []
    closed_set = set()

    start_node.g = 0
    start_node.h = heuristic(start_node.state, goal_state)
    start_node.f = start_node.g + start_node.h

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node == goal_node:
            return reconstruct_path(current_node)

        closed_set.add(current_node)

        for neighbor in get_neighbors(current_node):
            if neighbor in closed_set:
                continue

            tentative_g = current_node.g + distance(current_node, neighbor)

            if neighbor not in open_list or tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor.state, goal_state)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node


                heapq.heappush(open_list, neighbor)

    return None 

def print_state(state):
    for row in state:
        print(row)

if __name__ == "__main__":
    initial_state = [[2, 8, 3],
                     [1, 6, 4],
                     [7, 0, 5]]

    print("Initial State:")
    print_state(initial_state)
    print("\nGoal State:")
    print_state(goal_state)

    path = a_star(initial_state, goal_state)

    if path:
        print("\nPath from initial to goal state:")
        for step_num, state in enumerate(path):
            print(f"Step {step_num}:")
            print_state(state)
            print()
    else:
        print("No solution found.")
