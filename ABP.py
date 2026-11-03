# Leaf values from left to right for a depth-3 binary tree (2^3 = 8 leaves)
leaves = [3, 5, 6, 9, 1, 2, 0, -1]

# List to keep track of pruned values
pruned_nodes = []

def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: if depth is 3, we have reached the leaf nodes
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):  # 2 children per node (Left and Right)
            child_index = node_index * 2 + i
            eval_val = alpha_beta(depth + 1, child_index, False, values, alpha, beta)
            max_eval = max(max_eval, eval_val)
            alpha = max(alpha, eval_val)
            
            # Alpha-Beta Pruning condition
            if beta <= alpha:
                # Record the branches/leaves that get cut off (pruned)
                for j in range(i + 1, 2):
                    pruned_nodes.append(values[child_index + (j - i)])
                break
        return max_eval
    
    else:
        min_eval = float('inf')
        for i in range(2):  # 2 children per node
            child_index = node_index * 2 + i
            eval_val = alpha_beta(depth + 1, child_index, True, values, alpha, beta)
            min_eval = min(min_eval, eval_val)
            beta = min(beta, eval_val)
            
            # Alpha-Beta Pruning condition
            if beta <= alpha:
                # Record the branches/leaves that get cut off (pruned)
                for j in range(i + 1, 2):
                    pruned_nodes.append(values[child_index + (j - i)])
                break
        return min_eval

# --- Run the Algorithm ---
# Start at depth 0, root index 0, Maximizing player, with -inf and +inf alpha/beta
optimal_solution = alpha_beta(0, 0, True, leaves, float('-inf'), float('inf'))

# --- Print Results ---
print("========================================")
print("       ALPHA-BETA PRUNING (Depth 3)     ")
print("========================================")
print(f"Final Optimal Solution (Root Value) : {optimal_solution}")
print(f"Pruned Nodes / Values List          : {pruned_nodes}")
print("========================================")