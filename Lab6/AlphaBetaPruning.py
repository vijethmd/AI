INF = float("inf")

class AlphaBeta:
    def __init__(self, tree, leaf_values):
        self.tree = tree
        self.leaf_values = leaf_values
        self.pruned = []
        self.path = []

    def alpha_beta(self, root):
        value = self.max_value(root, -INF, INF, [])
        return value, self.path, self.pruned

    def max_value(self, node, alpha, beta, current_path):
        if node not in self.tree:
            return self.leaf_values[node]

        value = -INF

        for child in self.tree[node]:
            v = self.min_value(child, alpha, beta, current_path + [child])

            if v > value:
                value = v
                if node == current_path[0] if current_path else True:
                    self.path = [node] + (current_path + [child])

            if value >= beta:
                remaining = self.tree[node][self.tree[node].index(child)+1:]
                for r in remaining:
                    self.pruned.append((node, r))
                return value

            alpha = max(alpha, value)

        return value

    def min_value(self, node, alpha, beta, current_path):
        if node not in self.tree:
            return self.leaf_values[node]

        value = INF

        for child in self.tree[node]:
            v = self.max_value(child, alpha, beta, current_path + [child])

            if v < value:
                value = v

            if value <= alpha:
                remaining = self.tree[node][self.tree[node].index(child)+1:]
                for r in remaining:
                    self.pruned.append((node, r))
                return value

            beta = min(beta, value)

        return value


tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"]
}

leaf_values = {
    "D": 3,
    "E": 5,
    "F": 2,
    "G": 9
}

ab = AlphaBeta(tree, leaf_values)
value, path, pruned = ab.alpha_beta("A")

print("Value at Root (A):", value)
print("Best Path:", " -> ".join(path))
print("Pruned Branches:", pruned)
