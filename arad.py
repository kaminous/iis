ip = input("i/p (graph adj list) - ")
heuristic_ip = input("Enter heuristics dict - ")

graph = eval(ip)
heuristics = eval(heuristic_ip)

start = input("Enter start city - ")
target = input("Enter element to search - ")

# Stack/List stores elements as (heuristic_value, current_vertex, path_taken)
queue = [(heuristics[start], start, [start])]      
vis = {start}
res = []
final_path = []
found = False

while queue:
    # Sort in descending order so pop() removes the lowest heuristic element
    queue.sort(key=lambda x: x[0], reverse=True)
    curr_h, curr_ver, path = queue.pop()
    res.append(curr_ver)
    
    if curr_ver == target:
        found = True
        final_path = path
        print("Element Found!")
        break

    # Look through neighbors (handles graph layout format: [('City', cost), ...])
    for neighbor_tuple in graph.get(curr_ver, []):
        neighbor = neighbor_tuple[0]  # Extracts the city name string from the tuple
        if neighbor not in vis:
            vis.add(neighbor)
            queue.append((heuristics[neighbor], neighbor, path + [neighbor]))

if not found:
    print("Element Not Found!")                

print("Traversal order (All explored nodes) -", res)
print("Final Route Found -", final_path)

'''
i/p (graph adj list) - {0:[1,2], 1:[3,4], 2:[5], 3:[], 4:[],5:[]}
Enter heuristics dict - {0:10, 1:8, 2:5, 3:8, 4:2, 5:3}
Enter element to search - 4
Element Found!
o/p - [0, 2, 5, 1, 4]
'''