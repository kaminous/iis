def hill_climbing(graph, heuristics, start, target):
    curr_ver = start
    res = [curr_ver]

    if curr_ver == target:
        print("Element Found at Start!")
        print("Traversal", res)
        return True

    while True:
        neighbors = graph.get(curr_ver, [])

        if not neighbors:
            print("Stuck at a dead end (Local Maxima/Plateau)")
            break

        best_neighbor = min(neighbors, key=lambda x: heuristics.get(x, float('inf')))

        if heuristics.get(best_neighbor, float('inf')) >= heuristics.get(curr_ver, float('inf')):
            print("No better neighbor found (Local Maxima/Plateau reached).")
            break

        curr_ver = best_neighbor
        res.append(curr_ver)

        if curr_ver == target:
            print("Element Found!")
            print("Traversal", res)
            return True

    print("Traversal", res)
    return False

# Driver Code
ip_graph = input("Enter Graph (Adjacency List): ")
graph = eval(ip_graph)

ip_heuristic = input("Enter Heuristic Values for Nodes: ")
heuristics = eval(ip_heuristic)

start_node = int(input("Enter Start Element: "))
target_node = int(input("Enter Element to Search: "))

print("\nStarting Hill Climbing Search -")
found = hill_climbing(graph, heuristics, start_node, target_node)

if not found:
    print("\nElement Not Found or Search Stuck")

'''
Enter Graph (Adjacency List): {0:[1,2], 1:[3], 2:[4], 3: [], 4:[]}
Enter Heuristic Values for Nodes: {0:10, 1:6, 2:8, 3:0, 4:3}
Enter Start Element: 0
Enter Element to Search: 3
'''