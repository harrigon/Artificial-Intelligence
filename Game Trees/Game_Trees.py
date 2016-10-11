def max_value(tree, alpha=float('-inf'), beta=float('inf')):
    if type(tree) is int:
        if abs(tree) != float('inf'):
            return tree

    v = -float('inf')
    for i in range(len(tree)):
        v = max(v, min_value(tree[i], alpha, beta))

        if v >= beta:
            if tree[i + 1:]:
                print("Pruning:", ", ".join(map(str, tree[i + 1:])))
            return v

        alpha = max(alpha, v)
    return v

def min_value(tree, alpha=float('-inf'), beta=float('inf')):
    if type(tree) is int:
        if abs(tree) != float('inf'):
            return tree
    v = float('inf')
    for i in range(len(tree)):
        v = min(v, max_value(tree[i], alpha, beta))

        if v <= alpha:
            if tree[i + 1:]:
                print("Pruning:", ", ".join(map(str, tree[i + 1:])))
            return v

        beta = min(beta, v)
    return v


