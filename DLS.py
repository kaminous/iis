ip = input("i/p - ")

graph = eval(ip)

depth_limit = int(input("Enter depth limit - "))
target = int(input("Enter element to search - "))

stack = [(0, 0)]      
vis = {0}
res = []
found = False

while stack:
    curr_ver, depth = stack.pop()
    res.append(curr_ver)
    
    if curr_ver == target:
        found = True
        print("Element Found!")

    if depth < depth_limit:        
        for neighbor in graph[curr_ver]:
            if neighbor not in vis:
                vis.add(neighbor)
                stack.append((neighbor, depth + 1))

if not found:
    print("Element Not Found!")                

print("o/p -", res)

#{0:[1,2],1:[3],2:[4],3:[],4:[]}