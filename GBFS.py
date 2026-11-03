ip = input("i/p (graph adj list) - ")
heuristic_ip = input("Enter heuristics dict - ")

graph = eval(ip)
heuristics = eval(heuristic_ip)

target = int(input("Enter element to search - "))

# Stack/List stores elements as (heuristic_value, vertex)
# Using a list sorted in descending order allows pop() to efficiently get the lowest heuristic
queue = [(heuristics[0], 0)]      
vis = {0}
res = []
found = False

while queue:
    queue.sort(reverse=True)
    curr_h, curr_ver = queue.pop()
    res.append(curr_ver)
    
    if curr_ver == target:
        found = True
        print("Element Found!")
        break

    for neighbor in graph[curr_ver]:
        if neighbor not in vis:
            vis.add(neighbor)
            queue.append((heuristics[neighbor], neighbor))

if not found:
    print("Element Not Found!")                

print("o/p -", res)
'''
i/p (graph adj list) - {0:[1,2], 1:[3,4], 2:[5], 3:[], 4:[],5:[]}
Enter heuristics dict - {0:10, 1:8, 2:5, 3:8, 4:2, 5:3}
Enter element to search - 4
Element Found!
o/p - [0, 2, 5, 1, 4]
'''