ip = input("i/p (graph adj list with weights) - ")
heuristic_ip = input("Enter heuristics dict - ")

# The graph format expects node: [(neighbor, edge_weight), ...]
graph = eval(ip)
heuristics = eval(heuristic_ip)

target = int(input("Enter element to search - "))

# Queue stores elements as (f_value, g_value, vertex)
# f_value = g_value + heuristic
queue = [(heuristics[0], 0, 0)]      
vis = {0}
res = []
found = False

while queue:
    # Reverse sort allows pop() to efficiently remove the item with the lowest f_value
    queue.sort(reverse=True)
    curr_f, curr_g, curr_ver = queue.pop()
    res.append(curr_ver)
    
    if curr_ver == target:
        found = True
        print("Element Found!")
        break

    for neighbor, weight in graph[curr_ver]:
        if neighbor not in vis:
            vis.add(neighbor)
            g_neighbor = curr_g + weight
            f_neighbor = g_neighbor + heuristics[neighbor]
            queue.append((f_neighbor, g_neighbor, neighbor))

if not found:
    print("Element Not Found!")                

print("o/p -", res) 

'''
i/p (graph adj list with weights) - {0:[(1,3), (2,5)], 1:[(3,4)], 2:[(4,2)], 3: [], 4: []}
Enter heuristics dict - {0:10, 1:8, 2:2, 3:4, 4:0}
Enter element to search - 4
Element Found!
o/p - [0, 2, 4]
'''